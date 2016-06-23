# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:50:12 2016

@author: AbreuLastra_Work
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3 as lite

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

#copy webpage

r = requests.get(url)


soup = BeautifulSoup(r.content)

for row in soup('table'):
    print(row)


# setting our headers
country = []
year = []
total = []
men = []
women = []


table = soup('table')[9]

# Find all the <tr> tag pairs, skip the first one, then for each.
for row in table.find_all('tr')[4:]:
    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')
    
    # Create a variable of the string inside 1st <td> tag pair,
    column_1 = col[0].string.strip()
    # and append it to countryvariable
    country.append(column_1)
    
    # Create a variable of the string inside 2nd <td> tag pair,
    column_2 = col[1].string.strip()
    # and append it to year variable
    year.append(column_2)
    
    # Create a variable of the string inside 3rd <td> tag pair,
    column_3 = col[4].string.strip()
    # and append it to total variable
    total.append(column_3)
    
    # Create a variable of the string inside 4th <td> tag pair,
    column_4 = col[7].string.strip()
    # and append it to men variable
    men.append(column_4)
    
    # Create a variable of the string inside 5th <td> tag pair,
    column_5 = col[10].string.strip()
    # and append it to women variable
    women.append(column_5)

year = [int(i) for i in year]
total = [int(i) for i in total]
men = [int(i) for i in men]
women = [int(i) for i in women]

# Create a variable of the value of the columns
columns = {'year': year,'country': country, 'total': total, 'men': men, 'women': women}
# Create a dataframe from the columns variable
df = pd.DataFrame(columns)

con = lite.connect('UNdata.db')
cur = con.cursor()
with con:
    cur.execute('DROP TABLE IF EXISTS school_years')
    
df.to_sql("school_years",con)

