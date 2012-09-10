================
EEA Uberlisting
================
`EEA Uberlisting`_  enhances and extends the listing layouts capabilities of Plone.

It provides a set of attractive listing templates which can be applied 
to any folderish content type in  Plone. 

Additionally, it adds a single 'smart' view listing which gives the web visitor the ability
to switch the listing view, instead of having a fixed one. 

Example of listing templates are: 

  * listing view: same as in standard plone
  * summary view: same as standard plone
  * album view: same as standard plone
  * folder overview: summary view of sub-folders and its top content (2-level view) 
  * tabs view: folder overview with tabs
  * accordion view: folder_overview with accordion style (aka vertical tabs)

Optionally you can get enhanced thumbnails if used together with eea.depiction

.. contents::


Installation
============

zc.buildout
-----------
If you are using `zc.buildout`_ and the `plone.recipe.zope2instance`_
recipe to manage your project, you can do this:

* Update your buildout.cfg file:

  * Add ``eea.uberlisting`` to the list of eggs to install
  * Tell the `plone.recipe.zope2instance`_ recipe to install a ZCML slug

  ::

    [instance]
    ...
    eggs =
      ...
      eea.uberlisting

    zcml =
      ...
      eea.uberlisting

* Re-run buildout, e.g. with::

  $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.


Dependencies
============

`EEA Uberlisting`_ has the following dependencies:
  - Plone 4+
  - eea.jquery 

This package also supports eea.depiction. Thus the following dependencies are optional:
  - eea.depiction


Source code
===========

Latest source code (Plone 4 compatible):
  - http://github.com/eea/eea.uberlisting
  - http://github.com/collective/eea.uberlisting


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The eea.uberlisting (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details under docs/License.txt


Funding and project management
==============================

EEA_ - European Environment Agency (EU)

.. _EEA: http://www.eea.europa.eu/
.. _`EEA Uberlisting: http://eea.github.com/docs/eea.uberlisting
.. _`plone.recipe.zope2instance`: http://pypi.python.org/pypi/plone.recipe.zope2instance
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
