
"""
=============================================================================
Filename      : PlotMap
Author        : Sunderam Palavesam
Date Created  : 17 Dec 2022
=============================================================================
Description   : Plot the cities based on lat and lon from input csv
                Developed as part of course work AC50002
                Developed as part of Python assignment Msc course Work
                Dundee University
credits       : https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
Revisions
=============================================================================
23122022   2474761 AC50002  initial version                               1.0
=============================================================================
"""
# pre-requisite - 
#pip install numpy, pandas, matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv and laod to a pandas dataframe
df = pd.read_csv("C:\SSP\masters\ProgLang\wip\GrowLocations.csv")

#data cleansing , remove dupes and extract latitudes and longitudes
myCols =  ['Latitude','Longitude']
df1 = df[myCols].drop_duplicates(subset=None,keep="first",inplace=False)

#rename columns as its incorrect
df1.rename(columns={'Latitude':'Longitude','Longitude':'Latitude'},inplace=True)

#print the final cleansed result for verification
print(df1)

#define the bounding box for the map
BBox = (-10.592,   1.6848,  50.681, 57.985)

#load the map image
myMap = plt.imread('C:\SSP\masters\ProgLang\wip\map7.png')

#create a figure and set of subplot
fig, ax = plt.subplots(figsize = (8,10))
ax.scatter(df1.Longitude, df1.Latitude, c='b')
ax.set_title('Plotting Grow Data ')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(myMap, zorder=0, extent = BBox, aspect= 'equal')
#show the plotted map
plt.show()


