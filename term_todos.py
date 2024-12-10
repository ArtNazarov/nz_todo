from lib_nz_helpers import *
from lib_nz_config_attributes import *
from lib_nz_projects import *
from lib_nz_project_info import *
from lib_nz_commandline import *
from lib_nz_task_info import *
from lib_nz_tasks import *
from lib_nz_current_path import *
from lib_nz_stdin_parse import *
from prettytable import PrettyTable
import os
import shutil

# ################ model ###################

def load_full_model():
    model = dict()
    project_ids = read_project_ids()
    for project_id in project_ids:
        project_info = read_todo_info(project_id)
        model[project_id] = dict()
        model[project_id]['project_info'] = project_info
        model[project_id]['task_list'] = [];
        tasks = read_task_ids(project_id)
        for task_id in tasks:
            task = read_task_info(project_id, task_id)
            model[project_id]["task_list"].append(task)
    return model



def extract_table_projects_from_model(model, attrs_sequence):
    table = []
    for project_id in model:
        props = []
        for attr in attrs_sequence:
            props.append(model[project_id]['project_info'][attr])
        table.append(props)
    return table


def extract_table_tasks_from_model(model, project_id, attrs_sequence):
    table = []
    for task in model[project_id]['task_list']:
        props = []
        for attr in attrs_sequence:
            props.append(task[attr])
        table.append(props)
    return table



# ################# view #################

def output_projects_view():
    """
    Вывод таблицы проектов
    """
    model = load_full_model() # загружаем модель
    projects = extract_table_projects_from_model(model, attributes_of_project()) # извлекаем проекты
    mytable = PrettyTable() # объект для отображения табллицы
    mytable.field_names = attributes_of_project() # используемые атрибуты
    mytable.add_rows(projects) # добавление списка строк
    print(mytable) # вывод

def output_tasks_view(project_id):
    """
    Вывод таблицы задачи
    """
    model = load_full_model() # загружаем модель
    tasks = extract_table_tasks_from_model(model, project_id, attributes_of_task()) # извлекаем проекты
    mytable = PrettyTable() # объект для отображения табллицы
    mytable.field_names = attributes_of_task() # используемые атрибуты
    mytable.add_rows(tasks) # добавление списка строк
    print(mytable) # вывод


def about():
    return "(c) Назаров А.А, Оренбург, 2024-2025\nterm_todos - простой менеджер проектов\n"

def list_projects():
    """
    Вывод списка ID проектов

    """
    projects = read_project_ids()
    if len(projects) > 0:
        for project_id in projects:
            print(project_id)
    else:
        print("Проектов не найдено!")

def list_tasks(project_id):
    """
    Вывод списка ID задач для заданного проекта

    """
    tasks = read_task_ids(project_id)
    if len(tasks) > 0:
        for task_id in tasks:
            print(task_id)
    else:
        print("Задач не найдено!")


def input_new_project_info(project_id):
    """
    Ввод нового проекта (внесение в индекс и заполнение данных)

    """
    record = dict()
    for attribute in attributes_of_project():
        value = input(f"Введи значение для атрибута {attribute}: ")
        record[attribute] = value
    save_todo_info(project_id, record)
    add_project_id(project_id)


def input_new_task_info(project_id, task_id):
    """
    Ввод новых данных по задаче

    """
    record = dict()
    record['task_id'] = task_id
    for attribute in attributes_of_task():
        value = input(f"Введи значение для атрибута {attribute}: ")
        record[attribute] = value
    save_task_info(project_id, record)
    add_task_id(project_id, task_id)


def view_existing_project_info(project_id):
    """
    Просмотр информации по проекту
    
    """
    record = read_todo_info(project_id)
    print(f"Сведения о проекте с ID {project_id}")
    for key in record:
        print(f"{key} : {record[key]}") 

def view_existing_task_info(project_id, task_id):
    """
    Просмотр информации по задаче

    """
    record = read_task_info(project_id, task_id)
    print(f"Сведения о задаче {task_id} проекта {project_id}")
    for key in record:
        print(f"{key} : {record[key]}") 

def edit_existing_project_info(project_id):
    """
    Правка данных о проекте
    
    """
    record = read_todo_info(project_id)
    for attribute in record.keys():
        print(f"{attribute} : {record[attribute]}");
        keep = input("Храним значение атрибута? [Y/n]:")
        if (keep != "Y"):
            value = input(f"Укажи новое значение для {attribute}: ")
            record[attribute] = value
    save_todo_info(project_id, record)

