###
# This script will return a count of unique values from an ArcGIS
# feature class. You will need to define variables for the feature
# class and the field within the feature class that you want to search
# and get the values. Using arcpy's SearchCursor, the unique values are
# stored as a key in a dictionary and the county of those values are stored
# as values in the dictionary. The final two lines of code will print the dictionary.
###


# Import arcpy library
import arcpy

# Define variables for feature class and field in feature class
fc = r"PATH TO FEATURE CLASS"
field = "FIELD NAME"

# Create dictionary to store unique values
CountDi = {}

with arcpy.da.SearchCursor (fc, field) as cursor:
    for row in cursor:
        if not row[0] in CountDi.keys():
            CountDi[row[0]] = 1
        else:
            CountDi[row[0]] += 1

# Print the dictionary with the unique values and counts 
for key in CountDi.keys():
    print str(key) + ":", CountDi[key], "features"
