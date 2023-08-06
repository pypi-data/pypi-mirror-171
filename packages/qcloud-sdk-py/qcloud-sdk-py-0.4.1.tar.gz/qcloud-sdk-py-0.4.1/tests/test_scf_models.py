"""

"""

import unittest

from qcloud_sdk.config import settings
from qcloud_sdk.scf.models import QCloudScfResource


class ScfCloudResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.resource_raw = {
            'region': 'ap-shanghai',
            'account': f'uin/{settings.UIN}',
            'namespace': settings.SCF_DEFAULT_NAMESPACE,
            'function_name': settings.TEST_SCF_FUNCTION_NAME,
        }

    def test_init(self):
        resource = QCloudScfResource(**self.resource_raw)

    def test_to_string(self):
        resource = QCloudScfResource(**self.resource_raw)
        resource_str = resource.to_string()
        print(resource_str)


if __name__ == '__main__':
    unittest.main()
