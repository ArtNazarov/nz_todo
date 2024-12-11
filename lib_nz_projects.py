import sys
import os
from lib_nz_current_path import get_cur_path


def get_index_path() -> str:
    return os.path.join(get_cur_path(), 'index.projects')


def add_project_id(project_id: str) -> str:
    """
    Добавляет по указанному пути новый проект

    Параметры:
    project_id (str): строковый ID проекта
    """
    index_path = get_index_path()
    existing_ids = set()

    try:
        # Считаем существующие ID
        with open(index_path, 'r+', encoding='utf-8') as file:
            existing_ids = set(line.strip() for line in file)

    except FileNotFoundError as e:
        print(f"Maybe new file: {e}", file=sys.stderr)

    # Добавим новый
    existing_ids.add(str(project_id))

    try:
        # Отсортируем и запишем в отсортированном виде
        with open(index_path, 'w', encoding='utf-8') as file:
            for project in sorted(existing_ids):
                file.write(f"{project}\n")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{
              index_path}'.", file=sys.stderr)
    except OSError as e:
        print(f"Error: An OS error occurred: {e}", file=sys.stderr)


def read_project_ids() -> list[str]:
    """
    Возвращает список проектов по индексному файлу

    """
    file_path = get_index_path()
    try:
        # открываем список ID
        with open(file_path, 'r+', encoding='utf-8') as file:
            # забираем список в упорядоченном виде
            project_ids = sorted(set(line.strip() for line in file))
        return project_ids
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return []


def delete_project_id(project_id: str) -> None:
    """
    Удаляет указанный проект по его ID из файла.

    Параметры:
    project_id (str): строковый ID проекта для удаления
    """
    index_path = get_index_path()
    existing_ids = set()

    try:
        # Считаем существующие ID
        with open(index_path, 'r', encoding='utf-8') as file:
            existing_ids = set(line.strip() for line in file)

    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что путь указан правильно.")

    # Удалим проект, если он существует
    existing_ids.discard(str(project_id))

    try:
        # Отсортируем и запишем в отсортированном виде
        with open(index_path, 'w', encoding='utf-8') as file:
            for project in sorted(existing_ids):
                file.write(f"{project}\n")
        print(f"Проект с ID '{project_id}' успешно удалён.")

    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{
              index_path}'.", file=sys.stderr)
    except OSError as e:
        print(f"Error: An OS error occurred: {e}", file=sys.stderr)

# Пример использования
# delete_project_id('project_id_to_delete')
