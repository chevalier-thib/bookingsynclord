from tests.context import bookingsynclord
from bookingsynclord.data_store.GenericStore import GenericStore
from bookingsynclord import config

import unittest

class TestStore(GenericStore):
    def __init__(self,credential_manager):
        super(TestStore, self).__init__(credential_manager,"TEST")

class GenericStoreTest(unittest.TestCase):
    def setUp(self):
        self.test_store = TestStore(None)

    def test_entity_type_set(self):
        self.assertEqual(self.test_store.entity_type,'TEST')

    def test_build_url(self):
        endpoint = "/tests"
        self.assertEqual(GenericStore.build_url(endpoint),config.APIURL_ENDPOINT + endpoint)

    def test_list_endpoint(self):
        expected = "/tests"
        self.assertEqual(expected,self.test_store.get_endpoint("LIST"))


if __name__ == '__main__':
    unittest.main()
