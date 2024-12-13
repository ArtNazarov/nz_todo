""" Модуль для считывания модели и извлечения из нее таблиц """
from lib_nz_project_info import *
from lib_nz_task_info import *
from lib_nz_projects import *
from lib_nz_tasks import *

# ################ model ###################


def load_full_model() -> dict:
    """ Загружает модель в память (проекты и задачи к ним) """
    model = dict()
    project_ids = read_project_ids()
    for project_id in project_ids:
        project_info = read_todo_info(project_id)
        model[project_id] = dict()
        model[project_id]['project_info'] = project_info
        model[project_id]['task_list'] = []
        tasks = read_task_ids(project_id)
        for task_id in tasks:
            task = read_task_info(project_id, task_id)
            model[project_id]["task_list"].append(task)
    return model


def extract_table_projects_from_model(model: dict, attrs_sequence: tuple[str, ...] | list[str]) -> list[list[str]]:
    """ Извлекает из модели таблицу проектов """
    table = []
    for project_id in model:
        props = []
        props.append(project_id)
        for attr in attrs_sequence:
            props.append(model[project_id]['project_info'].get(attr, '???'))
        table.append(props)
    return table


def extract_table_tasks_from_model(model: dict, project_id: str, attrs_sequence: tuple[str, ...] | list[str]) -> list[list[str]]:
    """ Извлекает из модели таблицу задач по проекту """
    table = []
    for task in model[project_id]['task_list']:
        props = [task['task_id']]
        for attr in attrs_sequence:
            props.append(task[attr])
        table.append(props)
    return table


def filter_view(table: list[list[str]], filter_on: bool, filter_value: str) -> list[list[str]]:
    """
    Фильтрует таблицу по совпадению с фильтром
    """
    if filter_on is False:
        return table
    if filter_value == "":
        return table
    filtered = []
    for row in table:
        flag_get_row = False
        for cell in row:
            if filter_value in cell:
                flag_get_row = True
        if flag_get_row:
            filtered.append(row)
    return filtered
