import unittest
import os
from lib_nz_current_path import *
import re
pattern = r'^test_(\w+).py$'

def load_tests_from_directory(directory):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    print(f"using {directory}")
    for filename in os.listdir(directory):
        # Использование re.search для поиска совпадений
        # print(f"Анализ имени файла {filename}")
        match = re.search(pattern, filename)
        if match:
            module_name_test = f"test_{match.group(1)}"
            print(f"Подключим модуль {module_name_test}")
            module = __import__(module_name_test, fromlist=[''])
            suite.addTests(loader.loadTestsFromModule(module))
    
    return suite

if __name__ == "__main__":
    test_suite = load_tests_from_directory( "." )
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
