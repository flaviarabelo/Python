
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
 # https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

# Create a file to write to, add headers row
f = csv.writer(open('gymnasium-names.csv', 'w'))
#f.writerow(['Name', 'Link'])


page = requests.get('https://www.gymnasium-berlin.net/schulliste')

soup = BeautifulSoup(page.text, "html.parser")

gymnasium_name_list = soup.find(class_='view-content')

gymnasium_name_list_items = gymnasium_name_list.find_all('a')

pages = []
names = []
for gymnasium_name in gymnasium_name_list_items:
    names = gymnasium_name.contents[0]
    #print(gymnasio_name.prettify())
    links = 'https://www.gymnasium-berlin.net' + gymnasium_name.get('href')
    #print(names)
    #print(links)
    pages.append(links)    
    #f.writerow([names, links])

for item in pages:
    #print(item)
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Pull all text from the field-item even  div
    field_item_list = soup.find(class_='field-item even')

    #print (field_item_list)
    
    # Pull text from all instances of <p> tag within field-item div
    field_item_list_items = field_item_list.find_all('p')
    
    list_columns = []
    #print(field_item_list.get_text())
    
    #print(names)
    for item_p in field_item_list:
        #items = item_p.contents[0]
        items = item_p.get_text()
       
        list_columns.append( items)
        if item_p == 'a':
            list_columns.append(item_p.get('href'))

    print(list_columns)
    
    #f.writerow(list_columns)

csv = []
with open('gymnasium-names2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pd.concat([Series(row['gymnasium'], row['fach'].split(','))              
            for _, row in a.iterrows()]).reset_index()

print (pd)
