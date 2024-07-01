'''
This module is used to initialize the database and load the data.
'''

from sqlalchemy import create_engine, Column, Integer, Float, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()

# Define the training data table


class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

# Define the ideal functions table


class IdealFunctions(Base):
    __tablename__ = 'ideal_functions'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)
    y5 = Column(Float)
    y6 = Column(Float)
    y7 = Column(Float)
    y8 = Column(Float)
    y9 = Column(Float)
    y10 = Column(Float)
    y11 = Column(Float)
    y12 = Column(Float)
    y13 = Column(Float)
    y14 = Column(Float)
    y15 = Column(Float)
    y16 = Column(Float)
    y17 = Column(Float)
    y18 = Column(Float)
    y19 = Column(Float)
    y20 = Column(Float)
    y21 = Column(Float)
    y22 = Column(Float)
    y23 = Column(Float)
    y24 = Column(Float)
    y25 = Column(Float)
    y26 = Column(Float)
    y27 = Column(Float)
    y28 = Column(Float)
    y29 = Column(Float)
    y30 = Column(Float)
    y31 = Column(Float)
    y32 = Column(Float)
    y33 = Column(Float)
    y34 = Column(Float)
    y35 = Column(Float)
    y36 = Column(Float)
    y37 = Column(Float)
    y38 = Column(Float)
    y39 = Column(Float)
    y40 = Column(Float)
    y41 = Column(Float)
    y42 = Column(Float)
    y43 = Column(Float)
    y44 = Column(Float)
    y45 = Column(Float)
    y46 = Column(Float)
    y47 = Column(Float)
    y48 = Column(Float)
    y49 = Column(Float)
    y50 = Column(Float)


# Define the test data table
class TestData(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    delta_y = Column(Float)
    ideal_func_no = Column(Integer)


def setup_database():
    engine = create_engine('sqlite:///functions.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()

# Loading the data from SQL Lite to a Pandas dataframe.


def load_data(session):
    training_data = pd.read_csv('train.csv')
    for index, row in training_data.iterrows():
        training_row = TrainingData(
            x=row['X'], y1=row['Y1'], y2=row['Y2'], y3=row['Y3'], y4=row['Y4'])
        session.add(training_row)

    ideal_functions = pd.read_csv('ideal.csv')
    for index, row in ideal_functions.iterrows():
        ideal_row = IdealFunctions(x=row['X'], y1=row['Y1'], y2=row['Y2'], y3=row['Y3'], y4=row['Y4'], y5=row['Y5'], y6=row['Y6'], y7=row['Y7'], y8=row['Y8'], y9=row['Y9'], y10=row['Y10'], y11=row['Y11'], y12=row['Y12'], y13=row['Y13'], y14=row['Y14'], y15=row['Y15'], y16=row['Y16'], y17=row['Y17'], y18=row['Y18'], y19=row['Y19'], y20=row['Y20'], y21=row['Y21'], y22=row['Y22'], y23=row['Y23'], y24=row['Y24'], y25=row['Y25'], y26=row['Y26'], y27=row['Y27'], y28=row['Y28'], y29=row['Y29'], y30=row['Y30'], y31=row['Y31'], y32=row['Y32'], y33=row['Y33'], y34=row['Y34'], y35=row['Y35'], y36=row['Y36'], y37=row['Y37'], y38=row['Y38'], y39=row['Y39'], y40=row['Y40'], y41=row['Y41'], y42=row['Y42'], y43=row['Y43'], y44=row['Y44'], y45=row['Y45'], y46=row['Y46'], y47=row['Y47'], y48=row['Y48'], y49=row['Y49'], y50=row['Y50'],)
        session.add(ideal_row)

    test_data = pd.read_csv('test.csv')
    for index, row in test_data.iterrows():
        test_row = TestData(x=row['X'], y=row['Y'])
        session.add(test_row)

    session.commit()