def edit_existing_task_info(project_id, task_id):
    """
    Правка данных о задаче
    
    """
    record = read_task_info(project_id, task_id)
    for attribute in record.keys():
        if attribute == "task_id":
            continue
        print(f"{attribute} : {record[attribute]}");
        keep = input("Храним значение атрибута? [Y/n]:")
        if (keep != "Y"):
            value = input(f"Укажи новое значение для {attribute}: ")
            record[attribute] = value
    save_task_info(project_id, record)

def delete_project_totally(project_id):
    """
    Удаление данных о проекте

    """
    # удаляем ID проекта из индекса
    delete_project_id(project_id)
    # Путь к каталогу с данными
    # Проверяем, существует ли папка
    if os.path.exists(project_folder(project_id)):
        # Удаляем папку и все её содержимое
        shutil.rmtree(project_folder(project_id))
        print(f"Данные о проекте удалены вместе с каталогом '{project_folder(project_id)}' !")
    else:
        print(f"Каталога {project_folder(project_id)} нет, удалять нечего")


def delete_task_totally(project_id, task_id):
    """
    Удаление данных о задаче

    """
    # удаляем ID из индекса
    delete_task_id(project_id, task_id)
     # Проверяем, существует ли папка
    if os.path.exists(task_folder(project_id, task_id)):
        # Удаляем папку и все её содержимое
        shutil.rmtree(task_folder(project_id, task_id))
        print(f"Данные о проекте удалены вместе с каталогом '{task_folder(project_id, task_id)}' !")
    else:
        print(f"Каталога {task_folder(project_id, task_id)} нет, удалять нечего")


def wait_line():
    """
    Пауза перед продолжением диалога

    """
    key = input("Чтобы продолжить диалог - жми enter\n")


def dialog_help():
    print(f"Путь к индексному файлу со списком проектов index.projects установлен в {index_path()}")
    print("Выбери действие...")
    print("q для выхода")
    print("h для сведений о программе")
    print("lP для списка проектов")
    print("LP для списка проектов в табличной форме")
    print("+P для добавления проекта в список")
    print("vP чтобы посмотреть проект")
    print("eP чтобы отредактировать проект")
    print("xP чтобы удалить проект")
    print("+T чтобы добавить задачу в проект")
    print("lT чтобы посмотреть список задач в проекте")
    print("LT для списка задача к проекту в табличной форме")
    print("vT чтобы посмотреть параметры задачи проекта")
    print("xT чтобы удалить задачу из проекта")
    print("eT чтобы отредактировать задачу в проекте")
    print("mP - режим просмотра проектов")
    print("mT - режим просмотра задач")

def main_menu_prompt():
    """
    Главное меню диалогового режима с перечнем доступных команд

    """
    action = input("выбери действие: ")
    return action


# интерактивный режим
def dialog_mode():
    """
    Цикл запрос - ответ для диалогового режима

    """
    viewing = "projects"
    last_project_id = ""
    last_task_id = ""
    while True:
        clear_terminal()
        print(f"Режим просмотра {viewing} Открывали проект {last_project_id} задачу {last_task_id}")
        if viewing == "projects":
            print("Список проектов:")
            output_projects_view()
        elif viewing == "tasks":
            print("Список задач:")
            output_tasks_view(last_project_id)
        
        match main_menu_prompt().strip():
            case "q":
                break
            case "h":
                print(about())
                dialog_help()    
            case "lP":
                list_projects()
                viewing = "projects"
            case "LP":
                output_projects_view()
                viewing = "projects"
            case "+P":
                project_id = input("Id для нового проекта:")
                input_new_project_info(project_id)
                list_projects()
                last_project_id = project_id
                viewing = "projects"
            case "vP":
                project_id = input("Укажи какой id посмотреть:")
                view_existing_project_info(project_id)
                last_project_id = project_id
                viewing = "projects"
            case "eP":
                list_projects()
                project_id = input("Укажи какой id отредактировать:")
                edit_existing_project_info(project_id)
                last_project_id = project_id
                viewing = "projects"
            case "xP":
                project_id = input("Укажи какой id удаляем: ")
                confirm_id = input("Вы уверены? Введите еще раз имя проекта: ")
                if (confirm_id == project_id):
                    delete_project_totally(project_id)
                    list_projects
                else:
                    print("Ничего не удалялось")
                last_project_id = ""
                viewing = "projects"
            case "+T":
                project_id = input("В какой проект добавлять:")
                task_id = input("Придумайте ID для задачи:")
                input_new_task_info(project_id, task_id)
                last_project_id = project_id
                last_task_id = task_id
                viewing = "tasks"
            case "lT":
                project_id = input("Какой проект смотрим? : ")
                list_tasks(project_id)
                last_project_id = project_id
                last_task_id = ""
                viewing = "tasks"
            case "LT":
                project_id = input("Какой проект смотрим? : ")
                output_tasks_view(project_id)
                last_project_id = project_id
                last_task_id = ""
                viewing = "tasks"
            case "vT":
                project_id = input("ID проекта: ")
                task_id = input("ID задачи: ")
                view_existing_task_info(project_id, task_id)
                last_project_id = project_id
                last_task_id = task_id
                viewing = "tasks"
            case "xT":
                project_id = input("ID проекта: ")
                task_id = input("ID задачи: ")
                delete_task_totally(project_id, task_id)
                list_tasks(project_id)
                last_project_id = ""
                last_task_id = ""
                viewing = "tasks"
            case "eT":
                project_id = input("Укажи какой проект id отредактировать: ")
                list_tasks(project_id)
                task_id=input("Какую задачу id редактируем: ")
                edit_existing_task_info(project_id, task_id)
                last_project_id = project_id
                last_task_id = last_task_id
                viewing = "tasks"
            case "mP":
                viewing = "projects"
            case "mT":
                viewing = "tasks"
            case _:
                print("Действие неизвестно!")
        wait_line()


