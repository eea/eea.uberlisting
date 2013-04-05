""" Uberlisting Forms
"""

from eea.uberlisting import EEAMessageFactory as _
from eea.uberlisting.browser.app.interfaces import IUberlistingForm
from eea.uberlisting.browser.app.view import _redirect
from z3c.form import form, field, button
from plone.z3cform.layout import wrap_form


class UberlistingForm(form.EditForm):
    """ Returns uberTemplate if present in request
    """
    fields = field.Fields(IUberlistingForm)

    @button.buttonAndHandler(_(u'Cancel'))
    def handleCancel(self, action):
        """ Cancel form edit
        """
        _redirect(self, _('Canceled uberlisting configuration changes'))

    @button.buttonAndHandler(_(u'Save'))
    def handleSave(self, action):
        """ Save form data
        """
        data, errors = self.extractData()
        if errors:
            return False
        else:
            self.applyChanges(data)
            _redirect(self, _('Saved uberlisting configuration changes'))


UberlistingFormView = wrap_form(UberlistingForm)
