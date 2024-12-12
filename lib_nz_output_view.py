from prettytable import PrettyTable
from lib_nz_model import *
from lib_nz_config_attributes import *

# ################# view #################

def output_projects_view(filter_on: bool, filter_value: str) -> None:
    """
    Вывод таблицы проектов
    """
    model = load_full_model()  # загружаем модель
    projects = extract_table_projects_from_model(
        model, attributes_of_project())  # извлекаем проекты
    mytable = PrettyTable()  # объект для отображения табллицы
    mytable.field_names = ['project_id'] + \
        list(attributes_of_project())  # используемые атрибуты
    filtered_view = filter_view(projects, filter_on, filter_value)
    mytable.add_rows(filtered_view)  # добавление списка строк
    print(mytable)  # вывод


def output_tasks_view(project_id: str, filter_on: bool, filter_value: str):
    """
    Вывод таблицы задачи
    """
    model = load_full_model()  # загружаем модель
    tasks = extract_table_tasks_from_model(
        model, project_id,  attributes_of_task())  # извлекаем проекты
    mytable = PrettyTable()  # объект для отображения табллицы
    mytable.field_names = ['task_id'] + \
        list(attributes_of_task())  # используемые атрибуты
    filtered_view = filter_view(tasks, filter_on, filter_value)
    mytable.add_rows(filtered_view)  # добавление списка строк
    print(mytable)  # вывод
