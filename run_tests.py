import unittest
import os
from lib_nz_current_path import *

def load_tests_from_directory(directory):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    print(f"using {directory}")
    for filename in os.listdir(directory):
        if filename.startswith('test_') and filename.endswith('.py'):
            print(f"Подключим файл {filename}")
            module_name = filename[:-3]  # Убираем .py
            module = __import__(f'test_{module_name}', fromlist=[''])
            suite.addTests(loader.loadTestsFromModule(module))
    
    return suite

if __name__ == "__main__":
    test_suite = load_tests_from_directory( "." )
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
