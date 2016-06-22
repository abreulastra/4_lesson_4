# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:43:01 2016

@author: AbreuLastra_Work
"""

import pandas as pd
import sqlite3 as lite
import matplotlib.pyplot as plt
import math
import numpy as np

con = lite.connect('UNdata.db')
cur = con.cursor()

df = pd.read_sql_query('SELECT * FROM school_years INNER JOIN gdp USING (country)', con)

df = df.replace('',np.nan, regex=True)
df = df.dropna()

gdp_99 = [float(i) for i in df['_1999']]
df['log_gdp_99'] = map (lambda x: math.log(x), gdp_99)

df['_1999'] = gdp_99

df.corr()

plt.scatter(df['_1999'],df['total'])
plt.show()

plt.figure()
plt.scatter(df['log_gdp_99'],df['total'])
plt.show()