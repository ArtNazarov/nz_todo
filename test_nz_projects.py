from lib_nz_projects import *
import os
import unittest

class TestProjectManager(unittest.TestCase):

    def setUp(self):
        """Create a temporary file for testing."""
        self.file_path = get_index_path()
        with open(self.file_path, 'w') as f:
            f.write("1\n2\n3\n")

    def tearDown(self):
        """Remove the temporary file after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_project_id_new(self):
        """Test adding a new project ID."""
        add_project_id(4)
        expected_ids = ['1', '2', '3', '4']
        actual_ids = read_project_ids()
        self.assertEqual(actual_ids, expected_ids)

    def test_add_project_id_duplicate(self):
        """Test adding a duplicate project ID."""
        add_project_id(2)
        expected_ids = ['1', '2', '3']
        actual_ids = read_project_ids()
        self.assertEqual(actual_ids, expected_ids)

    def test_read_project_ids(self):
        """Test reading project IDs from the file."""
        expected_ids = ['1', '2', '3']
        actual_ids = read_project_ids()
        self.assertEqual(actual_ids, expected_ids)

if __name__ == '__main__':
    unittest.main()