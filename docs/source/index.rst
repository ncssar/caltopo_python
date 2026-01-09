.. caltopo_python documentation master file

:tocdepth: 1

.. .. toctree::
..    .. :maxdepth: 2
..    :caption: Other pages:

..    credentials
..    caltopo_python

caltopo_python
==========================================

CalTopo is a very popular web-browser-based and smartphone-app-based mapping tool.  SARTopo is a mostly-obsolete
name that refers to a set of Search-And-Rescue-specific features inside the CalTopo tool. See |caltopo_link| and |training_link|.

Being a web-based tool, CalTopo uses a web API to accomplish most user actions.  In 2025, CalTopo released documentation for many parts of the API.  See |api_link|.  Other parts of the API, used by this module, are not documented by CalTopo and are subject to change at any time.

This module provides a 'session' object which manages a data connection to a hosted map, and provides several wrapper methods and convenience methods that make calls to the CalTopo API.

If your CalTopo account is a member of a CalTopo Team account, you can use this module for SAR-specific features on a caltopo.com map.

**This third-party module is not written or maintained by CalTopo LLC or the authors of caltopo.com.**

**DISCLAIMER: This module can edit and delete CalTopo map features.  At the time of this module's publication, CalTopo does not have any 'undo' capability.**
Only you can take steps to prevent loss of map data due to use of this module - whether due to accidental misuse, or due to an unexpected bug in the module.  You should always consider exporting a full GeoJSON from your map before using this code.

Categories of provided class methods:
   - account data access
   - feature creation
   - feature editing
   - feature querying
   - feature deletion
   - geometry operations

See the `CaltopoSession Class Reference <./caltopo_python.html>`_ for details.

Installation
============
Install this package in the usual manner:

.. code-block:: python
   
   pip install caltopo_python

To activate online requests, you will need to determine your account ID, credential ID, and public key.  See details at the |api_link| and older unofficial details on the :doc:`credentials` page.

**NOTE: caltopo_python was formerly called sartopo_python.**
caltopo_python 1.0.x will be identical to sartopo_python 2.0.x.  Only caltopo_python will get new versions going forward.

For more information on migrating from sartopo_python to caltopo_python, see the :doc:`migration` page.

Key Features
===============

Internet or locally-hosted
--------------------------
In addition to the standard caltopo.com web interface, CalTopo provides a downloadable local HTTP server
called CalTopo Desktop (formerly CalTopo Offline or SARTopo Offline).  This module works with either solution.

Configuration file
------------------
User account details, including the authentication public key (used to generate signed requests, as required by caltopo.com),
are kept in a local configuration file that you control.  A template configuration file comes with this package.

See the bottom of the Examples section for configuration file examples.  See the :doc:`credentials` page for details on authentication.

Mapless session
---------------
You may want to initialize the session without specifying a map, e.g. if you need to start
by checking the list of available maps before you know which map to open.

You can open a 'mapless' session by simply omitting the mapID argument when you initialize the session.  In that case, you can
open a map later, within the same session, with .openMap().

Any of the 'account data access methods' will work in a mapless session.
Most of the other class methods require an open map, so will fail with an error message if called in a mapless session.

Local cache
-----------
If the session is associated with a hosted map, this module will keep a local cache of the entire map data structure.  This reduces
the number of web requests needed, which reduces the time taken for most tasks.

Sync with callbacks
-------------------
To keep the local cache in sync with the hosted map, this module automatically requests and processes updates from the host at the specified sync interval.

This sync procedure is done in a background thread, so that it doesn't delay or interfere with your code.  Sync can be paused or disabled if needed.

You can also write callback functions that will be called whenever map data changes are found during sync.

Non-blocking requests  (new in 2.0.0)
-------------------------------------
Requests can be set to run in another thread ('in the background') so that main thread execution isn't delayed, regardless of connection quality.

See details in the :doc:`non-blocking` page.

Examples
========

Opening a session
-----------------

.. code-block:: python

   from caltopo_python import CaltopoSession

   # open an online session and map
   cts=CaltopoSession('caltopo.com','A1B2C3D',
         configpath='../../cts.ini',
         account='joe@domain.com')

   # open a CalTopo Desktop session and map
   cts=CaltopoSession('localhost:8080','A1B2C3D',
         configpath='../../cts.ini',
         account='joe@domain.com')

   # open an online mapless session
   cts=CaltopoSession('caltopo.com',
         configpath='../../cts.ini',
         account='joe@domain.com')

   # open a map, for a session that was initially mapless
   cts.openMap('A1B2C3D')
   
   # close the map, but leave the mapless session open
   cts.closeMap()

Syncing and callbacks
---------------------

