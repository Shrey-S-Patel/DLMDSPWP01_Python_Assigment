'''
This module implements the data selection and mapping logic.
'''
import numpy as np
import pandas as pd
from sqlalchemy.orm import Session
from database import TrainingData, IdealFunctions, TestData

def compute_least_squares(y_train, y_ideal):
    return np.sum((y_train - y_ideal) ** 2)

def select_best_fit_functions(session: Session):
    training_data = session.query(TrainingData).all()
    ideal_functions = session.query(IdealFunctions).all()
    
    df_training = pd.DataFrame([(d.x, d.y1, d.y2, d.y3, d.y4) for d in training_data], columns=['x', 'y1', 'y2', 'y3', 'y4'])
    df_ideal = pd.DataFrame([(d.x, d.y1, d.y2, d.y3, d.y4, d.y5, d.y6, d.y7, d.y8, d.y9, d.y10, d.y11, d.y12, d.y13, d.y14, d.y15, d.y16, d.y17, d.y18, d.y19, d.y20, d.y21, d.y22, d.y23, d.y24, d.y25, d.y26, d.y27, d.y28, d.y29, d.y30, d.y31, d.y32, d.y33, d.y34, d.y35, d.y36, d.y37, d.y38, d.y39, d.y40, d.y41, d.y42, d.y43, d.y44, d.y45, d.y46, d.y47, d.y48, d.y49, d.y50) for d in ideal_functions], columns=['x', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13', 'y14', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23', 'y24', 'y25', 'y26', 'y27', 'y28', 'y29', 'y30', 'y31', 'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y40', 'y41', 'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y50'])

    best_fits = {}
    for y_train_col in ['y1', 'y2', 'y3', 'y4']:
        min_error = float('inf')
        best_fit = None
        for y_ideal_col in df_ideal.columns[1:]:
            error = compute_least_squares(df_training[y_train_col], df_ideal[y_ideal_col])
            if error < min_error:
                min_error = error
                best_fit = y_ideal_col
        best_fits[y_train_col] = best_fit
    
    return best_fits

def map_test_data(session: Session, best_fits):
    test_data = session.query(TestData).all()
    ideal_functions = session.query(IdealFunctions).all()
    
    df_ideal = pd.DataFrame([(d.x, d.y1, d.y2, d.y3, d.y4, d.y5, d.y6, d.y7, d.y8, d.y9, d.y10, d.y11, d.y12, d.y13, d.y14, d.y15, d.y16, d.y17, d.y18, d.y19, d.y20, d.y21, d.y22, d.y23, d.y24, d.y25, d.y26, d.y27, d.y28, d.y29, d.y30, d.y31, d.y32, d.y33, d.y34, d.y35, d.y36, d.y37, d.y38, d.y39, d.y40, d.y41, d.y42, d.y43, d.y44, d.y45, d.y46, d.y47, d.y48, d.y49, d.y50) for d in ideal_functions], columns=['x', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13', 'y14', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23', 'y24', 'y25', 'y26', 'y27', 'y28', 'y29', 'y30', 'y31', 'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y40', 'y41', 'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y50'])

    for test_point in test_data:
        x_test = test_point.x
        y_test = test_point.y
        min_deviation = float('inf')
        best_fit = None
        for y_train_col, y_ideal_col in best_fits.items():
            ideal_row = df_ideal[df_ideal['x'] == x_test]
            if not ideal_row.empty:
                y_ideal = ideal_row[y_ideal_col].values[0]
                deviation = abs(y_test - y_ideal)
                if deviation < min_deviation:
                    min_deviation = deviation
                    best_fit = y_ideal_col
        
        if best_fit:
            test_point.delta_y = min_deviation
            test_point.ideal_func_no = int(best_fit[1:])
    
    session.commit()
