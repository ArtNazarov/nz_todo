from lib_nz_current_path import *

def get_index_path():
    return os.path.join(get_cur_path(), 'index.projects')

def add_project_id(project_id):
    """
    Добавляет по указанному пути новый проект

    Параметры:
    project_id (str): строковый ID проекта
    """
    index_path = get_index_path()
    existing_ids = set()

    try:
        # Считаем существующие ID
        with open(index_path, 'r') as file:
            existing_ids = set(line.strip() for line in file)

    except Exception as e:
        print(f"Maybe new file: {e}")

    # Добавим новый
    existing_ids.add(str(project_id))
    
    try:
        # Отсортируем и запишем в отсортированном виде
        with open(index_path, 'w') as file:
            for project in sorted(existing_ids):
                file.write(f"{project}\n")
    except Exception as e:
        print(f"Error: {e}")

                
    

def read_project_ids():
    """
    Возвращает список проектов по индексному файлу

    """
    file_path = get_index_path()
    try:
        # открываем список ID 
        with open(file_path, 'r') as file:
            # забираем список в упорядоченном виде
            project_ids = sorted(set(line.strip() for line in file))
        return project_ids
    except Exception as e:
        # print(f"Error: {e}")
        return []


def delete_project_id(project_id):
    """
    Удаляет указанный проект по его ID из файла.

    Параметры:
    project_id (str): строковый ID проекта для удаления
    """
    index_path = get_index_path()
    existing_ids = set()

    try:
        # Считаем существующие ID
        with open(index_path, 'r') as file:
            existing_ids = set(line.strip() for line in file)

    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что путь указан правильно.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Удалим проект, если он существует
    existing_ids.discard(str(project_id))

    try:
        # Отсортируем и запишем в отсортированном виде
        with open(index_path, 'w') as file:
            for project in sorted(existing_ids):
                file.write(f"{project}\n")
        print(f"Проект с ID '{project_id}' успешно удалён.")
        
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

# Пример использования
# delete_project_id('project_id_to_delete')
