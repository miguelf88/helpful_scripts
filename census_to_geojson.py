# This script reads in data from the Census API
# Configures a dataframe
# and rides the data to geoJSON

# Import libraries
import pandas as pd
import numpy as np
import requests
import geopandas as gpd

subject_variables = {
    # Income variables
    'Total Households':                        'S1901_C01_001E',
    'Households Earning Less than 10,000 %':   'S1901_C01_002E',
    'Households Earning 10,000 to 14,999 %':   'S1901_C01_003E',
    'Households Earning 15,000 to 24,999 %':   'S1901_C01_004E',
    'Households Earning 25,000 to 34,999 %':   'S1901_C01_005E',
    'Households Earning 35,000 to 49,999 %':   'S1901_C01_006E',
    'Households Earning 50,000 to 74,999 %':   'S1901_C01_007E',
    'Households Earning 75,000 to 99,999 %':   'S1901_C01_008E',
    'Households Earning 100,000 to 149,999 %': 'S1901_C01_009E',
    'Households Earning 150,000 to 199,999 %': 'S1901_C01_010E',
    'Households Earning 200,000 or more %':    'S1901_C01_011E',
    'Households Median Income':                'S1901_C01_012E',
    'Households Mean Income':                  'S1901_C01_013E',
    'Population Below Poverty Level':          'S1701_C02_001E',
    # Commute variables
    'Total Workers':                           'S0801_C01_001E',
    'Drove Alone %':                           'S0801_C01_003E',
    'Carpooled %':                             'S0801_C01_004E',
    'Public Transportation %':                 'S0801_C01_009E',
    'Walked %':                                'S0801_C01_010E',
    'Biked %':                                 'S0801_C01_011E',
    'Taxi/Motorcycle/Other %':                 'S0801_C01_012E',
    'Worked from Home %':                      'S0801_C01_013E',
    'Work in County of Residence %':           'S0801_C01_015E',
    'Work outside County of Residence %':      'S0801_C01_016E',
    'Work outside State of Residence %':       'S0801_C01_017E',
    'Travel Time Less than 10 Minutes %':      'S0801_C01_037E',
    'Travel Time 10 to 14 Minutes %':          'S0801_C01_038E',
    'Travel Time 15 to 19 Minutes %':          'S0801_C01_039E',
    'Travel Time 20 to 24 Minutes %':          'S0801_C01_040E',
    'Travel Time 25 to 29 Minutes %':          'S0801_C01_041E',
    'Travel Time 30 to 34 Minutes %':          'S0801_C01_042E',
    'Travel Time 35 to 44 Minutes %':          'S0801_C01_043E',
    'Travel Time 45 to 59 Minutes %':          'S0801_C01_044E',
    'Travel Time 60 Minutes or More %':        'S0801_C01_045E',
    'Travel Time Mean':                        'S0801_C01_046E'
}

detail_variables = {
    # Race variables
    'Total Population':                        'B01003_001E',
    'Race White':                              'B02001_002E',
    'Race Black':                              'B02001_003E',
    'Race American Indian/Alaska Native':      'B02001_004E',
    'Race Asian':                              'B02001_005E',
    'Race Native Hawwaiian/Pacific Islander':  'B02001_006E',
    'Race Some Other Race':                    'B02001_007E',
    'Race Two or More':                        'B02001_008E'
}

# Get codes to pass into URL
subject_codes = ','.join(['%s' % (value) for (value) in subject_variables.values()])
detail_codes = ','.join(['%s' % (value) for (value) in detail_variables.values()])

# Make calls to the Census API
nc_subject = requests.get('https://api.census.gov/data/2018/acs/acs5/subject?get=' + subject_codes + '&for=tract:*&in=state:37').json()
nc_detailed = requests.get('https://api.census.gov/data/2018/acs/acs5/?get=' + detail_codes + '&for=tract:*&in=state:37').json()

# Create dataframes from the response variables
nc_df_sub = pd.DataFrame(nc_subject)
nc_df_det = pd.DataFrame(nc_detailed)

# Create list for geographic ids in census data
geo_ids = ['State', 'County', 'Tract']

# Create lists to rename columns using keys in dictionary
subject_headers = list(subject_variables.keys()) + geo_ids
detail_headers = list(detail_variables.keys()) + geo_ids

# Start dataframe on second row
nc_df_sub = nc_df_sub[1:]
nc_df_det = nc_df_det[1:]

# Rename columns
nc_df_sub.columns = subject_headers
nc_df_det.columns = detail_headers

# Create new index by concatenating state, county and tract to give each record unique ID
nc_df_sub['ID'] = nc_df_sub['State'] + nc_df_sub['County'] + nc_df_sub['Tract']
nc_df_sub.set_index('ID', inplace=True)

nc_df_det['ID'] = nc_df_det['State'] + nc_df_det['County'] + nc_df_det['Tract']
nc_df_det.set_index('ID', inplace=True)

# Join the two data frames together
nc_census = nc_df_det.merge(nc_df_sub, how = 'outer', on = 'ID')

# Drop columns left over from join
nc_census.drop(['State_x', 'State_y', 'County_x', 'County_y', 'Tract_x', 'Tract_y'], axis = 1, inplace = True)

# Convert variables to numeric data types
nc_census = nc_census.apply(pd.to_numeric, errors='coerce')

# Read in census tract geography
census_geo = gpd.read_file(r'D:\U.S. Census\2018 NC Census Tracts\tl_2018_37_tract.shp')

# Join tabular data to geography
census_data = census_geo.merge(nc_census, left_on='GEOID', right_on='ID')

# Write dataframe to geojson
census_data.to_file(r'D:\Project Data\Commuter Analysis\nc_census.geojson', driver='GeoJSON')
