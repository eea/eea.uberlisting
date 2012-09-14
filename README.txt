================
EEA Uberlisting
================
`EEA Uberlisting`_  enhances and extends the listing layouts capabilities of Plone.

| By default it adds a single **uberlisting_view** view method to the **Folder** 
  Content Type, which when set as the default View gives the web visitor the 
  ability to switch between the views that are available for that Content Type,
  instead of having a fixed one, all from the same template.
|

.. contents::

Tips and tricks
===============

Choose the right templates to use for this package
--------------------------------------------------
  
  * The python logic that retrieves the contents of the template listings 
    expects the template to implement the **listing** macro. 
    
    By default all of the Plone templates implement this macro so all 
    templates that come from Plone and those that implement a listing macro 
    to list results should work with the Uberlisting View.

Disable templates from showing up in the Uberlisting View
---------------------------------------------------------

  * In ZMI > context > manage_properties: Add a '*lines*' property named 
    **bannedUberlistingTemplates**.

    Here add one by one the template id's that you would like to be skipped 
    from the listing.

    ::

     ex: folder_summary_view
         folder_contents

Set default template when visiting template for first time
----------------------------------------------------------

  * In ZMI > context > manage_properties: Add a '*string*' property named 
    **defaultUberlistingTemplate** and add the template id that should be used
    as the default template.

    ex: folder_summary_view

    By default if this property isn't set and no cookie is present with the name
    of the default template then **folder_listing** will be used as default.

Get listing of templates as images instead of template title name
-----------------------------------------------------------------

  * This packages looks for a png image to use for the views listing in the 
    format of template id + '.png'.

    ex: folder_summary_view.png
   
    We have provides some images for the common Plone templates as well as
    some for our own templates, if you need a different style for the icons you can
    customize them TTW or you can have a skin layer before **uberlisting_imgs** with
    images that have the same name.

  * If no images are found then the template name will be displayed in the listing.

  * If you don't want to have the listing of templates with images and you would
    prefer to have only template name then In ZMI > context > manage_properties:
    Add a checked **boolean** property named '**noUberlistingTemplateImages**'

Get enhanced thumbnails when used with eea.depiction
----------------------------------------------------

  * If you have eea.depiction installed you can configure a fallback image for
    the contenttypes that do not have an image field by default, allowing the 
    content to be displayed in  a view where the listing would look better 
    with images like album view.

Get enhanced search capabilities when used with eea.facetednavigation
---------------------------------------------------------------------

  * If you have eea.facetednavigation installed you can use uberlisting_view as
    a view for the Faceted Navigation, allowing you to combine the search capabilities
    of it with the ability to change between views from the same template. 


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
  - `EEA jQuery`_ - we are depending and loading only the `jquery.bbq`_ plugin

This package also supports other EEA Packages. Thus the following dependencies are optional:
  - `EEA Depiction`_
  - `EEA Faceted Navigation`_


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
.. _`EEA Faceted Navigation`: http://eea.github.com/docs/eea.facetednavigation
.. _`jquery.bbq`: https://github.com/cowboy/jquery-bbq
.. _`plone.recipe.zope2instance`: http://pypi.python.org/pypi/plone.recipe.zope2instance
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
