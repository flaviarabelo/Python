#Write a Python script that adds additional Geo information to the zip codes in the sample Order
#file. 
#• Latitude
#• Longitude
#• State
#• City
#Note: please use the following site to get the location information
#http://www.zipcodeapi.com/API#zipToLoc. They have free use API for 50 zip codes per hour


import urllib 
import string as str
import requests, json
import numpy as np
import pandas as pd

import csv

# read file
order_df = pd.read_csv('2018_07_19_Case_Study_DWH_Offside_Orders TEST (1).csv')

print (order_df)
#distinct
ls = order_df.zipcode.unique() 

#order_df['zipcode'] = order_df.to_string(columns = ['zipcode'])

#url_zip = ', '.join(my)

#ERRO concat integer list in string
#str1 = " ".join(str(e) for e in ls)

url_zipcode = '32901, 07950'
url_zipcode_aux = '32901, 07950'

print (ls)
mylist = list(set(ls))

for f in mylist: 
  url_zipcode_aux = f

print (mylist)
print (url_zipcode_aux)

#url = 'http://www.zipcodeapi.com/rest/DKUCzl4Y0d76LyJ6uqg392u5QmAtiBZ7EoaqWrPnoXjunwqVNMbu5PIaMWEHmcHA/info.csv/'+ url_zipcode + '/degrees'
url = 'http://www.zipcodeapi.com/rest/DKUCzl4Y0d76LyJ6uqg392u5QmAtiBZ7EoaqWrPnoXjunwqVNMbu5PIaMWEHmcHA/multi-info.csv/'+ url_zipcode + '/degrees'


r  = requests.get(url)
print (r.text)

#x = r.json()

#latitude_df = pd.DataFrame(x['Results'])




#order_df.set_index('zipcode')
#latitude_df.set_index('zip_code')


#result = pd.concat([order_df, latitude_df], axis=1, join_axes=[order_df.index])
#print(result)






order_df.to_csv('output_sorted.csv', index=False)




