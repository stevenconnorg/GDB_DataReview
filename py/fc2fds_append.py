import arcpy, os
import pandas

# get inputs
mainDir = "C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\AF_Installation_Feedback"
os.chdir(mainDir)

def getDirectoryFiles(directory):
    dirFileList = []
    for subdir, dirs, files in os.walk(directory):
        for subdir in dirs:
            subdirPath = os.path.join(directory,subdir)
            dirFileList.append(subdirPath)
    return(dirFileList)
            

# to get feature dataset, feature class combinations in target geodatabase in dataframe
def getFeaturesdf(GDB):
	'''
	# to get unique FDS, FC, and FIELDS across a geodatabase
	Parameters
	----------
	GDB = path to GDB
	
	Returns
	-------
	pandas dataframe of with two columns: Feature Dataset, Feature Class for each fc in gdb.
	'''

	d = pandas.DataFrame([])
	arcpy.env.workspace = GDB
	for theFDS in arcpy.ListDatasets():
		for theFC in arcpy.ListFeatureClasses(feature_dataset=theFDS):
			d = d.append(pandas.DataFrame({'FDS': theFDS, 'FC': theFC}, index=[0]), ignore_index=True)
	return(d)

def fc2fds(installGDB,compGDB):
	## get target geodatabase
	path_gdb = compGDB
	## get source data geodatabase
	path_sGDB = installGDB
	gdb = os.path.basename(path_sGDB) # get gdb name
	filename = os.path.splitext(gdb) # get name without extension
	gdbN = filename[0]
	gbdName = gdbN+".gdb" # append 'cleaned' to name 
	if arcpy.Exists(os.path.join(mainDir,"gdbs-cleaned",gbdName)):
                print gbdName +" exists in gdbs-cleaned directory! Using this gdb!"
		pass
	else:
		arcpy.CreateFileGDB_management (os.path.join(mainDir,"gdbs-cleaned"), gbdName) # and create empty gdb as '[gdbName]_cleaned'
	outGDB = os.path.join(mainDir,"gdbs-cleaned",gbdName) # path to outout gdb
	# get list of feature classes in source geodatabase (they're all loose feature classes)
	arcpy.env.workspace = path_sGDB
	#arcpy.env.overwriteOutput = True 
	fcList=list(arcpy.ListFeatureClasses())
	# get fds, fc combos for target geodatabase
	targetFeatures = getFeaturesdf(path_gdb)
	# get list of unique fds in target geodatabase to create in new out gdb
	target_ds = list(targetFeatures.FDS.unique())
	# also add a nonSDS feature dataset for all nonSDS feature classes
	target_ds.append('nonSDS')
	# for feature datasets in target feature dataset, create in new, empty geodatabase
	for ds in target_ds: 
		if arcpy.Exists(os.path.join(outGDB, ds)):
			print "{} exists, passing !".format(ds)
			#arcpy.Delete_management(os.path.join(path_sGDB,ds))
			#arcpy.CreateFeatureDataset_management(outGDB,ds,spatial_reference = os.path.join(path_sGDB,fcList[1])) # arbitrarily set FDS srs to srs of random fc in list
			pass
		else:
			print "{} doesn't exist; creating".format(ds)
			arcpy.CreateFeatureDataset_management(outGDB,ds,spatial_reference = os.path.join(path_sGDB,fcList[1]))
	# for each loose feature class in source gdb, copy to associated feature dataset in new gdb, where applicable
	# else, just copy the loose feature class to gdb outside of feature dataset
	targetFCs = list(targetFeatures['FC'].tolist())
	for fc in fcList:
		if fc in targetFCs:
			targetFDS = targetFeatures.loc[targetFeatures['FC'] == fc,'FDS']
			targetFDS = list(targetFDS)[0]
			if arcpy.Exists(os.path.join(outGDB,targetFDS,fc)):
				print "Replacing " + fc + " in " + targetFDS
				arcpy.Delete_management(os.path.join(outGDB,targetFDS,fc))
				arcpy.CopyFeatures_management(os.path.join(path_sGDB,fc), os.path.join(outGDB,targetFDS,fc))

			else:
				print "Copying " + fc + " to " + targetFDS
				arcpy.AppendFeatures_management(os.path.join(path_sGDB,fc), os.path.join(outGDB,targetFDS,fc))
		else:
			print fc + " doesn't exist in " + path_gdb
			arcpy.AppendFeatures_management(os.path.join(path_sGDB,fc), os.path.join(outGDB,"nonSDS",fc))
		#arcpy.Delete_management(tempFC)
		del targetFDS
	del target_ds
	del fcList
	del outGDB
	del path_sGDB
	del path_gdb

# define comparison/target geodatabase inside targetGDBdir ("gdbs-target")
installationGDBdir = os.path.join(mainDir,"gdbs")
targetGDBdir = os.path.join(mainDir,"gdbs-target")
compGDB = os.path.join(targetGDBdir,"Full.gdb")
installationgdbList =  getDirectoryFiles(installationGDBdir)

# for each gdbs in installationGDBdir, create new geodatabase inside "gdbs-cleaned" directory & move source feature classes into respective feature datasets according to target geodatabase  
for installGDB in installationgdbList:
	installationName = os.path.splitext(os.path.basename(installGDB))[0]
	#print ("Getting Feature Datasets, Feature Classes and Fields for " + compGDB)
	#compFeaturesdf = getFeaturesdf(GDB=compGDB)
	compName = os.path.splitext(os.path.basename(compGDB))[0]
	fc2fds(installGDB,compGDB)
