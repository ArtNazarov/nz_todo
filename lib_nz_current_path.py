""" Модуль для получения абс. путей к используемым каталогам или файлам  """
import os


def get_cur_path() -> str:
    """
    Возвращает путь к данным
    """
    return os.path.dirname(os.path.realpath(__file__))


def current_path() -> str:
    """
    Псевдоним для get_cur_path
    """
    return get_cur_path()


def get_index_path() -> str:
    """
    Возвращает путь к файлу проектов index.projects
    """
    return os.path.join(get_cur_path(), 'index.projects')


def index_path() -> str:
    """
    Путь к индексу проектов
    """
    return os.path.join(current_path(),  "index.projects")


def project_folder(project_id: str) -> str:
    """
    Путь к каталогу определенного проекта
    """
    return os.path.join(current_path(), f"project_{project_id}")


def task_folder(project_id: str, task_id: str) -> str:
    """
    Путь к каталогу определенной задачи
    """
    return os.path.join(project_folder(project_id), f"task_{task_id}")


def get_tasks_index_path(project_id: str) -> str:
    """
    Возвращает путь к файлу index.tasks

    Args:
        project_id (str): ID проекта
    """
    return os.path.join(project_folder(project_id), 'index.tasks')
