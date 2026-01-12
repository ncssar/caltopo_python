Non-blocking requests
==========================================

Caltopo_python version 1 only provided blocking request capability.  Caltopo_python version 2 (2.0.0 and onwards) allows non-blocking requests.

Blocking:

.. code-block:: python
    
    a=cts.addMarker(39,-120,'MyMarker')
    print(f'Done with addMarker: {a}')

The line doesn't get printed until the marker has been created, or the request times out.  Execution is 'blocked' until the addMarker function, including the HTTP request inside it, finishes.  This might not happen for several seconds, depending on the internet connection, the server response time, etc.

Non-blocking:

.. code-block:: python

    a=cts.addMarker(39,-120,'MyMarker',blocking=False)
    print(f'Done with addMarker: {a}')

blocking=False tells caltopo_python that the HTTP request should not block execution.  So, the line is printed 'immediately', regardless of internet connection or server response time or any other related connectivity issues.

This allows for seamless handling of intermittent or dropped internet connection, a slow server, or any related failures.

Behind the scenes, when blocking=False is specified, the HTTP request is enqueued, so code execution can move on quickly.  Another 'worker' thread is constantly watching that queue, and as soon as a new request is enqueued from the main thread, the worker thread immediately picks up the HTTP request for processing.

If the connection is 'good' at the time that a queued item is picked up for processing, then the HTTP request is sent.  But it's not removed from the queue until a valid response is received.  If the connection fails after the request has been sent, caltopo_python will keep trying to send the same request every few seconds until it gets a valid response.

Once a failed connection is detected, caltopo_python will not try to process any more queued requests until a valid response is received.  But you can keep adding to the queue e.g. with more addMarker calls.  Once the connection is re-established, the queue will be processed in the same first-in-first-out sequence.

Response values from non-blocking requests
------------------------------------------

So, in the code examples, what would actually get printed?

In the blocking example, the entire json dictionary of the marker would be printed (after the request is finished), or if there was a failure or a timeout, 'False' would be printed.

In the non-blocking example, the return value is only a True or False confirmation of whether the request was successfully enqueued.

So how do we make use of the newly created marker data in the non-blocking example?  With a callback:

.. code-block:: python

    def added(id):
        print(f'Callback triggered; id={id}')

    a=cts.addMarker(39,-120,'MyMarker',blocking=False,callbacks=[[added,['.result.id']]])
    print(f'Done with addMarker: {a}')

Which would probably give this output:

.. code-block:: python

    Done with addMarker: True
    Callback triggered; id=abcd1234....

So, the addMarker line returns 'immediately', but the callback isn't triggered until a valid HTTP response is received.  If everything is 'normal', this will happen just as quickly as the printed line from the blocking example.  But, if there is an intermittent or dropped connection, this might not happen for some time.

See the Callbacks section below for a full explanation of the callbacks argument.  In the example, after a valid HTTP response is received, 'added' will be called with only the 'id' value from the response passed as an argument.

Basically, your code will need to be written a bit differently to make use of non-blocking requests.

If needed, you can use both blocking and non-blocking requests in the same program - though you'll need to take care when considering the sequence of these events and their responses: there's no guarantee of the time that a non-blocking request will actually be processed successfully.

In general, non-blocking requests, and the asynchronous code structure needed to make them happen, should allow your code to be faster and more robust.  The overhead needed to change your old blocking requests to non-blocking requests with callbacks should be 'worth it' in most cases.

NOTE: an important consideration is that the callbacks will be called from the worker thread.  In PyQt, and in general, GUI actions must only be called from the main thread!  Silent mysterious crashes and unstable code are frequent and well-documented side effects of GUI actions called from non-main-thread code.  You can 'redirect' your callback to the main thread, by writing a worker-thread-callback and a companion main-thread-callback, and use the signal/slot mechanism to trigger the main-thread-callback from the worker-thread-callback.  You may also need to consider threading locks or other synchronization tools.

There are a few mechanisms you can use to specify whether a given request should be blocking or non-blocking:

- the session has an argument and variable 'blockingByDefault' (default=True)
- the optional blocking argument in each method can be used to override the blockingByDefault behavior
- if any callbacks are specified, the call will be non-blocking, regardless of the logic above; specification of callbacks and of blocking=True in the same call is an error condition: the error will be reported and the request will be skipped

So, in the example above, 'blocking=False' could be omitted: the presence of the callbacks argument is enough to make it a non-blocking request.

For example, if you have a piece of code written for blocking requests, and you want to preserve that functionality while switching to caltopo_python v2, you can specify blockingByDefault=True when creating the CaltopoSession object.

As you migrate your code to work in the non-blocking paradigm, you can change to blockingByDefault=False.

Also keep in mind that the main thread could end before a non-blocking response is available.  The request thread is a daemon thread, meaning that it does not prevent the main program from exiting.  So, if you want to be assured of getting a response to a non-blocking request, you should take other steps to make sure your main thread continues running until the response is available.

Callbacks
---------

Most of the methods that actually make HTTP requests have a standardized optional argument named 'callbacks', which can be specified as a list of lists.

Each list is of the form [function[,*args[,**kwargs]]] where function is the callable function object; args is a list of positional arguments for the callback; and kwargs is a dict of keyword arguments for the callback.

The callbacks argument is a list of lists because you may need to specify more than one callback function to be called.  The callbacks are called sequentially in whichever thread called _sendRequest and _handleResponse: if the request was blocking (in the main thread), them the callback/s will also be blocking (in the main thread).  But if the request was non-blocking, the callbacks will be run in the request thread meaning that no GUI calls can happen directly in those callbacks: you would need to do callback thread redirection with a signal mechanism, as in the NOTE above.

Some pre-processing is done on the callbacks argument value before the callback function/s are actually called:

- For add... methods, a standardized callback _addFeatureCallback is prepended (so that it is called first - even if no other callbacks are specified), with the request response passed as an argument.  _addFeatureCallback immediately adds the new feature to the cache.
- The entire response object is always available to the callback argument preprocessing; you don't need to specify returnJson='ALL' in the add... method call
- Argument values that are strings can use a placeholder syntax, to be evaluated at callback execution time (i.e. after the cache has been populated): if the string starts with a period, then periods are hierarchy delimiters, separating key names in the response's json dictionary.

 - '.a.b.c' is evaluated as 'r.json()["a"]["b"]["c"]' where r is the response object passed to _handleResponse
 - '.id' is evaluated as 'r.json()["id"]'
 - '.result.id' is the most commonly used, based on the CalTopo response structure, and is evaluated as 'r.json()["result"]["id"]'