# режим командной строки
def commandline_mode():
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
            record = overwriteDict(initial_record, get_record_from_commandline(project_id, attributes_of_project()))
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
            old_record =  read_todo_info(project_id) if (project_id != "" and is_attributes_exists(project_id)) else empty_record
            print(old_record)
            new_record = get_record_from_commandline(project_id,  get_attributes_from_commandline())
            print(new_record)
            record = overwriteDict(old_record, new_record)
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
            record =  get_record_about_task_from_commandline(project_id, task_id, attributes_of_task())
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
            old_record =  read_task_info(project_id, task_id) if (project_id != "" and task_id != "" and is_attributes_of_task_exists(project_id, task_id)) else empty_record
            print(old_record)
            new_record = get_record_about_task_from_commandline(project_id, task_id, attributes_of_task())
            print(new_record)
            record = overwriteDict(old_record, new_record)
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId и(или) ID задачи task_id=taskId")
            else:
                add_task_id(project_id, task_id)
                save_task_info(project_id, record)
        
        case _:
            print(f"Неизвестное действие {opcode}")


def pipe_mode():
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
                print("Введи код операции! Доступны коды lP|xP|eP|+P|+I|eI|vP|+T|lT|xT|eT")
            case "+P":
                project_id = statement["project_id"]
                if (project_id == ""):
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
                if (project_id == ""):
                    print("Нужен ID проекта project_id=projectId")
                else:
                    add_project_id(project_id)
                    save_todo_info(project_id, record)
            case "eI": 
                # overwrite attrs
                project_id = statement["project_id"]
                empty_record = fill_empty_record("project")
                old_record =  read_todo_info(project_id) if (project_id != "" and is_attributes_exists(project_id)) else empty_record
                print(old_record)
                given_record = dict()
                for attr in attributes_of_project():
                    given_record[attr] = statement[attr]
                print(given_record)
                record = overwriteDict(old_record, given_record)
                if (project_id == ""):
                    print("Нужен ID проекта project_id=projectId")
                else:
                    add_project_id(project_id)
                    save_todo_info(project_id, record)
            case "lP":
                list_projects()
            case "vP":
                project_id = statement["project_id"]
                if (project_id == ""):
                    print("Нужен ID проекта project_id=projectId")
                else:
                    view_existing_project_info(project_id)
            case "xP":
                project_id = statement["project_id"]
                if (project_id == ""):
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
                record =  overwriteDict(empty_record, given_record)
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
                old_record =  read_task_info(project_id, task_id) if (project_id != "" and task_id != "" and is_attributes_of_task_exists(project_id, task_id)) else empty_record
                print(old_record)
                print(given_record)
                record = overwriteDict(old_record, given_record)
                if (project_id == ""):
                    print("Нужен ID проекта project_id=projectId и(или) ID задачи task_id=taskId")
                else:
                    add_task_id(project_id, task_id)
                    save_task_info(project_id, record)
            
            case _:
                print(f"Unknown action {opcode}")


# получаем режим программы
mode = get_mode_from_commandline()
if (mode == "pipe"): # в режиме конвеера
    pipe_mode()
elif (mode == "dialog"): # если в диалоговом
    dialog_mode()
elif (mode == "commandline"): # если в командном
    commandline_mode()
else: # неизвестный режим
    print("Unknown mode! Use mode=dialog or mode=commandline")