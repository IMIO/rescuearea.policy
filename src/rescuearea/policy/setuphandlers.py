# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from collective.ttwpo import api as poapi


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'rescuearea.policy:uninstall',
        ]


def post_install(context):
    """Post install script"""
    if 'rescuearea.core' not in poapi.domains():
        poapi.create('rescuearea.core', locales=['fr'])


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
