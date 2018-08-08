# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rescuearea.policy


class RescueareaPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rescuearea.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rescuearea.policy:default')


RESCUEAREA_POLICY_FIXTURE = RescueareaPolicyLayer()


RESCUEAREA_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RESCUEAREA_POLICY_FIXTURE,),
    name='RescueareaPolicyLayer:IntegrationTesting',
)


RESCUEAREA_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RESCUEAREA_POLICY_FIXTURE,),
    name='RescueareaPolicyLayer:FunctionalTesting',
)


RESCUEAREA_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RESCUEAREA_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RescueareaPolicyLayer:AcceptanceTesting',
)
