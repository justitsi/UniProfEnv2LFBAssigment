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

data = pd.read_pickle('Excel_data')
#print data for first and 2000nd element

#print (data.describe())
#print(data['DateOfCall'].loc[2000])
sub_data_2firetrucks = data [data['NumPumpsAttending']==12]
print (sub_data_2firetrucks.loc[244943])