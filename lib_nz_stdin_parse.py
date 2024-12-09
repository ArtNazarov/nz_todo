import sys

def get_operations_list():
    """
    Возвращает список операций, операции задаются словарями
    
    """
    operations = []
    # Читаем данные из stdin
    input_data = sys.stdin.read().strip()
    
    # разбиваем на операторы
    statements = input_data.split('#')

    for statement in statements:
        # Разбиваем строку на пары ключ=значение
        pairs = statement.split(";")
        operation = dict()

        for pair in pairs:
            list = pair.split('=')
            operation[list[0].strip()] = list[1].replace('"', '').strip()
        operations.append(operation)

    return operations

