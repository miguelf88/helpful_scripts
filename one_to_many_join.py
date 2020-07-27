###
# Script will join many features from a table to a single feature
# Please note:
# 1. Feature class and table that you want to join have to be in the same geodatabase.
#    You will need to convert Excel of csv file to geodatabase table first and locate
#    them in the same geodatabase as the feature class.
# 2. MakeQueryTable generates a temporary layer. Use CopyFeatures_management to export
#    the layer and save it as a permanent feature class.
###

# Import libraries
import arcpy,os
from arcpy import env

# Set workspace
env.overwriteOutput = True
env.workspace = r"PATH TO GEODATABASE"

# List the polygon feature class and table that want to be joined
tableList = [ r"PATH TO GEOMETRY FILE",
             \r"PATH TO TABLE"]

# Define the query for matching
whereClause = "GEOMETRYLAYERNAME.FIELD = TABLENAME.FIELD"

# Name the temporary layer name created by MakeQueryTable
lyrName = "TEMPORARY LAYER NAME"

# Name the output fc name
outFeatureClass = "PERMANENT LAYER NAME"

arcpy.MakeQueryTable_management(tableList, lyrName,"USE_KEY_FIELDS", "", "", whereClause)

# Since lyrName created by MakeQueryTable is temporary, save it as permanent gdb file
arcpy.CopyFeatures_management(lyrName, outFeatureClass)
