"""
测试APIClient实例
"""

import unittest

# 测试库
from qcloud_sdk.api import qcloud_api_client


class APIClientTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # APIClient实例
        cls.client = qcloud_api_client
