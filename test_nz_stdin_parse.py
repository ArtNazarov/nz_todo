import unittest
from lib_nz_stdin_parse import *

class TestTaskFunctions(unittest.TestCase):

    def test_get_operations_list_inner(self):
        data = "opcode=vP # opcode=+P ; project_id=someProject"
        expected = [
            {'opcode' : 'vP'},
            {'opcode' : '+P', 'project_id' : 'someProject'}
        ];
        self.assertEqual(get_operations_list_inner(data), expected)
    
  