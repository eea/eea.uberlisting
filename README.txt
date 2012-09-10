================
EEA Uberlisting
================
`EEA Uberlisting`_  enhances and extends the listing layouts capabilities of Plone.

| It provides a set of attractive listing templates which can be applied 
| to any folderish content type in  Plone. 
|
| By default it adds a single **uberlisting_view** view method to the **Folder** Content Type, which gives   the web visitor the ability to switch the listing view with the views that are available for that Content Type, instead of having a fixed one.
 

By default this package also comes with the following listing templates which can be used as listing templates: 

  * subfolder view: summary view of sub-folders and its top content (2-level view) 
  * tabs view: folder overview with tabs
  * accordion view: folder_overview with accordion style (aka vertical tabs)

.. contents::

Tips and tricks
===============

Disable templates from showing up in the Uberlisting View
---------------------------------------------------------

  * In ZMI > context > manage_properties: Add a '*lines*' property named **bannedUberlistingTemplates**.

    Here add one by one the template id's that you would like to be skipped from the listing.

    ex: folder_summary_view

Set default template when visiting template for first time
----------------------------------------------------------

  * In ZMI > context > manage_properties: Add a '*string*' property named **defaultUberlistingTemplate**
    and add the template id that should be used as the default template.

    ex: folder_summary_view

    By default if this property isn't set and no cookie is present with the name of the default template
    then folder_listing will be used as default.

Choose the right templates to use for this package
--------------------------------------------------
  
  * The python logic that retrieves the contents of the template listings expects the template to 
    implement the **listing** macro. 
    
    By default all of the Plone templates implement this macro so all 
    templates that come from Plone and those that implement a listing macro to list results should 
    work with the Uberlisting View.

Get enhanced thumbnails when used with eea.depiction
----------------------------------------------------

  * If you have eea.depiction installed you can configure a fallback image for the contenttypes that
    do not have an image field by default, allowing the content to be displayed in  a view where the 
    listing would look better with images like album view.


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
  - `EEA jQuery`_

This package also supports eea.depiction. Thus the following dependencies are optional:
  - `EEA Depiction`_


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
.. _`EEA Uberlisting`: http://eea.github.com/docs/eea.uberlisting
.. _`EEA jQuery`: http://eea.github.com/docs/eea.jquery
.. _`EEA Depiction`: http://eea.github.com/docs/eea.depiction
.. _`plone.recipe.zope2instance`: http://pypi.python.org/pypi/plone.recipe.zope2instance
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
