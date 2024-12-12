import os
import shutil

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

def list_projects() -> None:
    """
    Вывод списка ID проектов

    """
    projects = read_project_ids()
    if len(projects) > 0:
        for project_id in projects:
            print(project_id)
    else:
        print("Проектов не найдено!")

def list_tasks(project_id: str) -> None:
    """
    Вывод списка ID задач для заданного проекта

    """
    tasks = read_task_ids(project_id)
    if len(tasks) > 0:
        for task_id in tasks:
            print(task_id)
    else:
        print("Задач не найдено!")

def input_new_project_info(project_id: str) -> None:
    """
    Ввод нового проекта (внесение в индекс и заполнение данных)

    """
    record = dict()
    for attribute in attributes_of_project():
        value = input(f"Введи значение для атрибута {attribute}: ")
        record[attribute] = value
    save_todo_info(project_id, record)
    add_project_id(project_id)


def input_new_task_info(project_id: str, task_id: str) -> None:
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


def view_existing_project_info(project_id: str) -> None:
    """
    Просмотр информации по проекту

    """
    record = read_todo_info(project_id)
    print(f"Сведения о проекте с ID {project_id}")
    for key in record:
        print(f"{key} : {record[key]}")


def view_existing_task_info(project_id: str, task_id: str) -> None:
    """
    Просмотр информации по задаче

    """
    record = read_task_info(project_id, task_id)
    print(f"Сведения о задаче {task_id} проекта {project_id}")
    for key in record:
        print(f"{key} : {record[key]}")


def edit_existing_project_info(project_id: str) -> None:
    """
    Правка данных о проекте

    """
    record = read_todo_info(project_id)
    for attribute in record.keys():
        print(f"{attribute} : {record[attribute]}")
        keep = input("Храним значение атрибута? [Y/n]:")
        if (keep != "Y"):
            value = input(f"Укажи новое значение для {attribute}: ")
            record[attribute] = value
    save_todo_info(project_id, record)


def edit_existing_task_info(project_id: str, task_id: str) -> None:
    """
    Правка данных о задаче

    """
    record = read_task_info(project_id, task_id)
    for attribute in record.keys():
        if attribute == "task_id":
            continue
        print(f"{attribute} : {record[attribute]}")
        keep = input("Храним значение атрибута? [Y/n]:")
        if (keep != "Y"):
            value = input(f"Укажи новое значение для {attribute}: ")
            record[attribute] = value
    save_task_info(project_id, record)


def delete_project_totally(project_id: str) -> None:
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
        print(f"Данные о проекте удалены вместе с каталогом '{
              project_folder(project_id)}' !")
    else:
        print(f"Каталога {project_folder(project_id)} нет, удалять нечего")


def delete_task_totally(project_id: str, task_id: str) -> None:
    """
    Удаление данных о задаче

    """
    # удаляем ID из индекса
    delete_task_id(project_id, task_id)
    # Проверяем, существует ли папка
    if os.path.exists(task_folder(project_id, task_id)):
        # Удаляем папку и все её содержимое
        shutil.rmtree(task_folder(project_id, task_id))
        print(f"Данные о проекте удалены вместе с каталогом '{
              task_folder(project_id, task_id)}' !")
    else:
        print(f"Каталога {task_folder(
            project_id, task_id)} нет, удалять нечего")


def dialog_help() -> None:
    print(f"Путь к индексному файлу со списком проектов index.projects установлен в {
          index_path()}")
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
    print("+F - фильтр на данные (при совпадении отображать)")
    print("-F - отмена фильтрации")


def main_menu_prompt() -> str:
    """
    Главное меню диалогового режима с перечнем доступных команд

    """
    action = input("выбери действие: ")
    return action

# интерактивный режим
def dialog_mode() -> None:
    """
    Цикл запрос - ответ для диалогового режима

    """
    viewing = "projects"
    last_project_id = ""
    last_task_id = ""
    filter_on = False
    filter_value = ""
    while True:
        clear_terminal()
        about_filter = 'Включен' if filter_on else 'Выключен'
        print(f"Режим просмотра {viewing} Открывали проект {
              last_project_id} задачу {last_task_id}")
        print(f"Фильтр:{about_filter} Отображать, если совпадает с {
              filter_value} ")
        if viewing == "projects":
            print("Список проектов:")
            output_projects_view(filter_on, filter_value)
        elif viewing == "tasks":
            print("Список задач:")
            output_tasks_view(last_project_id, filter_on, filter_value)

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
                output_projects_view(filter_on, filter_value)
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
                output_tasks_view(project_id, filter_on, filter_value)
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
                task_id = input("Какую задачу id редактируем: ")
                edit_existing_task_info(project_id, task_id)
                last_project_id = project_id
                last_task_id = last_task_id
                viewing = "tasks"
            case "mP":
                viewing = "projects"
            case "mT":
                viewing = "tasks"
            case "+F":
                filter_value = input("Введи значение фильтра : ")
                filter_on = True
            case "-F":
                filter_on = False
            case _:
                print("Действие неизвестно!")
        wait_line()



