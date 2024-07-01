'''
This is the main file that is responsible for coordinating the overall workflow of the application.
It invokes all the functions from the other modules. 
'''

from database import setup_database, load_data
from data_processing import select_best_fit_functions, map_test_data
from visualization import plot_data

def main():
    session = setup_database()
    load_data(session)
    best_fits = select_best_fit_functions(session)
    map_test_data(session, best_fits)
    plot_data(session, best_fits)

if __name__ == "__main__":
    main()