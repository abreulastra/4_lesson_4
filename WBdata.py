# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:17:43 2016

@author: AbreuLastra_Work
"""

import csv
import sqlite3 as lite


con = lite.connect('UNdata.db')
cur = con.cursor()

with con:
    cur.execute('DROP TABLE IF EXISTS gdp')
    cur.execute('CREATE TABLE gdp (country, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010)')

with open('API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    next(inputFile) 
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:            
            cur.execute('INSERT INTO gdp (country, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[44:-5]) + '");')
    con.commit
          
con.close
    
