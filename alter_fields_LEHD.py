###
# This script changes the field names for LEHD data. When the data is downloaded from 
# OnTheMap, attributes are alphanumeric and this script will evaluate each field title and replace
# it with a description from: https://lehd.ces.census.gov/data/lodes/LODES7/LODESTechDoc7.3.pdf
###

# Import geoprocessing
import arcpy

# Set workspace
arcpy.env.workspace = r'PATH TO GEODATABASE'

# Get a list of feature classes
# Figure out a way to only get certain feature classes in the list!!
fcList = arcpy.ListFeatureClasses()

# Print to check contents of list
print(fcList)

# Verify contents of list 
proceed_with_script = input('Would you like to continue? Y/N: ')

if proceed_with_script.upper() == 'Y':
	# Loop through feature classes
	for fc in fcList:
		# Get a list of fields for each feature class
		fieldList = arcpy.ListFields(fc)
		# Loop through each field
		for field in fieldList:
			# Print to follow along with loop
			print('I got to {} field'.format(field.name))
			# Look for fields that do not need to be changed
			if field.name == 'OBJECTID' or field.name == 'Shape' or field.name == 'id' or field.name == 'county':
				continue
			elif field.name.upper() == 'C000':
				arcpy.AlterField_management(fc, field.name, 'C000', 'Total Number of Jobs')
			elif field.name.upper() == 'CA01':
				arcpy.AlterField_management(fc, field.name, 'CA01', 'Workers age 29 or younger')
			elif field.name.upper() == 'CA02':
				arcpy.AlterField_management(fc, field.name, 'CA02', 'Workers age 30 to 54')
			elif field.name.upper() == 'CA03':
				arcpy.AlterField_management(fc, field.name, 'CA03', 'Workers age 55 or older')
			elif field.name.upper() == 'CE01':
				arcpy.AlterField_management(fc, field.name, 'CE01', 'Earnings $1,250/month or less')
			elif field.name.upper() == 'CE02':
				arcpy.AlterField_management(fc, field.name, 'CE02', 'Earnings $1,251/month to $3,333/month')
			elif field.name.upper() == 'CE03':
				arcpy.AlterField_management(fc, field.name, 'CE03', 'Earnings greater than $3,333/month')
			elif field.name.upper() == 'CNS01':
				arcpy.AlterField_management(fc, field.name, 'CNS01', 'Agriculture, Forestry, Fishing and Hunting')
			elif field.name.upper() == 'CNS02':
				arcpy.AlterField_management(fc, field.name, 'CNS02', 'Mining, Quarrying, and Oil and Gas Extraction')
			elif field.name.upper() == 'CNS03':
				arcpy.AlterField_management(fc, field.name, 'CNS03', 'Utilities')
			elif field.name.upper() == 'CNS04':
				arcpy.AlterField_management(fc, field.name, 'CNS04', 'Construction')
			elif field.name.upper() == 'CNS05':
				arcpy.AlterField_management(fc, field.name, 'CNS05', 'Manufacturing')
			elif field.name.upper() == 'CNS06':
				arcpy.AlterField_management(fc, field.name, 'CNS06', 'Wholesale Trade')
			elif field.name.upper() == 'CNS07':
				arcpy.AlterField_management(fc, field.name, 'CNS07', 'Retail Trade')
			elif field.name.upper() == 'CNS08':
				arcpy.AlterField_management(fc, field.name, 'CNS08', 'Transportation and Warehouse')
			elif field.name.upper() == 'CNS09':
				arcpy.AlterField_management(fc, field.name, 'CNS09', 'Information')
			elif field.name.upper() == 'CNS10':
				arcpy.AlterField_management(fc, field.name, 'CNS10', 'Finance and Insurance')
			elif field.name.upper() == 'CNS11':
				arcpy.AlterField_management(fc, field.name, 'CNS11', 'Real Estate and Rental and Leasing')
			elif field.name.upper() == 'CNS12':
				arcpy.AlterField_management(fc, field.name, 'CNS12', 'Professional, Scientific, and Technical Services')
			elif field.name.upper() == 'CNS13':
				arcpy.AlterField_management(fc, field.name, 'CNS13', 'Management of Companies and Enterprises')
			elif field.name.upper() == 'CNS14':
				arcpy.AlterField_management(fc, field.name, 'CNS14', 'Administrative and Support and Waste Management and Remediation Services')
			elif field.name.upper() == 'CNS15':
				arcpy.AlterField_management(fc, field.name, 'CNS15', 'Educational Services')
			elif field.name.upper() == 'CNS16':
				arcpy.AlterField_management(fc, field.name, 'CNS16', 'Health Care and Social Assistance')
			elif field.name.upper() == 'CNS17':
				arcpy.AlterField_management(fc, field.name, 'CNS17', 'Arts, Entertainment, and Recreation')
			elif field.name.upper() == 'CNS18':
				arcpy.AlterField_management(fc, field.name, 'CNS18', 'Accommodation and Food Services')
			elif field.name.upper() == 'CNS19':
				arcpy.AlterField_management(fc, field.name, 'CNS19', 'Other Services (Except Public Administration)')
			elif field.name.upper() == 'CNS20':
				arcpy.AlterField_management(fc, field.name, 'CNS20', 'Public Administration')
			elif field.name.upper() == 'CR01':
				arcpy.AlterField_management(fc, field.name, 'CR01', 'Race: White, Alone')
			elif field.name.upper() == 'CR02':
				arcpy.AlterField_management(fc, field.name, 'CR02', 'Race: Black or African American, Alone')
			elif field.name.upper() == 'CR03':
				arcpy.AlterField_management(fc, field.name, 'CR03', 'Race: American Indian or Alaska Native, Alone')
			elif field.name.upper() == 'CR04':
				arcpy.AlterField_management(fc, field.name, 'CR04', 'Race: Asian, Alone')
			elif field.name.upper() == 'CR05':
				arcpy.AlterField_management(fc, field.name, 'CR05', 'Race: Native Hawaiian or Other Pacific Islander, Alone')
			elif field.name.upper() == 'CR07':
				arcpy.AlterField_management(fc, field.name, 'CR07', 'Race: Two or More Race Groups')
			elif field.name.upper() == 'CT01':
				arcpy.AlterField_management(fc, field.name, 'CT01', 'Ethnicity: Not Hispanic or Latino')
			elif field.name.upper() == 'CT02':
				arcpy.AlterField_management(fc, field.name, 'CT02', 'Ethnicity: Hispanic or Latino')
			elif field.name.upper() == 'CD01':
				arcpy.AlterField_management(fc, field.name, 'CD01', 'Educational Attainment: Less than high school')
			elif field.name.upper() == 'CD02':
				arcpy.AlterField_management(fc, field.name, 'CD02', 'Educational Attainment: High school or equivalent, no college')
			elif field.name.upper() == 'CD03':
				arcpy.AlterField_management(fc, field.name, 'CD03', 'Educational Attainment: Some college or Associate degree')
			elif field.name.upper() == 'CD04':
				arcpy.AlterField_management(fc, field.name, 'CD04', 'Educational Attainment: Bachelors degree or advanced degree')
			# LEHD documentation lists these fields as CS01 and CS02, but download has it labeled CG01 and CG02
			elif field.name.upper() == 'CG01':
				arcpy.AlterField_management(fc, field.name, 'CG01', 'Sex: Male')
			elif field.name.upper() == 'CG02':
				arcpy.AlterField_management(fc, field.name, 'CG02', 'Sex: Female')

	# Alert user the script has finished running
	print('Script ran successfully!! Wooohooo!!')
	
# If user does not confirm list of feature classes, exit loop
else:
	print('The script will not run and the program will terminate!')
