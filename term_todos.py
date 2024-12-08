from lib_nz_projects import *
from lib_nz_todo import *
import os
import shutil


def clear_terminal():
    os.system('clear')  # Для Linux и macOS


current_path = os.path.dirname( os.path.realpath(__file__))
index_path = os.path.join(  current_path,  "index.projects")

attributes = ("Название", "Описание", "Приоритет")

def about():
    return "(c) Назаров А.А, Оренбург, 2024-2025\nterm_todos - простой менеджер проектов\n"

def list_projects():
    projects = read_project_ids(index_path)
    if len(projects) > 0:
        for project_id in projects:
            print(project_id)
    else:
        print("Проектов не найдено!")

def input_new_project_info(project_id):
    record = dict()
    for attribute in attributes:
        value = input(f"Введи значение для атрибута {attribute}: ")
        record[attribute] = value
    save_todo_info(project_id, record)
    add_project_id(index_path, project_id)

def view_existing_project_info(project_id):
    record = read_todo_info(project_id)
    print(f"Сведения о проекте с ID {project_id}")
    for key in record:
        print(f"{key} : {record[key]}") 

def edit_existing_project_info(project_id):
    record = read_todo_info(project_id)
    for attribute in record.keys():
        print(f"{attribute} : {record[attribute]}");
        keep = input("Храним значение атрибута? [Y/n]:")
        if (keep != "Y"):
            value = input(f"Укажи новое значение для {attribute}: ")
            record[attribute] = value
    save_todo_info(project_id, record)

def delete_project_totally(project_id):
    # удаляем ID проекта из индекса
    delete_project_id(index_path, project_id)
    # Путь к каталогу с данными
    project_folder = os.path.join(current_path, f"project_{project_id}")  
    # Проверяем, существует ли папка
    if os.path.exists(project_folder):
        # Удаляем папку и все её содержимое
        shutil.rmtree(project_folder)
        print(f"Данные о проекте удалены вместе с каталогом '{project_folder}' !")
    else:
        print(f"Каталога {project_folder} нет, удалять нечего")


def wait_line():
    key = input("Чтобы продолжить диалог - жми enter\n")

def main_menu():
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
    action = input("выбери действие: ")
    return action


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
        case _:
            print("Действие неизвестно!")
    wait_line()


