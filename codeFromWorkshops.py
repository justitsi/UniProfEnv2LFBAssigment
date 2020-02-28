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
#Formatting comments that don't make sense
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)

data = pd.read_pickle('Excel_data')
#print data for first and 2000nd element
#print(data['DateOfCall'].loc[0])
#print(data['DateOfCall'].loc[2000])

#TASK 1 get most common day for fires in takeaway shops
#------------------------------------------------------
data['PropertyType'] = data['PropertyType'].str.strip()
sub_data = data [data['PropertyType']=='Takeaway/ fast food']

month_data = sub_data['DateOfCall'].dt.day_name()
print (month_data.describe())

# combining dataseries into dataframe
sub_data1 = pd.DataFrame(data['NumPumpsAttending'], data['HourOfCall'])
print(sub_data1)

#TASK 2 corelation between hour and num of pumps??
#-------------------------------------------------
#engines = data['NumPumpsAttending'].values
#time = data['FirstPumpArriving_AttendanceTime'].values
#engines_n= np.nan_to_num(engines)
#time_n= np.nan_to_num(time)
#corr= np.corrcoef(time_n, engines_n)
#print (corr)

#TASK 3 Create histogram and don't get cancer
#data['PropertyType'] = data['PropertyType'].str.strip()
#sub_data2 = data [data['PropertyType']=='Student Hall of Residence']

#sh_month = sub_data2['DateOfCall'].dt.month
#print (sh_month)
#count = sh_month.value_counts()
#print (count)

#myfigure = plt.figure()
#plt.hist(sh_month, bins = 12)
#plt.show()

# TASK 4 - original try for a 3D diagram
# x = data['Northing_rounded']
# y = data['Easting_rounded']
# z = data.groupby(['Northing_rounded','Easting_rounded'])['Northing_rounded', 'Easting_rounded'].count()
# z = z['Northing_rounded'].values

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# x, y = np.meshgrid('north_round', 'east_round')
# ax.plot_wireframe(x, y, z)

# ax.set_xlabel ('Northing')
# ax.set_ylabel('Easting')
# ax.set_zlabel('Number of calls')

# ax.show()

# TASK 4 - actual working try for a 3D diagram
# table = pd.pivot_table(data, values=['IncidentNumber'], index=['Easting_rounded'], columns=['Northing_rounded'], aggfunc='count')

# surf_mat = table.values

# x = np.unique(data['Easting_rounded'].values)
# y = np.unique(data['Northing_rounded'].values)
# z = np.nan_to_num(surf_mat)
# x= x.reshape(x.shape[0], 1)
# y= y.reshape(y.shape[0], 1).T

# fig = plt.figure()
# ax = Axes3D(fig)

# ax.plot_surface(x, y, z,  cmap=cm.coolwarm)

# ax.set_xlabel('Northing')
# ax.set_ylabel('Easting')
# ax.set_zlabel('Number of calls')

# plt.show()