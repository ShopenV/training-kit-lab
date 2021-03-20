# -*- coding: utf-8 -*-
#CH csv to dataframe

from pathlib import Path
import csv
import pandas as pd

pd.set_option('display.max_columns', None)
crs_file = Path("D:\Clickhouse2\Explore_CH\CH-arrays.csv")

# create an array of arrays from rows
l = []
with open(crs_file) as f:
    reader = csv.reader(f)
    for row in reader:
        l.append(row)
if len(l) < 2:
    content = 0
elif len(l) == 2:
    content = 1
else:
    content = 1
    print('Not all rows were included, check the code to add more than 1 content row')

for i in range(len(l[content])):
    l[content][i] = l[content][i].split(',')
    for j in range(len(l[content][i])):
        l[content][i][j] = (l[content][i][j]).strip()

# rewrite for a case when there's no name for a column, or no headers at all
l_dict = {}
for x in range(len(l[content])):
    l_dict[l[0][x]] = l[content][x]

df = pd.DataFrame(l_dict)

print(df)