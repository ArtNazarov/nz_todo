from lib_nz_projects import *
from lib_nz_project_info import *
from lib_nz_commandline import *
from lib_nz_task_info import *
from lib_nz_tasks import *
from lib_nz_current_path import *
from lib_nz_stdin_parse import *
import os
import shutil

def overwriteDict(old_record, new_record):
    use_keys = set()
    for key in old_record.keys():
        use_keys |= { key }
    for key in new_record.keys():
        use_keys |= { key }
    record = dict()
    for key in use_keys:
        if key in new_record.keys():
            record[key] = new_record[key]
        else:
            record[key] = old_record[key]
    return record

def clear_terminal():
    os.system('clear')  # Для Linux и macOS


current_path = get_cur_path()
index_path = os.path.join(  current_path,  "index.projects")

attributes_of_project = ("НазваниеПроекта", "ОписаниеПроекта", "СтатусПроекта")
attributes_of_task = ("НазваниеЗадачи", "ОписаниеЗадачи", "ПриоритетЗадачи")


def fill_empty_record(type_of_record):
    attributes = attributes_of_task
    if (type_of_record == "project"):
        attributes = attributes_of_project
    empty_record = dict()
    for attr in attributes:
        empty_record[attr] = ""
    return empty_record

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
    for attribute in attributes_of_project:
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
    for attribute in attributes_of_task:
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
    project_folder = os.path.join(current_path, f"project_{project_id}")  
    # Проверяем, существует ли папка
    if os.path.exists(project_folder):
        # Удаляем папку и все её содержимое
        shutil.rmtree(project_folder)
        print(f"Данные о проекте удалены вместе с каталогом '{project_folder}' !")
    else:
        print(f"Каталога {project_folder} нет, удалять нечего")


def delete_task_totally(project_id, task_id):
    """
    Удаление данных о задаче

    """
    # удаляем ID из индекса
    delete_task_id(project_id, task_id)
    # Путь к каталогу с данными
    # print(f"Текущий путь: {get_cur_path()}")
    project_folder = os.path.join(get_cur_path(), f"project_{project_id}")
    # print(f"Путь к каталогу проекта: {project_folder}")
    task_folder = os.path.join(project_folder, f"task_{task_id}")
    # print(f"Удаление данных из {task_folder}")  
    # Проверяем, существует ли папка
    if os.path.exists(task_folder):
        # Удаляем папку и все её содержимое
        shutil.rmtree(task_folder)
        print(f"Данные о проекте удалены вместе с каталогом '{task_folder}' !")
    else:
        print(f"Каталога {task_folder} нет, удалять нечего")


def wait_line():
    """
    Пауза перед продолжением диалога

    """
    key = input("Чтобы продолжить диалог - жми enter\n")

def main_menu():
    """
    Главное меню диалогового режима с перечнем доступных команд

    """
    clear_terminal()
    print(f"Путь к индексному файлу со списком проектов index.projects установлен в {index_path}")
    print("Выбери действие...")
    print("q для выхода")
    print("h для сведений о программе")
    print("lP для списка проектов")
    print("+P для добавления проекта в список")
    print("vP чтобы посмотреть проект")
    print("eP чтобы отредактировать проект")
    print("xP чтобы удалить проект")
    print("+T чтобы добавить задачу в проект")
    print("lT чтобы посмотреть список задач в проекте")
    print("vT чтобы посмотреть параметры задачи проекта")
    print("xT чтобы удалить задачу из проекта")
    print("eT чтобы отредактировать задачу в проекте")
    action = input("выбери действие: ")
    return action


# интерактивный режим
def dialog_mode():
    """
    Цикл запрос - ответ для диалогового режима

    """
    while True:
        clear_terminal()
        match main_menu().strip():
            case "q":
                break
            case "h":
                print(about())    
            case "lP":
                list_projects()
            case "+P":
                project_id = input("Id для нового проекта:")
                input_new_project_info(project_id)
                list_projects()
            case "vP":
                project_id = input("Укажи какой id посмотреть:")
                view_existing_project_info(project_id)
            case "eP":
                list_projects()
                project_id = input("Укажи какой id отредактировать:")
                edit_existing_project_info(project_id)
            case "xP":
                project_id = input("Укажи какой id удаляем: ")
                confirm_id = input("Вы уверены? Введите еще раз имя проекта: ")
                if (confirm_id == project_id):
                    delete_project_totally(project_id)
                    list_projects
                else:
                    print("Ничего не удалялось")
            case "+T":
                project_id = input("В какой проект добавлять:")
                task_id = input("Придумайте ID для задачи:")
                input_new_task_info(project_id, task_id)
            case "lT":
                project_id = input("Какой проект смотрим? : ")
                list_tasks(project_id)
            case "vT":
                project_id = input("ID проекта: ")
                task_id = input("ID задачи: ")
                view_existing_task_info(project_id, task_id)
            case "xT":
                project_id = input("ID проекта: ")
                task_id = input("ID задачи: ")
                delete_task_totally(project_id, task_id)
                list_tasks(project_id)
            case "eT":
                project_id = input("Укажи какой проект id отредактировать: ")
                list_tasks(project_id)
                task_id=input("Какую задачу id редактируем: ")
                edit_existing_task_info(project_id, task_id)
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
    match get_operation_from_commandline():
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
            record = overwriteDict(initial_record, get_record_from_commandline(project_id, attributes_of_project))
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
            record =  get_record_about_task_from_commandline(project_id, task_id, attributes_of_task)
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
            new_record = get_record_about_task_from_commandline(project_id, task_id, attributes_of_task)
            print(new_record)
            record = overwriteDict(old_record, new_record)
            if (project_id == ""):
                print("Нужен ID проекта project_id=projectId и(или) ID задачи task_id=taskId")
            else:
                add_task_id(project_id, task_id)
                save_task_info(project_id, record)
        
        case _:
            print("Unknown action")


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
                for attr in attributes_of_project:
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
                for attr in attributes_of_project:
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
                project_id = statement["project_id"]
                task_id = statement["task_id"]
                empty_record = fill_empty_record("task")
                given_record = dict()
                for attr in attributes_of_task:
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
                for attr in attributes_of_project:
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
                print("Unknown action")


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