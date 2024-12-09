import os
from lib_nz_current_path import *

def get_tasks_index_path(project_id):
    current_path = get_cur_path()
    tasks_path = os.path.join(current_path, f"project_{project_id}")
    if not os.path.exists(tasks_path):
        os.makedirs(tasks_path)

    task_path_index = os.path.join(tasks_path, "index.tasks")
    return task_path_index


def add_task_id(project_id, task_id):
    """
    Добавляет по указанному пути новый проект

    Параметры:
    project_id (str): строковый ID проекта
    task_id (str): строковый ID задачи из проекта
    """
    current_path = get_cur_path()
    task_path_index = get_tasks_index_path(project_id)
    
    existing_ids = set()

    try:
        # Считаем существующие ID
        with open(task_path_index, 'r') as file:
            existing_ids = set(line.strip() for line in file)

    except Exception as e:
        print(f"Maybe new file: {e}")

    # Добавим новую задачу
    existing_ids.add(str(task_id))
    
    try:
        # Отсортируем и запишем в отсортированном виде
        with open(task_path_index, 'w') as file:
            for task_id in sorted(existing_ids):
                file.write(f"{task_id}\n")
    except Exception as e:
        print(f"Error: {e}")

                

def read_task_ids(project_id):
    """
    Возвращает список проектов по индексному файлу

    index_path (str): путь к индексному файлу
    project_id (str): id проекта
    """
    current_path = get_cur_path()
    task_path_index = get_tasks_index_path(project_id)
    try:
        # открываем список ID 
        with open(task_path_index, 'r') as file:
            # забираем список в упорядоченном виде
            task_ids = sorted(set(line.strip() for line in file))
        return task_ids
    except Exception as e:
        # print(f"Error: {e}")
        return []


def delete_task_id(project_id, task_id):
    """
    Удаляет указанный проект по его ID из файла.

    Параметры:
    current_path (str): путь к индексу
    project_id (str): строковый ID проекта для удаления
    task_id (str): строкововый ID заметки
    """
    current_path = get_cur_path() 
    existing_ids = set()
    task_path_index = get_tasks_index_path(project_id)
    try:
        # Считаем существующие ID
        with open(task_path_index, 'r') as file:
            existing_ids = set(line.strip() for line in file)

    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что путь указан правильно.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Удалим проект, если он существует
    existing_ids.discard(str(task_id))

    try:
        # Отсортируем и запишем в отсортированном виде
        with open(task_path_index, 'w') as file:
            for task in sorted(existing_ids):
                file.write(f"{task}\n")
        print(f"Задача с ID '{task_id}' успешно удалёна.")
        
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

# Пример использования
# delete_task_id('path/to/index.projects', 'project_id', 'task_id_to_delete')



