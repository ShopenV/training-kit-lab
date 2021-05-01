# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None
pd.options.display.float_format = '{:.2f}'.format

src = pd.read_csv('w16.csv')#, converters={'category': str})
src = src.loc[:23]
src['category'] = src['category'].astype(int)
#src['short_cat'] = src['category'] - 1000000000
src = src.sort_values('clients')
src.index = src['category'] - 1000000000
#src.index = src['short_cat']

dic = pd.read_csv('dic_cat1.csv', 
                  sep=';', 
                  quotechar='"', 
                  encoding='ANSI', 
                  index_col=0,
                  usecols=('category_code', 'short_name'))

rslt = pd.merge(src, dic, how='left', 
                left_index=True, right_index=True)

# signs = rslt['category_name'].tolist()
# for i in range(len(signs)):
#     signs[i] = signs[i][:9]

#rslt = rslt.sort_values('clients')
#the label locations and the width of the bars
label_locs = np.arange(len(rslt.index))
width = 0.3

fig, ax = plt.subplots(figsize=(12,8), dpi=300)

chart1 = ax.barh(label_locs - width/2, rslt['clients'], width, label='Year 2021')
chart2 = ax.barh(label_locs + width/2, rslt['ly_clients'], width, label='Year 2020')

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
# src.plot(x='short_cat', y=['clients', 'ly_clients'], kind='barh')
# plt.show()

# ax.bar(src.index-0.5, src['clients'], width=0.5, color='b')
# ax.bar(src.index, src['ly_clients'], width=0.5, color='r')
# ax.set_xlabel('category')
# ax.set_ylabel('clients quantity')
# ax.set_title('clients quantity YoY dynamic')
# plt.show()
