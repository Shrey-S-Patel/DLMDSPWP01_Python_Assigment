'''
This module is where the unit tests were written for the program to be tested properly.
'''

import unittest
from sqlalchemy.orm import sessionmaker
from database import setup_database, TrainingData, IdealFunctions, TestData
from data_processing import select_best_fit_functions, map_test_data

class TestFunctionMapping(unittest.TestCase):
    def setUp(self):
        self.session = setup_database()

    def test_select_best_fit_functions(self):
        best_fits = select_best_fit_functions(self.session)
        self.assertIsInstance(best_fits, dict)
        self.assertEqual(len(best_fits), 4)

    def test_map_test_data(self):
        best_fits = select_best_fit_functions(self.session)
        map_test_data(self.session, best_fits)
        results = self.session.query(TestData).all()
        self.assertTrue(all(result.ideal_func_no is not None for result in results))

if __name__ == '__main__':
    unittest.main()
