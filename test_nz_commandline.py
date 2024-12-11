import unittest
from unittest.mock import patch
from lib_nz_commandline import get_mode_from_commandline


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


if __name__ == '__main__':
    unittest.main()
