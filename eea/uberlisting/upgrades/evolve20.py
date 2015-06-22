""" Layout upgrades
"""
import logging
from Products.CMFCore.utils import getToolByName
from eea.uberlisting.browser.app.interfaces import IUberlistingView
from zope.interface import alsoProvides
import transaction
logg = logging.getLogger("eea.uberlisting.upgrades")


def set_uberlisting_view(context):
    """ Set IUberlistingView interface to objects that have uberlisting_view
        set
    """
    ctool = getToolByName(context, 'portal_catalog')
    folders = ctool(portal_type="Folder")
    count = 0
    for brain in folders:
        if brain.getLayout() == 'uberlisting_view':
            logg.info(brain.getURL())
            obj = brain.getObject()
            alsoProvides(obj, IUberlistingView)
            obj.reindexObject(idxs=['object_provides'])
            count += 1
            if count % 10 == 0:
                logg.info("Committing uberlisting migration transaction")
                transaction.commit()

    logg.info("DONE adding IUberlistingView to objs with uberlisting template")
