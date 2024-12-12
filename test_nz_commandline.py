import unittest
from unittest.mock import patch
from lib_nz_commandline import *


class TestGetModeFromCommandLine(unittest.TestCase):

    @patch('sys.argv', ['script_name', 'mode=test'])
    def test_mode_is_test(self):
        self.assertEqual(get_mode_from_commandline(), 'test')

    @patch('sys.argv', ['script_name', 'mode=production'])
    def test_mode_is_production(self):
        self.assertEqual(get_mode_from_commandline(), 'production')

    @patch('sys.argv', ['script_name'])
    def test_default_mode(self):
        self.assertEqual(get_mode_from_commandline(), 'dialog')

    @patch('sys.argv', ['script_name', 'other_arg=value'])
    def test_no_mode_argument(self):
        self.assertEqual(get_mode_from_commandline(), 'dialog')
    
    @patch('sys.argv', ['script_name', 'opcode=+P'])
    def test_get_operation_from_commandline_with_opcode(self):
        self.assertEqual(get_operation_from_commandline(), '+P')

    @patch('sys.argv', ['script_name', 'other_arg=value'])
    def test_get_operation_from_commandline_no_opcode(self):
        self.assertEqual(get_operation_from_commandline(), '')

    @patch('sys.argv', ['script_name', 'project_id=SomeProject'])
    def test_get_project_id_from_commandline_with_project_id(self):
        self.assertEqual(get_project_id_from_commandline(), 'SomeProject')

    @patch('sys.argv', ['script_name', 'other_arg=value'])
    def test_get_project_id_from_commandline_no_project_id(self):
        self.assertEqual(get_project_id_from_commandline(), '')

    @patch('sys.argv', ['script_name', 'task_id=SomeTask'])
    def test_get_task_id_from_commandline_with_project_id(self):
        self.assertEqual(get_task_id_from_commandline(), 'SomeTask')

    @patch('sys.argv', ['script_name', 'other_arg=value'])
    def test_get_task_id_from_commandline_no_project_id(self):
        self.assertEqual(get_task_id_from_commandline(), '')
    


if __name__ == '__main__':
    unittest.main()
