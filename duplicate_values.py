###
# This script identifies duplicate values from a table in ArcGIS
# You will need to create a new string column (Concat) and concatenate all the 
# attributes that you want to identify as duplicate. After that, order the new column
# (Concat) by ascending order.
# Create a new integer column (Duplicates) and use the fuction in the field calcualator.
# Select Calculate field for the new Duplicates field and enter the function below in the code block section
# Then, in the expression box, enter 'isDuplicate(name of field) and click run.
# After the field is calculated, you can sort the duplicates field to see which records are duplicates.
# Duplicate values are identified with a 1 while unique values are identified with a 0.


#creates a list that will store a list of unique values from the concat field
uniqueList = []

def isDuplicate(inValue):

  #checking to see if value is in the list
  if inValue in uniqueList:

    #if the value is in the list returns a value of 1
    return 1

  else:

    #if the value is not in the list, add it to the list, and return 0
    uniqueList.append(inValue)

    return 0
