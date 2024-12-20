""" Модуль для сохранения и чтения информации о задаче проекта """
import os


def save_todo_info(project_id: str, todo_info: dict[str, str]) -> None:
    """
    Сохраняет информацию о задаче в отдельных файлах

    Параметры:
    project_id (str): Уникальный строковый ID проекта
    todo_info (dict): Словарь ключ-значение, где
    ключи - атрибуты заметки (caption, description, priority).
    """
    # Создаем каталог согласно ключа

    project_path = f"project_{project_id}"

    if not os.path.exists(project_path):
        os.makedirs(project_path)

    # Сохраним атрибуты в отдельные файлы
    for key, value in todo_info.items():
        # получаем полный путь к файлу
        file_path = os.path.join(project_path, f"{project_id}.{key}")
        # открываем на запись
        with open(file_path, 'w', encoding='utf-8') as file:
            # пишем строковое значение
            file.write(value)


def read_todo_info(project_id: str) -> dict[str, str]:
    """
    Считывает информацию из файлов по ID

    Параметры:
    project_id (str): Уникальный ID проектов

    Возвращает:
    dict: Словарь ключ-значение, информация по ключам извлекается из файлов
    """
    todo_info = {}

    project_path = f"project_{project_id}"
    # Проверим, что путь к проекту существует
    if os.path.exists(project_path):
        # Считываем атрибуты по файлам
        for filename in os.listdir(project_path):
            # print(filename)
            if not filename.startswith('task_') and filename != 'index.tasks':
                key = filename.split('.')[1]  # Извлечем атрибут
                # получаем имя файла
                file_path = os.path.join(project_path, filename)
                # откроем на считывание
                with open(file_path, 'r', encoding='utf-8') as file:
                    # забираем значение атрибута
                    # очищаем от строку слева и справа
                    todo_info[key] = file.read().strip()

    return todo_info


def is_attributes_exists(project_id: str) -> bool:
    """
    Существует ли каталог с проектом
    """
    project_path = f"project_{project_id}"
    # Проверим, что путь к проекту существует
    return os.path.exists(project_path)


def get_attributes_of_project(project_id: str) -> set[str]:
    """
    Считывает атрибуты по файлам

    Параметры:
    project_id (str): Уникальный ID проектов

    Возвращает:
    set: Множество атрибутов
    """
    attrs = set()

    project_path = f"project_{project_id}"

    # Проверим, что путь к проекту существует
    if is_attributes_exists(project_id):
        # Считываем атрибуты по файлам
        for filename in os.listdir(project_path):
            key = filename.split('.')[1]  # Извлечем атрибут
            attrs |= {key}

    return attrs
