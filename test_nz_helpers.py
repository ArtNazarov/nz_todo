import unittest
from lib_nz_helpers import *

class TestTaskFunctions(unittest.TestCase):

    def test_overwrite_dict(self):
        d1 = {'key1' : 'value1', 'key2':'value2'}
        d2 = {'key2' : 'edited2', 'key3' : 'value3'}
        resFact = overwrite_dict(d1, d2)
        expected = {'key1' : 'value1', 'key2':'edited2', 'key3' : 'value3' }
        self.assertEqual(resFact, expected)
    
  