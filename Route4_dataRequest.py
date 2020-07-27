#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
from os import walk
from datetime import date


# In[45]:


path = r'D:\Project Data\Triangle Data Request\Triangle Request'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    for x in filenames:
        if x.startswith('stop'):
            f.append(x)


# In[79]:


week_of = []
avg_ridership = []
route = []
dayOfWeek = []

for filename in f:
    df = pd.read_excel(path + '\\' + filename)  # read in excel file
    file_slice = filename[18:26]  # create object that contains start of week date
    week_of.append(file_slice)  # append the start of week date to list
    s = round(df['ON'].sum(),2)  # sum avg daily ridership
    avg_ridership.append(s)  # append ridership to list
    route.append(4)  # append route number to list
    dayOfWeek.append("Weekday")  # append day of week to list

# Create final dataframe
output = pd.DataFrame({'Week Of': week_of,
                       'AVG Ridership': avg_ridership,
                       'Route': route,
                       'Day of Week': dayOfWeek})

# Convert `Week Of` to date
output['Week Of'] = pd.to_datetime(output['Week Of'], format = '%Y%m%d')
# Remove the time component from datetime object
output['Week Of'] = output['Week Of'].dt.date


# In[80]:


today = str(date.today())

# Write to csv file
output.to_excel("D:\Project Data\Triangle Data Request\PART_ridership_" + today + ".xlsx", index = False)


# In[ ]:





# In[ ]:




