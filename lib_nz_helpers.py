from lib_nz_config_attributes import *
from lib_nz_current_path import *

import os

def overwriteDict(old_record, new_record):
    """
    Перезаписывает значениями новой записи значения старой
    """
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
    """
    Очистка терминала
    """
    os.system('clear')  # Для Linux и macOS


def fill_empty_record(type_of_record):
    """
    В зависимости от типа (проект или задача) заполняет словарь
    """
    attributes = attributes_of_task()
    if (type_of_record == "project"):
        attributes = attributes_of_project()
    empty_record = dict()
    for attr in attributes:
        empty_record[attr] = ""
    return empty_record

