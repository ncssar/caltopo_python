<img src='./docs/source/_static/caltopo_python_logo.png' width=200px>

# caltopo_python

See this project's ReadTheDocs page.

CalTopo is a very popular web-browser-based and smartphone-app-based mapping tool. SARTopo is a mostly-obsolete name that refers to a set of Search-And-Rescue-specific features inside the CalTopo tool. See [caltopo.com](https://caltopo.com) and [training.caltopo.com](https://training.caltopo.com).

Being a web-based tool, CalTopo uses a web API to accomplish most user actions. The API is not currently documented or developed for general public use, and could change at any time.

This module provides a ‘session’ object which manages a data connection to a hosted map, and provides several wrapper methods and convenience methods that make calls to the non-publicized CalTopo API.

If your CalTopo account is a member of a SAR team account, you can use this module for SAR-specific features on a caltopo.com map.

**This third-party module is not written or maintained by CalTopo LLC or the authors of caltopo.com.**

**DISCLAIMER: This module can edit and delete CalTopo map features. At the time of this module’s publication, CalTopo does not have any ‘undo’ capability.** Only you can take steps to prevent loss of map data due to use of this module - whether due to accidental misuse, or due to an unexpected bug in the module. You should always consider exporting a full GeoJSON from your map before using this code.

## Categories of provided class methods:
- account data access
- feature creation
- feature editing
- feature querying
- feature deletion
- geometry operations

## Installation
Install this package in the usual manner:
```
pip install caltopo_python
```

To activate online requests, you will need to determine your account ID, credential ID, and public key. See details at the ReadTheDocs Credentials page.

**NOTE: caltopo_python was formerly called sartopo_python. caltopo_python 1.0.x will be identical to sartopo_python 2.0.x.**

For more information, see the ReadTheDocs Migration page.
