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
#print (data.dtypes)
#print 
data_fire = data [data['IncidentGroup']=='Fire']
data_ss = data [data['IncidentGroup']=='Special Service']
data_fa= data [data['IncidentGroup']=='False Alarm']

#print(data_fa,data_ss,data_fire)

data_tmp = data_ss.pivot_table(index=['SpecialServiceType'], aggfunc='size')
data_tmp.to_frame()
# print (data_tmp)
indexNamesArr = data_tmp.index.values

for i in indexNamesArr:
    # print ("----------------------------------------")
    # print (i)
    tmp = data_ss[data_ss['SpecialServiceType']==i]
    tmp = tmp['DateOfCall'].dt.dayofweek
    count = tmp.value_counts()
    # print (count)

    # TOO MANY CHARTSS
    # myfigure = plt.figure()
    # plt.hist(tmp, bins = 7)
    # plt.show()

print("START PER BOROUGH INFO")
data_tmp = data_ss.pivot_table(index=['IncGeo_BoroughName'], aggfunc='size')
data_tmp.to_frame()
# print (data_tmp)
indexNamesArr = data_tmp.index.values
for i in indexNamesArr:
    # print ("----------------------------------------")
    # print (i)
    tmp = data_ss[data_ss['IncGeo_BoroughName']==i]
    tmp = tmp['DateOfCall'].dt.dayofweek
    count = tmp.value_counts()
    # print (count)

    # TOO MANY CHARTSS
    # myfigure = plt.figure()
    # plt.hist(tmp, bins = 7)
    # plt.show()


#LOOKING AT WESTMINSTER SPECIAL SERVICES:
data_WM = data_ss[data['IncGeo_BoroughName']=='WESTMINSTER']
data_tmp = data_WM.pivot_table(index=['SpecialServiceType'], aggfunc='size')
data_tmp.to_frame()
indexNamesArr = data_tmp.index.values
for i in indexNamesArr:
    # print ("----------------------------------------")
    # print (i)
    tmp = data_WM[data_WM['SpecialServiceType']==i]
    tmp = tmp['DateOfCall'].dt.dayofweek
    count = tmp.value_counts()
    # print (count)

    # TOO MANY CHARTSS
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