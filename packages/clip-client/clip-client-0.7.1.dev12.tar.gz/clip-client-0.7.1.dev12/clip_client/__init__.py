__version__ = '0.7.1.dev12'

import os

from clip_client.client import Client

if 'NO_VERSION_CHECK' not in os.environ:
    from clip_client.helper import is_latest_version

    is_latest_version(github_repo='clip-as-service')
