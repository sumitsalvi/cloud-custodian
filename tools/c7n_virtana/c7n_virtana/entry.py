# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

import logging

# register provider
import c7n_virtana.provider

# squelch inconsiderate logging
logging.getLogger('googleapiclient.discovery').setLevel(logging.WARNING)


def initialize_virtana():
    """Load virtana provider"""

    # register execution modes
    import c7n_virtana.policy # noqa

    # load shared registered resources
    import c7n_virtana.actions
    import c7n_virtana.output # noq
