import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series , DataFrame


df = pd.read_csv('gymnasium-names2.csv')


#pd.concat([Series(row['gymnasium'], row['fach'].split(','))              
#            for _, row in df.iterrows()]).reset_index()



b = DataFrame(df.fach.str.split(', ').tolist(), index=df.gymnasium).stack()
b = b.reset_index()[[0, 'gymnasium']] # var1 variable is currently labeled 0
b.columns = ['fach', 'gymnasium'] # renaming var1

b.to_csv('dim_fach.csv', index=False)

b = DataFrame(df.sprachen.str.split(', ').tolist(), index=df.gymnasium).stack()
b = b.reset_index()[[0, 'gymnasium']] # var1 variable is currently labeled 0
b.columns = ['sprachen', 'gymnasium'] # renaming var1


b.to_csv('dim_sprachen.csv', index=False)
