# PYTHON script
'''

Converting a .csv file to Python dictionary

'''

import csv
import pprint as pp

signs_dict = {}
dict_list = []

i = 0
with open('signnames.csv', newline='') as csvfile:
    row_reader = csv.reader(csvfile, delimiter=',')
    for row in row_reader:
        dict_list.append(row)
        if (i != 0):
            signs_dict[i-1] = dict_list[i][1]
        i = i + 1
        
pp.pprint(signs_dict)
