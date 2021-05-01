# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:25:19 2021

@author: LPurist2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None
pd.options.display.float_format = '{:.2f}'.format

src = pd.read_csv('w16.csv')
src = src.loc[:23]
src['category'] = src['category'].astype(int)
src = src.sort_values('clients')
src.index = src['category'] - 1000000000

dic = pd.read_csv('dic_cat1.csv', 
                  sep=';', 
                  quotechar='"', 
                  encoding='ANSI', 
                  index_col=0,
                  usecols=('category_code', 'short_name'))

rslt = pd.merge(src, dic, how='left', 
                left_index=True, right_index=True)

label_locs = np.arange(len(rslt.index))
width = 0.3

fig, ax = plt.subplots(figsize=(12,8), dpi=300)

chart1 = ax.barh(label_locs - width/2, rslt['clients'], width, label='Week 16 year 2021')
chart2 = ax.barh(label_locs + width/2, rslt['ly_clients'], width, label='Week 17 year 2020')

ax.set_xlabel('Clients quantity')
ax.set_title('Clients quantity by categories')

ax.set_yticks(label_locs)
ax.set_yticklabels(rslt['short_name'], fontsize='xx-small')#, rotation=90)
ax.legend()

#ax.bar_label(chart1, padding=3)
#ax.bar_label(chart2, padding=3)

fig.tight_layout()

plt.savefig('chart_test.png')
print(rslt.head(3))
