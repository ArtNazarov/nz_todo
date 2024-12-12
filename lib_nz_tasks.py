""" Модуль для чтения-записи списка задач в проекте """
import sys
from lib_nz_current_path import get_tasks_index_path


def add_task_id(project_id: str, task_id: str) -> None:
    """
    Добавляет по указанному пути новый проект

    Параметры:
    project_id (str): строковый ID проекта
    task_id (str): строковый ID задачи из проекта
    """
    task_path_index = get_tasks_index_path(project_id)

    existing_ids = set()

    try:
        # Считаем существующие ID
        with open(task_path_index, 'r+', encoding='utf-8') as file:
            existing_ids = set(line.strip() for line in file)

    except FileNotFoundError as e:
        print(f"Maybe new file: {e}", file=sys.stderr)

    # Добавим новую задачу
    existing_ids.add(str(task_id))

    try:
        # Отсортируем и запишем в отсортированном виде
        with open(task_path_index, 'w', encoding='utf-8') as file:
            for task_id in sorted(existing_ids):
                file.write(f"{task_id}\n")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{
              task_path_index}'.", file=sys.stderr)
    except OSError as e:
        print(f"Error: An OS error occurred: {e}", file=sys.stderr)


def read_task_ids(project_id: str) -> list[str]:
    """
    Возвращает список проектов по индексному файлу

    index_path (str): путь к индексному файлу
    project_id (str): id проекта
    """
    task_path_index = get_tasks_index_path(project_id)
    try:
        # открываем список ID
        with open(task_path_index, 'r', encoding='utf-8') as file:
            # забираем список в упорядоченном виде
            task_ids = sorted(set(line.strip() for line in file))
        return task_ids
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return []


def delete_task_id(project_id: str, task_id: str) -> None:
    """
    Удаляет указанный проект по его ID из файла.

    Параметры:
    current_path (str): путь к индексу
    project_id (str): строковый ID проекта для удаления
    task_id (str): строкововый ID заметки
    """
    existing_ids = set()
    task_path_index = get_tasks_index_path(project_id)
    # print(f"Удаление затронет файл индекса проекта {task_path_index}...")
    try:
        # Считаем существующие ID
        with open(task_path_index, 'r+', encoding='utf-8') as file:
            existing_ids = set(line.strip() for line in file)

    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что путь указан правильно.",
              file=sys.stderr)

    # Удалим проект, если он существует
    existing_ids.discard(str(task_id))

    try:
        # Отсортируем и запишем в отсортированном виде
        with open(task_path_index, 'w', encoding='utf-8') as file:
            for task in sorted(existing_ids):
                file.write(f"{task}\n")
        # print(f"Задача с ID '{task_id}' успешно удалёна.")
    except FileNotFoundError:
        print(f"Error: The file path '{
              task_path_index}' was not found.", file=sys.stderr)
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{
              task_path_index}'.", file=sys.stderr)
    except OSError as e:
        print(f"Error: An OS error occurred: {e}", file=sys.stderr)

# Пример использования
# delete_task_id('path/to/index.projects', 'project_id', 'task_id_to_delete')
