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

# режим командной строки
def commandline_mode() -> None:
    """
    В режиме командной строки используются параметры в виде
    код=значение
    Для полей данных в виде .Поле=Значение
    """
    opcode = get_operation_from_commandline()
    match opcode:
        case "":
            print("Введи код операции! Доступны коды lP|xP|eP|+P|+I|eI|vP|+T|lT|xT|eT")
        case "+P":
            project_id = get_project_id_from_commandline()
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId")
            else:
                add_project_id(project_id)
        case "+I":
            project_id = get_project_id_from_commandline()
            initial_record = fill_empty_record("project")
            save_todo_info(project_id, initial_record)
            record = overwrite_dict(initial_record, get_record_from_commandline(
                project_id, attributes_of_project()))
            print(record)
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId")
            else:
                add_project_id(project_id)
                save_todo_info(project_id, record)
        case "eI":
            # overwrite attrs
            project_id = get_project_id_from_commandline()
            empty_record = fill_empty_record("project")
            old_record = read_todo_info(project_id) if (
                project_id != "" and is_attributes_exists(project_id)) else empty_record
            print(old_record)
            new_record = get_record_from_commandline(
                project_id,  get_attributes_from_commandline())
            print(new_record)
            record = overwrite_dict(old_record, new_record)
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId")
            else:
                add_project_id(project_id)
                save_todo_info(project_id, record)
        case "lP":
            list_projects()
        case "vP":
            project_id = get_project_id_from_commandline()
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId")
            else:
                view_existing_project_info(project_id)
        case "xP":
            project_id = get_project_id_from_commandline()
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId")
            else:
                delete_project_totally(project_id)
        case "+T":
            project_id = get_project_id_from_commandline()
            task_id = get_task_id_from_commandline()
            record = get_record_about_task_from_commandline(
                project_id, task_id, attributes_of_task())
            record["task_id"] = task_id
            save_task_info(project_id, record)
        case "lT":
            project_id = get_project_id_from_commandline()
            list_tasks(project_id)
        case "vT":
            project_id = get_project_id_from_commandline()
            task_id = get_task_id_from_commandline()
            view_existing_task_info(project_id, task_id)
        case "xT":
            project_id = get_project_id_from_commandline()
            task_id = get_task_id_from_commandline()
            delete_task_totally(project_id, task_id)
            list_tasks(project_id)
        case "eT":
            project_id = get_project_id_from_commandline()
            task_id = get_task_id_from_commandline()
            empty_record = fill_empty_record("task")
            old_record = read_task_info(project_id, task_id) if (
                project_id != "" and task_id != "" and is_attributes_of_task_exists(project_id, task_id)) else empty_record
            print(old_record)
            new_record = get_record_about_task_from_commandline(
                project_id, task_id, attributes_of_task())
            print(new_record)
            record = overwrite_dict(old_record, new_record)
            if (project_id == ""):
                print(
                    "Нужен ID проекта project_id=projectId и(или) ID задачи task_id=taskId")
            else:
                add_task_id(project_id, task_id)
                save_task_info(project_id, record)

        case _:
            print(f"Неизвестное действие {opcode}")
