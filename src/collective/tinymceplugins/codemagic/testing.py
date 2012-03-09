from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveTinymce_Codemagic(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.tinymceplugins.codemagic
        xmlconfig.file('configure.zcml',
                       collective.tinymceplugins.codemagic,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.tinymceplugins.codemagic:default')

COLLECTIVE_TINYMCE_CODEMAGIC_FIXTURE = CollectiveTinymce_Codemagic()
COLLECTIVE_TINYMCE_CODEMAGIC_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_TINYMCE_CODEMAGIC_FIXTURE, ),
                       name="CollectiveTinymce_Codemagic:Integration")
