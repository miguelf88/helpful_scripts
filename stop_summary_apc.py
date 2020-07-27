##############
#This script will process Stop Summary APC (automatic passenger count) data and manipulate it so it is ready for use in Excel.
#You will need to provide the path to the three stop summary reports (wkdy, sat, sun) as well as specify the path for the
#final file.

#Last updated: 2019/11/15

#TO DO: Create some validation feature that removes stops that are not associated with a particular route
       #Create user inputs for APC data files for weekday, Saturday, and Sunday  
##############

# Import libraries
import pandas as pd

# Read in APC data from local source
wkdy = pd.read_excel('PATH TO WEEKDAY FILE')
sat = pd.read_excel('PATH TO SATURDAY FILE')
sun = pd.read_excel('PATH TO SUNDAY FILE')

# Read in Stop Code Master to replace the values in the STOP_NAME column
stops = pd.read_excel('W:\\COMMUTER OPERATIONS DEPT\\PART Express Operations\\Stop Codes\\Stop Code Master.xlsx')

# Fix header row in stops dataframe
new_header = stops.iloc[0]
stops1 = stops[1:]
stops1.columns = new_header
stops1 = stops1[['stop_code', 'stop_name', 'stop_lat', 'stop_lon']]
stops1.dropna(inplace=True)
stops1['stop_code'].astype('int')
stops1 = stops1.set_index('stop_code')

# Concatenate the dataframes
df = pd.concat([wkdy, sat, sun])

# Rename columns
df.rename(columns = {
    'DAY_OF_WEEK': 'DAY',
    'UNIQUE_STOP_NO': 'STOP_CODE',
    'SEQUENTIAL_STOP_NO': 'SEQUENCE',
    'STOPNAME': 'STOP_NAME'
    },
    inplace=True)

# Define function to add service period
def service_period(row):
    time = row[3]
    if time < 900:
        return 'AM Peak'
    elif time >= 900 and time < 1500:
        return 'Off Peak'
    elif time >= 1500 and time < 1800:
        return 'PM Peak'
    else:
        return 'Evening'

# Create new field for service period and apply function
df['SERVICE_PERIOD'] = df.apply(lambda time: service_period(time), axis=1)

# Round the ON, OFF, and LOAD columns
df[['ON', 'OFF', 'LOAD']] = df[['ON', 'OFF', 'LOAD']].round(2)

# Drop columns that will be replaced with the merge
df.drop(['PATTERN', 'LAT', 'LONG', 'SAMPLES', 'STOP_NAME'], axis=1, inplace=True)

# Define function to create ROUTE_LONG_NAME
def route_name(row):
    name = row[1]
    if name == 1:
        return '1 - Winston-Salem Express'
    elif name == 2:
        return '2 - Greensboro Express'
    elif name == 3:
        return '3 - High Point Express'
    elif name == 4:
        return '4 - Alamance-Burlington Express'
    elif name == 5:
        return '5 - NC Amtrak Connector'
    elif name == 6:
        return '6 - Surry County Express'
    elif name == 9:
        return '9 - Davidson Business 85 Express'
    elif name == 10:
        return '10 - Randolph Express'
    elif name == 17:
        return '17 - Kernersville Express'
    elif name == 19:
        return '19 - Palladium Circulator'
    elif name == 20:
        return '20 - NW Pleasant Ridge'
    elif name == 21:
        return '21 - NE Chimney Rock'
    elif name == 22:
        return '22 - SW Sandy Ridge'
    elif name == 23:
        return '23 - SE Piedmont Parkway'
    elif name == 27:
        return '27 - Airport Area'
    elif name == 28:
        return '28 - West Forsyth Express'
    else:
        return 'Undefined'

# Create new field and apply function
df['ROUTE_LONG_NAME'] = df.apply(lambda name: route_name(name), axis=1)

# Merge the stops dataframe with the APC dataframe
final = df.merge(stops1, left_on='STOP_CODE', right_on='stop_code')

# Write the final dataframe to an excel file
final.to_excel('PATH TO FINAL OUTPUT')
