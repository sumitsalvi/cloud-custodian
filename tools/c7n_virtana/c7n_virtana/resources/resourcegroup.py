# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

from c7n_virtana.provider import resources
import c7n.policy

@resources.register('resourcegroup')
class ResourceGroup():
    resource_type = "virtana.resourcegroup"

    def get_client(self):
        # Create and return the Virtana API client
        pass

    def get_resources(self, query=None):
        client = self.get_client()
        # Use the client to retrieve the list of resource groups
        # from the Virtana API
        pass


