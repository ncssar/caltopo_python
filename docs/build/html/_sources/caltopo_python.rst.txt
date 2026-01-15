:tocdepth: 3

caltopo\_python module
======================

This module provides one main class: CaltopoSession.  Class methods are categorized and documented below.

Downstream code should create and use one instance of this class.

An exception class is also defined, CTSException, which could be thrown during initialization but is not documented here.

.. see https://stackoverflow.com/a/48682589/3577105 for categorization technique
.. currentmodule:: caltopo_python

.. autoclass:: CaltopoSession

.. omitting class name from automethod calls, when the section headers are unindented,
..   causes these failures, but, the headers need to be unindented for the TOC to recognize them:
.. WARNING: don't know which module to import for autodocumenting 'openMap' (try placing a "module" or "currentmodule" directive in the document, or giving an explicit module name)

.. **Session setup methods**
.. -------------------------

.. automethod:: CaltopoSession.openMap
.. automethod:: CaltopoSession.closeMap

**Account data access methods**
-------------------------------
These methods may be called from either a mapless or a map-associated session.

   .. automethod:: CaltopoSession.getAccountData
   .. automethod:: CaltopoSession.getMapList
   .. automethod:: CaltopoSession.getAllMapLists
   .. automethod:: CaltopoSession.getMapTitle
   .. automethod:: CaltopoSession.getAccountsAndFolders
   .. automethod:: CaltopoSession.getGroupAccountTitles

**Feature creation methods**
----------------------------
Most of these feature creation methods can be used to edit an existing feature,
by specifying the existingId argument.  .editFeature is a convenience method
that calls the appropriate .add... method with existingId specified.

   .. automethod:: CaltopoSession.addFolder
   .. automethod:: CaltopoSession.addMarker
   .. automethod:: CaltopoSession.addLine
   .. automethod:: CaltopoSession.addPolygon
   .. automethod:: CaltopoSession.addOperationalPeriod
   .. automethod:: CaltopoSession.addAssignment
   .. automethod:: CaltopoSession.addAreaAssignment(...,geomType='Area')
      
      Convenience method that calls addAssignment with geomType='Area'

   .. automethod:: CaltopoSession.addLineAssignment(...,geomType='Line')

      Convenience method that calls addAssignment with geomType='Line'

   .. automethod:: CaltopoSession.addLiveTrack
   .. automethod:: CaltopoSession.flush

**Feature query methods**
-------------------------

   .. automethod:: CaltopoSession.getFeature
   .. automethod:: CaltopoSession.getFeatures
      
**Feature editing methods**
---------------------------

   .. automethod:: CaltopoSession.editFeature
   .. automethod:: CaltopoSession.moveMarker
   .. automethod:: CaltopoSession.editMarkerDescription
   .. automethod:: CaltopoSession.updateLiveTrack
   .. automethod:: CaltopoSession.stopLiveTrack

**Feature deletion methods**
----------------------------

   .. automethod:: CaltopoSession.delFeature
   .. automethod:: CaltopoSession.delFeatures
   .. automethod:: CaltopoSession.delMarker
   .. automethod:: CaltopoSession.delMarkers

**Geometry operation methods**
------------------------------
These methods use the python |shapely_link| module.

   .. automethod:: CaltopoSession.cut
   .. automethod:: CaltopoSession.expand
   .. automethod:: CaltopoSession.crop
   .. automethod:: CaltopoSession.getBounds

**Internal data management methods**
------------------------------------
These methods are typically only called internally, from other class methods.  They can be called from downstream code if needed, with caution.  Not all internal data management methods are documented.

   .. automethod:: CaltopoSession._setupSession
   .. automethod:: CaltopoSession._sendUserdata
   .. automethod:: CaltopoSession._doSync
   .. automethod:: CaltopoSession._refresh
   .. automethod:: CaltopoSession.__del__
   .. automethod:: CaltopoSession._start
   .. automethod:: CaltopoSession._stop
   .. automethod:: CaltopoSession._pause
   .. automethod:: CaltopoSession._resume
   .. automethod:: CaltopoSession._syncLoop
   .. automethod:: CaltopoSession._sendRequest
   .. automethod:: CaltopoSession._requestWorker
   .. automethod:: CaltopoSession._handleResponse
   .. automethod:: CaltopoSession._addFeature
   .. automethod:: CaltopoSession._delAsync
   .. automethod:: CaltopoSession._buffer2
   .. automethod:: CaltopoSession._intersection2

**Internal helper methods**
---------------------------
These methods are typically only called internally, from other class methods.  They can be called from downstream code if needed, with caution.  Not all internal helper methods are documented.

   .. automethod:: CaltopoSession._caseMatch
   .. automethod:: CaltopoSession._twoify
   .. automethod:: CaltopoSession._fourify
   .. automethod:: CaltopoSession._removeDuplicatePoints
   .. automethod:: CaltopoSession._removeSpurs
   .. automethod:: CaltopoSession._getUsedSuffixList
   .. automethod:: CaltopoSession._getNextAvailableSuffix
   .. automethod:: CaltopoSession._validatePoints
   .. automethod:: CaltopoSession._getToken

.. |shapely_link| raw:: html

   <a href="https://shapely.readthedocs.io/en/stable/" target="_blank">Shapely</a>