.. code-block:: python

   # define callback functions
   def pucb(*args):
      print('Property Updated: pucb called with args '+str(args))

   def gucb(*args):
      print('Geometry Updated: gucb called with args '+str(args))

   def nfcb(*args):
      print('New Feature: nfcb called with args '+str(args))

   def dfcb(*args):
      print('Deleted Feature: dfcb called with args '+str(args))

   # open a session, connecting to the defined callbacks;
   #  syncing is enabled by default, since the 'sync' argument defaults to True
   cts=CaltopoSession('caltopo.com','A1B2C3D',
         configpath='../../cts.ini',
         account='joe@domain.com',
         propUpdateCallback=pucb,
         geometryUpdateCallback=gucb,
         newFeatureCallback=nfcb,
         deletedFeatureCallback=dfcb)

Getting map data and account data
---------------------------------

.. code-block:: python

   # get the personal map list (for joe@domain.com)
   cts.getMapList()

   # get the MyTeam map list (assuming joe@domain.com is a member of MyTeam)
   cts.getMapList('MyTeam')

   # get a dict of all map lists (for joe@domain.com)
   cts.getAllMapLists()

   # get the title of a map (assuming joe@domain.com has access to the map)
   cts.getMapTitle('A1B2C')

   # get the list of titles of group accounts of which joe@domain.com is a member
   cts.getGroupAccountTitles()

   # get the account's entire hierarchical listing of folders, maps, and bookmarks
   cts.getAccountsAndFolders()

Adding features
---------------

A word on longitude / latitude sequence:

caltopo.com expects each point of every type of geometry to have longitude first, followed by latutude, e.g. [120,-39].

While the code will swap coordinates if needed and if detectable (which is only the case for half of the globe), it's best to get in the habit of
specifying points in [lon,lat] sequence.  See the *._validatePoints* documentation for details.

This is opposite of the Marker functions, which call for the latitude argument first.  

.. code-block:: python

   # add a marker
   cts.addMarker(39,-120,'MyMarker')

   # add a folder
   fid=cts.addFolder('MyFolder')

   # add a marker in the folder
   myMarker2=cts.addMarker(39.01,-120.01,'MyMarker2',folderId=fid)
   
   # add a line
   cts.addLine([[-120,39],[-120.1,39.1]],'MyLine')

   # prepare to add a polygon - queue it for later
   cts.addPolygon([[-120,39],[-120.1,39.1],[-120,39.1]],'MyPolygon',queue=True)

   # add an Operational Period
   op1=cts.addOperationalPeriod('1')

   # prepare to add a line assignment - queue it for later
   aa=cts.addLineAssignment([[-120,39.2],[-120.1,39.2]],
         letter='AA',
         opId=op1,
         resourceType='DOG-TRAIL',
         description='FindEm',
         queue=True)

   cts.addAreaAssignment([[-120,39.3],[-120.1,39.4],[-120,39.4]],
         letter='AB',
         number='104',
         opId=op1,
         resourceType='DOG-AREA',
         description='FindEmFirst',
         responsivePOD='HIGH',
         priority='HIGH')

   # add the queued features now (MyPolygon and AA)
   cts.flush()

Querying and editing features
-----------------------------

.. code-block:: python

   myMarker=cts.getFeature('Marker','MyMarker')

   cts.editFeature(myMarker['id'],properties={'title','NewTitle'})

   cts.moveMarker(39,-121.5,myMarker['id'])

   cts.editMarkerDescription('New marker description',myMarker['id'])

Geometry operations
-------------------

.. code-block:: python

   # assuming all of the named features below have already been drawn

   # cut area assignment AC 103, using line b0
   cts.cut('AC 103','b0')

   # cut line a1, using line b1
   cts.cut('a1','b1')

   # cut polygon a8, using polygon b8, but do not delete b8 afterwards
   cts.cut('a8','b8',deleteCutter=False)

   # arguments are ids instead of entire features
   cts.cut(a12['id'],b12['id'])

   # expand polygon a7 to include polygon b7, a.k.a. "a7 = a7 OR b7"
   cts.expand('a7','b7')

   # crop line a14 using boundary poygon b14
   cts.crop('a14','b14')

   # crop line a15 using boundary polygon b15, with zero oversize
   cts.crop('a15','b15',beyond=0)

Deleting features
-----------------

.. code-block:: python

   cts.delFeature(aa)

   cts.delMarkers([myMarker,myMarker2])

Configuration file
------------------

.. code-block:: python

   # caltopo_python config file
   # This file contains credentials used to send API map requests
   #  to caltopo.com or CalTopo Desktop.
   # Protect and do not distribute these credentials.

   [joe@domain.com] # section referenced by 'account' session object attribute / argument
   id=A1B2C3D4E5F6 # 12-character credential ID
   key=............................................ # 44-character caltopo API key
   accountId=A1B2C3 # 6-character account ID


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

.. |caltopo_link| raw:: html

   <a href="https://caltopo.com" target="_blank">caltopo.com</a>

.. |training_link| raw:: html

   <a href="https://training.caltopo.com" target="_blank">training.caltopo.com</a>

.. |api_link| raw:: html

   <a href="https://training.caltopo.com/all_users/team-accounts/teamapi" target="_blank">Teams API documentation at training.caltopo.com</a>
   


