from tests.context import bookingsynclord
from bookingsynclord.data_store.GenericStore import GenericStore
from bookingsynclord.entities.Entity import Entity
from bookingsynclord import config

import unittest

class TestStore(GenericStore):
    def __init__(self,credential_manager):
        super(TestStore, self).__init__(credential_manager,"tests")
class TestEntity(Entity):
    ENTITY_TYPE = 'tests'
    def __init__(self,id = None):
        return super(TestEntity,self).__init__("tests",id)

class GenericStoreTest(unittest.TestCase):
    def setUp(self):
        self.test_store = TestStore(None)

    def test_entity_type_set(self):
        self.assertEqual(self.test_store.entity_type,'tests')

    def test_build_url(self):
        endpoint = "/tests"
        self.assertEqual(GenericStore.build_url(endpoint),config.APIURL_ENDPOINT + endpoint)

    def test_list_endpoint(self):
        expected = "/tests"
        self.assertEqual(expected,self.test_store.get_endpoint("LIST"))

    def test_get_endpoint(self):

        expected = "/tests/21"
        test_entity = TestEntity()
        test_entity.id = 21
        self.assertEqual(expected,self.test_store.get_endpoint("PUT",test_entity))

if __name__ == '__main__':
    unittest.main()
