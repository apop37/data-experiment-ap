#Python code used to convert .csv to .db

import sqlite3
import pandas as pd

#Step1 load data file to project folder
df = pd.read_csv('dataset.csv')

#Step2 creating a .db file to work with
connection = sqlite3.connect('demo.db')

#Step3 load .csv to .db
df.to_sql('project1', connection)

#Step4 close connection
connection.close()