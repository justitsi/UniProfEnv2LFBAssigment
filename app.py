#import everything we have usd in the workshops and are realistincally intended to use
import math
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import datetime
from datetime import date
import openpyxl
import xlrd
import pickle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt; plt.rcdefaults()

data = pd.read_pickle('Excel_data')
#print (data["IncidentGroup"].dtypes)

data_fire = data [data['IncidentGroup']=='Fire']
data_ss = data [data['IncidentGroup']=='Special Service']
data_fa= data [data['IncidentGroup']=='False Alarm']


data_tmp = data_ss.pivot_table(index=['SpecialServiceType'], aggfunc='size')
data_tmp.to_frame()
indexNamesArr = data_tmp.index.values
print (indexNamesArr)

for i in indexNamesArr:
    print (i)
    tmp = data_ss[data_ss['SpecialServiceType']==i]
    tmp = tmp['DateOfCall'].dt.dayofweek
    # print (tmp)
    count = tmp.value_counts()
    print (count)

    # myfigure = plt.figure()
    # plt.hist(tmp, bins = 7)
    # plt.show()




# data_byDayOfTheWeek = data_fa['DateOfCall'].dt.dayofweek
# print (data_byDayOfTheWeek)
# count = data_byDayOfTheWeek.value_counts()
# print (count)

# myfigure = plt.figure()
# plt.hist(data_byDayOfTheWeek, bins = 7)
# plt.show()