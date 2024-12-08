def add_project_id(index_path, project_id):
    """
    Добавляет по указанному пути новый проект

    Параметры:
    index_path (str): путь к индексу
    project_id (str): строковый ID проекта
    """
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

                
    

def read_project_ids(file_path):
    """
    Возвращает список проектов по индексному файлу

    file_path (str): путь к индексному файлу
    """
    try:
        # открываем список ID 
        with open(file_path, 'r') as file:
            # забираем список в упорядоченном виде
            project_ids = sorted(set(line.strip() for line in file))
        return project_ids
    except Exception as e:
        # print(f"Error: {e}")
        return []
