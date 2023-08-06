from plone import api
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing import zope

import collective.elasticsearch


class ElasticSearch(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super().setUpZope(app, configurationContext)
        self.loadZCML(package=collective.elasticsearch)

    def setUpPloneSite(self, portal):
        super().setUpPloneSite(portal)
        # install into the Plone site
        applyProfile(portal, "collective.elasticsearch:default")
        setRoles(portal, TEST_USER_ID, ("Member", "Manager"))
        workflowTool = api.portal.get_tool("portal_workflow")
        workflowTool.setDefaultChain("plone_workflow")


ElasticSearch_FIXTURE = ElasticSearch()
ElasticSearch_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ElasticSearch_FIXTURE,), name="ElasticSearch:Integration"
)
ElasticSearch_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ElasticSearch_FIXTURE,), name="ElasticSearch:Functional"
)
ElasticSearch_API_TESTING = FunctionalTesting(
    bases=(ElasticSearch_FIXTURE, zope.WSGI_SERVER_FIXTURE),
    name="ElasticSearch:API",
)
