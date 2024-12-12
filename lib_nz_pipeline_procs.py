""" Модуль с функциями для режима конвеера """
from lib_nz_projects import *
from lib_nz_tasks import *
from lib_nz_helpers import *
from lib_nz_interactive import *
from lib_nz_config_attributes import *
from lib_nz_project_info import *
from lib_nz_commandline import *
from lib_nz_task_info import *
from lib_nz_current_path import *
from lib_nz_stdin_parse import *
from lib_nz_model import *
from lib_nz_output_view import *
from lib_nz_dialog_procs import *


def pipe_mode() -> None:
    # режим конвеера
    """
    В режиме конвеера входные данных берутся из потока ввода
    в виде последовательности операторов
    Операторы разделяются знаком #
    Оператор это последовательность параметров вида Параметр=Значение;
    Для полей данных в виде .Поле=Значение
    Пары Параметр-Значение отделяются друг от друга знаком ;
    """
    statements = get_operations_list()
    for statement in statements:
        opcode = statement["opcode"]
        match opcode:
            case "":
                print(
                    "Введи код операции! Доступны коды lP|xP|eP|+P|+I|eI|vP|+T|lT|xT|eT")
            case "+P":
                project_id = statement["project_id"]
                if project_id == "":
                    print("Нужен ID проекта project_id=projectId")
                else:
                    add_project_id(project_id)
            case "+I":
                project_id = statement["project_id"]
                initial_record = fill_empty_record("project")
                save_todo_info(project_id, initial_record)
                given_record = dict()
                for attr in attributes_of_project():
                    given_record[attr] = statement[attr]
                record = overwriteDict(initial_record, given_record)
                print(record)
                if project_id == "":
                    print("Нужен ID проекта project_id=projectId")
                else:
                    add_project_id(project_id)
                    save_todo_info(project_id, record)
            case "eI":
                # overwrite attrs
                project_id = statement["project_id"]
                empty_record = fill_empty_record("project")
                old_record = read_todo_info(project_id) if (
                    project_id != "" and is_attributes_exists(project_id)) else empty_record
                print(old_record)
                given_record = dict()
                for attr in attributes_of_project():
                    given_record[attr] = statement[attr]
                print(given_record)
                record = overwriteDict(old_record, given_record)
                if project_id == "":
                    print("Нужен ID проекта project_id=projectId")
                else:
                    add_project_id(project_id)
                    save_todo_info(project_id, record)
            case "lP":
                list_projects()
            case "vP":
                project_id = statement["project_id"]
                if project_id == "":
                    print("Нужен ID проекта project_id=projectId")
                else:
                    view_existing_project_info(project_id)
            case "xP":
                project_id = statement["project_id"]
                if project_id == "":
                    print("Нужен ID проекта project_id=projectId")
                else:
                    delete_project_totally(project_id)
            case "+T":
                print(statement)
                project_id = statement["project_id"]
                task_id = statement["task_id"]
                empty_record = fill_empty_record("task")
                given_record = dict()
                for attr in attributes_of_task():
                    if attr in statement.keys():
                        given_record[attr] = statement[attr]
                record = overwriteDict(empty_record, given_record)
                record["task_id"] = task_id
                save_task_info(project_id, record)
            case "lT":
                project_id = statement["project_id"]
                list_tasks(project_id)
            case "vT":
                project_id = statement["project_id"]
                task_id = statement["task_id"]
                view_existing_task_info(project_id, task_id)
            case "xT":
                project_id = statement["project_id"]
                task_id = statement["task_id"]
                delete_task_totally(project_id, task_id)
                list_tasks(project_id)
            case "eT":
                project_id = statement["project_id"]
                task_id = statement["task_id"]
                empty_record = fill_empty_record("task")
                given_record = dict()
                for attr in attributes_of_task():
                    if attr in statement.keys():
                        given_record[attr] = statement[attr]
                old_record = read_task_info(project_id, task_id) if (
                    project_id != "" and task_id != "" and is_attributes_of_task_exists(project_id, task_id)) else empty_record
                print(old_record)
                print(given_record)
                record = overwriteDict(old_record, given_record)
                if project_id == "":
                    print(
                        "Нужен ID проекта project_id=projectId и(или) ID задачи task_id=taskId")
                else:
                    add_task_id(project_id, task_id)
                    save_task_info(project_id, record)

            case _:
                print(f"Unknown action {opcode}")
