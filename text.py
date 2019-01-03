import matplotlib.pyplot as plt
import matplotlib.com as cm
from matplotlib.colors import Normalize
from numpy.random import random
import csv
import collections

#read csv file using dictionary
f = open('data.csv')
csv_f = csv.DictReader(f)

#Create and fill dictionary with keys = purpose, values = lists of corresponding interest rates
data={}
for row in csv_f:
    if row['purpose'] in data:
        data[row['purpose']].append(row['int_rate'])
    else:
        data[row['purpose']] = [row['int_rate']]
#Create new dictionary with keys = keys of data, & values = perform mean calculation of data value list elements
mean = {k:((sum(map(float,v)))/float(len(v))) for k,v in data.items()}
print(mean)

#Sort <mean> into key alpha ordered list
od = collections.OrderedDict(sorted(mean.items()))

plt.bar(od.keys(), od.values(), color='g')
#plt.rc({'xtick': 5})

plt.show()

#close file reader
f.close()
