""" Модуля для сохранения или записи задачи по проекту """
import os
import lib_nz_tasks
from lib_nz_current_path import current_path


def get_task_info_path_by_id(project_id: str, task_id: str) -> str:
    """
    Возвращает абсолютный путь к файлу
    index.tasks для заданной задачи в проекте

    Args:
        project_id (str): ID проекта
        task_id (str):ID задачи

    Returns:
        str: Путь к файлу вида /path/to/index.tasks

    """
    project_path = os.path.join(
        current_path(), f"project_{project_id}")
    tasks_path = os.path.join(
        project_path, f"task_{task_id}")
    if not os.path.exists(tasks_path):
        os.makedirs(tasks_path)
    return tasks_path


def save_task_info(project_id: str, task_info: dict) -> None:
    """
    Сохраняет информацию о задаче в отдельных файлах

    Параметры:
    project_id (str): Уникальный строковый ID проекта
    task_info (dict): Словарь ключ-значение, где ключи - атрибуты заметки
    (caption, description, priority).
    """
    # Создаем каталог согласно ключа
    task_id = task_info['task_id']
    lib_nz_tasks.add_task_id(project_id, task_id)
    task_info_path = get_task_info_path_by_id(project_id, task_id)
    # print(task_info_path);

    # Сохраним атрибуты в отдельные файлы
    for key, value in task_info.items():
        # получаем полный путь к файлу
        file_path = os.path.join(
            task_info_path, f"{task_id}.{key}")
        # открываем на запись
        with open(file_path, 'w', encoding='utf-8') as file:
            # пишем строковое значение
            file.write(value)


def read_task_info(project_id: str, task_id: str) -> dict[str, str]:
    """
    Считывает информацию из файлов по ID

    Параметры:
    project_id (str): Уникальный ID проектов
    task_id (str): Уникальный ID задачи

    Возвращает:
    dict: Словарь ключ-значение, информация по ключам извлекается из файлов
    """
    task_info = {}
    task_path = get_task_info_path_by_id(project_id, task_id)

    # Проверим, что путь к проекту существует
    if os.path.exists(task_path):
        # Считываем атрибуты по файлам
        for filename in os.listdir(task_path):
            key = filename.split('.')[1]  # Извлечем атрибут
            # получаем имя файла
            file_path = os.path.join(task_path, filename)
            # откроем на считывание
            with open(file_path, 'r', encoding='utf-8') as file:
                # забираем значение атрибута
                # очищаем от строку слева и справа
                task_info[key] = file.read().strip()

    return task_info


def is_attributes_of_task_exists(project_id: str, task_id: str) -> bool:
    """
    Существует ли каталог с проектом
    """
    task_path = get_task_info_path_by_id(project_id, task_id)
    # Проверим, что путь к проекту существует
    return os.path.exists(task_path)


def get_attributes_of_task(project_id: str, task_id: str) -> set[str]:
    """
    Считывает атрибуты по файлам

    Параметры:
    project_id (str): Уникальный ID проектов
    task_id (str): Уникальный ID тасков

    Возвращает:
    set[str]: Список атрибутов
    """
    attrs = []

    task_path = get_task_info_path_by_id(project_id, task_id)

    # Проверим, что путь к проекту существует
    if is_attributes_of_task_exists(project_id, task_id):
        # Считываем атрибуты по файлам
        for filename in os.listdir(task_path):
            key = filename.split('.')[1]  # Извлечем атрибут
            attrs.append(key)

    return set(sorted(attrs))
