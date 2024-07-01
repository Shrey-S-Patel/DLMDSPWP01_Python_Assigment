'''
This is used to create the visualizations of our data and functions.
'''

import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file
from sqlalchemy.orm import Session
from database import TrainingData, IdealFunctions, TestData

def plot_data(session: Session, best_fits):
    training_data = session.query(TrainingData).all()
    ideal_functions = session.query(IdealFunctions).all()
    test_data = session.query(TestData).all()
    
    df_training = pd.DataFrame([(d.x, d.y1, d.y2, d.y3, d.y4) for d in training_data], columns=['x', 'y1', 'y2', 'y3', 'y4'])
    df_ideal = pd.DataFrame([(d.x, d.y1, d.y2, d.y3, d.y4, d.y5, d.y6, d.y7, d.y8, d.y9, d.y10, d.y11, d.y12, d.y13, d.y14, d.y15, d.y16, d.y17, d.y18, d.y19, d.y20, d.y21, d.y22, d.y23, d.y24, d.y25, d.y26, d.y27, d.y28, d.y29, d.y30, d.y31, d.y32, d.y33, d.y34, d.y35, d.y36, d.y37, d.y38, d.y39, d.y40, d.y41, d.y42, d.y43, d.y44, d.y45, d.y46, d.y47, d.y48, d.y49, d.y50) for d in ideal_functions], columns=['x', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13', 'y14', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23', 'y24', 'y25', 'y26', 'y27', 'y28', 'y29', 'y30', 'y31', 'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y40', 'y41', 'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y50'])
    df_test = pd.DataFrame([(d.x, d.y, d.delta_y, d.ideal_func_no) for d in test_data], columns=['x', 'y', 'delta_y', 'ideal_func_no'])

    output_file("plot.html")
    p = figure(title="Training, Ideal, and Test Data", x_axis_label='x', y_axis_label='y')

    # Plot training data
    for y_col in ['y1', 'y2', 'y3', 'y4']:
        p.line(df_training['x'], df_training[y_col], legend_label=f'Training {y_col}', line_width=2)

    # Plot ideal functions
    for y_col in df_ideal.columns[1:]:
        p.line(df_ideal['x'], df_ideal[y_col], legend_label=f'Ideal {y_col}', line_width=1, line_dash='dashed')

    # Plot test data
    p.circle(df_test['x'], df_test['y'], size=10, color='red', legend_label='Test Data')

    show(p)
