import sys

def get_operations_list_inner(input_data):
    """
    Возвращает список операций, операции задаются словарями
    
    """
    operations = []
    # Читаем данные из stdin
 
    # разбиваем на операторы
    statements = input_data.split('#')

    for statement in statements:
        # Разбиваем строку на пары ключ=значение
        pairs = statement.split(";")
        operation = dict()

        for pair in pairs:
            list = pair.split('=')
            key = list[0].strip()
            value = list[1].replace('"', '').strip()
            if key[0] == ".":
                key = key[1:]
            operation[key] = value 
        operations.append(operation)

    return operations

def get_operations_list():
    input_data = sys.stdin.read().strip()
    return get_operations_list_inner(input_data)
