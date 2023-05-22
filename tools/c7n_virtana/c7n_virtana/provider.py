# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

from functools import partial

from c7n.provider import Provider, clouds
from c7n.registry import PluginRegistry
from c7n.utils import local_session
from .client import Session

from c7n_virtana.resources.resource_map import ResourceMap

import logging

log = logging.getLogger('custodian.provider')


@clouds.register('virtana')
class Virtana(Provider):

    display_name = 'Virtana'
    resource_prefix = 'virtana'
    resources = PluginRegistry('%s.resources' % resource_prefix)
    resource_map = ResourceMap
    # region_to_cloud = {
    #     'VirtanaCloud': VIRTANA_PRIVATE_CLOUD
    # }

    cloud_endpoints = None

    def initialize(self, options):
        return options

    def initialize_policies(self, policy_collection, options):
        return policy_collection

    def get_session_factory(self, options):
        return partial(Session, project_id=options.account_id)


resources = Virtana.resources
