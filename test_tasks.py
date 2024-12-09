import os
import unittest
import shutil
from lib_nz_tasks import get_tasks_index_path, add_task_id, read_task_ids, delete_task_id  

def getLines(filename):
    # Открываем файл и читаем его содержимое
    with open(filename, 'r') as file:
        # Читаем все строки, обрезаем пробелы и сохраняем в список
        trimmed_lines = [line.strip() for line in file.readlines()]
    return trimmed_lines


class TestTaskFunctions(unittest.TestCase):

    def setUp(self):
        self.project_id = "someTestProject"
        self.current_path = os.path.dirname( os.path.realpath(__file__))
        self.tasks_path = os.path.join(self.current_path, f"project_{self.project_id}")
        os.makedirs(self.tasks_path, exist_ok=True)

    def test_get_tasks_index_path(self):
        
        project_path = os.path.join(self.current_path, f'project_{self.project_id}')
        tasks_index_path_expected = os.path.join(project_path, 'index.tasks')
        tasks_index_path_fact =  get_tasks_index_path(self.current_path, self.project_id)
        
        self.assertEqual(tasks_index_path_expected, tasks_index_path_fact )
    
    def test_add_task_id(self):
        add_task_id(self.current_path, self.project_id, "1")
        add_task_id(self.current_path, self.project_id, "2")
        add_task_id(self.current_path, self.project_id, "3")
        add_task_id(self.current_path, self.project_id, "4")
        linesExpected = [ "1", "2", "3", "4" ]
        linesFact = read_task_ids(self.current_path, self.project_id)
        self.assertEqual(linesExpected, linesFact)     
        
    def test_delete_task_id(self):
        add_task_id(self.current_path, self.project_id, "1")
        add_task_id(self.current_path, self.project_id, "2")
        add_task_id(self.current_path, self.project_id, "3")
        add_task_id(self.current_path, self.project_id, "4")
        delete_task_id(self.current_path, self.project_id, "3")
        linesExpected = [ "1", "2", "4" ]
        linesFact = read_task_ids(self.current_path, self.project_id)
        self.assertEqual(linesExpected, linesFact)

    def tearDown(self):
        # Удаляем директорию после теста
        if os.path.exists(self.tasks_path):
            shutil.rmtree(self.tasks_path)


if __name__ == '__main__':
    unittest.main()
