import pandas as pd
import numpy as np

data = pd.read_csv('test.txt')

column1 = data['column1']
column2 = data['column2']

print("-----------column 1----------\n{column1}\n".format(column1 = column1))
print("-----------column 2----------\n{column1}\n".format(column1 = column2))

allData = data.iloc[:,:] #all data
print("-----------all data----------\n{column1}\n".format(column1 = allData))

part1  = data.iloc[:7,2] #till the first column and second row
print("-----------:7,2 part----------\n{column1}\n".format(column1 = part1))

part2 = data.iloc[2:7,'column3']
print("-----------part 2 ----------\n{column1}".format(column1 = part2))

