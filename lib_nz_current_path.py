import os

def get_cur_path():
    """
    Возвращает путь к данным
    """
    return os.path.dirname( os.path.realpath(__file__))

def current_path():
    """
    Псевдоним для get_cur_path
    """
    return get_cur_path()

def index_path():
    """
    Путь к индексу проектовв
    """
    return os.path.join(  current_path(),  "index.projects")

def project_folder(project_id):
    """
    Путь к каталогу определенного проекта
    """
    return os.path.join(current_path(), f"project_{project_id}")  

def task_folder(project_id, task_id):
    """
    Путь к каталогу определенной задачи
    """
    return os.path.join(project_folder(project_id), f"task_{task_id}")