import os
import unittest
from lib_nz_task_info import *
from lib_nz_current_path import *

class TestTaskFunctions(unittest.TestCase):
    def setUp(self):
        self.current_path = os.path.dirname( os.path.realpath(__file__))
        self.project_id = 'testProject'
        self.task_info = {'task_id': 'testTaskId', 'caption': 'Test Task', 'description': 'This is a test.', 'priority': 'high'}


    def test_get_task_info_path_by_id(self):
        resFact = get_task_info_path_by_id(self.project_id, self.task_info['task_id'])
        expected = os.path.join(self.current_path, f"project_{self.project_id}")
        expected = os.path.join(expected, f"task_{self.task_info['task_id']}")
        self.assertEqual(expected, resFact)
        
        
    def test_save_task_info(self):
        save_task_info(self.project_id, self.task_info)
        resFact = read_task_info(self.project_id, self.task_info['task_id'])
        self.assertEqual(self.task_info, resFact)

    def test_is_attributes_exists(self):
        save_task_info(self.project_id, self.task_info)
        result = is_attributes_of_task_exists(self.project_id, self.task_info['task_id'])
        self.assertTrue(result)

    def test_get_attributes_of_task(self):
        result = get_attributes_of_task(self.project_id, self.task_info['task_id'])
        # Проверяем что атрибут был считан
        self.assertEqual(self.task_info.keys(), result)

if __name__ == '__main__':
    unittest.main()
