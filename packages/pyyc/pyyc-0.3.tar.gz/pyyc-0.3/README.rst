pyYC - a sample project
=======================

A sample project.

Package initialization (`__init__.py`)
--------------------------------------

>>> import pyyc
Initialisation top-level module
Initialisation module A1
Initialisation module A2
Initialisation sous-package B module + sous-package A module A1
>>> pyyc.subpkgA.modA1.version
'module A1'
>>> pyyc.subpkgB.version
'module A1 appelé depuis subpkgB.modB'

Main files (`__main__.py`)
--------------------------

The *main* program can be called in different ways:

* as the main entry of a module, e.g.::

    $ python -m pyyc arg1 arg2     # Execute pyyc/__main__.py
    Initialisation top-level module
    Initialisation module A1
    Initialisation module A2
    Initialisation sous-package B module + sous-package A module A1
    ---------------------- MAIN ----------------------
    Reading configuration from .../pyYC/pyyc/config/default.cfg...
    cfg-1.0
    Command line arguments: ['arg1', 'arg2']

* as command-line scripts defined as entry points in `setup.cfg`::

    $ pyyc arg1 arg2               # Execute pyyc/__main__.py:main()
    Initialisation top-level module
    Initialisation module A1
    Initialisation module A2
    Initialisation sous-package B module + sous-package A module A1
    ---------------------- MAIN ----------------------
    Reading configuration from .../pyYC/pyyc/config/default.cfg...
    cfg-1.0
    Command line arguments: ['arg1', 'arg2']    

    $ pyyc_addition 1 2            # Execute pyyc/mod.py:main_addition()
    Initialisation top-level module
    Initialisation sous-package A module A1
    Initialisation sous-package A module A2
    Initialisation sous-package B module + sous-package A module A1
    1 + 2 = 3
    
Source: https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    
Data files (e.g. `config/`)
---------------------------

Example to access data file at runtime:

>>> from pyyc.mod import read_config
>>> cfg = read_config()  # will look for config file distributed with pyyc package
Reading configuration from .../pyYC/pyyc/config/default.cfg...
>>> cfg['DEFAULT']['version']
'cfg-1.0'

Source: https://setuptools.pypa.io/en/latest/userguide/datafiles.html#accessing-data-files-at-runtime

To be completed
---------------

* sphinx documentation (`docs/`),
* continuous integration (`.gitlab-ci.yml`),
* tests (`tests/`),
* coverage.

To do
-----

* Display directory structure and content based on `this recipe
  <https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python>`_.
