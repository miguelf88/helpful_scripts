#!/usr/bin/env python
# coding: utf-8

###
# Due to COVID-19, GoTriangle has put their On-Board Survey on hold.
# The agency wants to examine ridership weekly to establish a baseline level for ridership
# When ridership returns to normal or a new normal is identified, the survey will proceed.
# GoTriangle has requested ridership every week so I wrote this script to automate the process
# The ridership data is saved with the week in the file name
# The final file is saved with the day it was written to track updates
###

# Import libraries
import pandas as pd
from os import walk
from datetime import date

# Set path to data
path = r'D:\Project Data\Triangle Data Request\Triangle Request'

# Read in data
f = []
for (dirpath, dirnames, filenames) in walk(path):
    for x in filenames:
        if x.startswith('stop'):
            f.append(x)
            
# Create empty lists
week_of = []
avg_ridership = []
route = []
dayOfWeek = []

# Loop through files and perform calculations
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

# Set today's date
today = str(date.today())

# Write to csv file
output.to_excel("D:\Project Data\Triangle Data Request\PART_ridership_" + today + ".xlsx", index = False)
