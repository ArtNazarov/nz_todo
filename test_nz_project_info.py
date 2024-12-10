from lib_nz_project_info import *
import unittest

class TestTodoFunctions(unittest.TestCase):

    def setUp(self):
        self.project_id = "project_123"
        self.todo_info = {
            "caption": "Project Title",
            "description": "This is a detailed description of the project.",
            "priority": "High"
        }

    def test_save_and_read_todo_info(self):
        # Сохраним заметку
        save_todo_info(self.project_id, self.todo_info)

        # Считаем назад значение
        loaded_todo_info = read_todo_info(self.project_id)

        # Проверяем, что загруженная информация совпадает с сохраненной
        self.assertEqual(loaded_todo_info, self.todo_info)

if __name__ == '__main__':
    unittest.main()
