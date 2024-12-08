import sys
import re

def get_mode_from_commandline():
    """
    Получает режим операции

    """
    n = len(sys.argv)
    for i in range(1, n):
        if "mode=" in sys.argv[i]:
            return sys.argv[i].split('=')[1]
    return "dialog"


def get_operation_from_commandline():
    """
    Получает код операции

    """
    n = len(sys.argv)
    for i in range(1, n):
        if "opcode=" in sys.argv[i]:
            return sys.argv[i].split('=')[1]
    return ""

def get_project_id_from_commandline():
    """
    Ищет id проекта в аргументах

    """
    n = len(sys.argv)
    for i in range(1, n):
        if "project_id=" in sys.argv[i]:
            return sys.argv[i].split('=')[1]
    return ""


def get_record_from_commandline(project_id, attributes):
    """
    Составляет словарь по командной строке

    project_id (str): id проекта
    """
    record = dict()
    n = len(sys.argv)
    for attr in attributes:
        record[attr] = "" # начальное значение
        for i in range(1, n):
            if f".{attr}=" in sys.argv[i]:
                record[attr] = sys.argv[i].split('=')[1]
    return record

def get_attributes_from_commandline():
    """
    Составляет множество атрибутов по командной строке

    Параметры должны иметь вид .Поле=Значение
    """
    attrs = set()
    n = len(sys.argv)
   
    # Регулярное выражение для извлечения значений
    pattern = r"\.(\w+)="

    # Список для хранения результатов
    results = []
    data = sys.argv[1:]

    # Проходим по каждой строке в массиве
    for item in data:
        match = re.search(pattern, item)
        if match:
            # Добавляем найденное значение в список результатов
            results.append(match.group(1))
    return results