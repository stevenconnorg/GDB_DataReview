# -*- #################
"""
Created on Thu Apr 26 11:15:52 2018

@author: stevenconnorg
"""

import arcpy, os, sys
#Get path to the geodatabase
workpath = arcpy.GetParameterAsText(0)
xyTolerance = arcpy.GetParameterAsText(1)
zTolerance = arcpy.GetParameterAsText(2)
outputCSV = arcpy.GetParameterAsText(3)
outputLayers =  arcpy.GetParameterAsText(4)

# Workspace
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True


def unique_values(table , field):
                with arcpy.da.SearchCursor(table, [field]) as cursor:
                    return sorted({row[0] for row in cursor})
                

# some error checking
if not outputCSV.endswith('.csv'):
    arcpy.AddError("Your outputCSV file does not end with '.csv'. Try writing to a csv file (e.g.: 'C:/path/to/file.csv'.")
    sys.exit(0)
if not os.path.exists(outputLayers):
    arcpy.AddError("It doesn't like "+ outputLayers+" exists. Create a directory to write to or try writing output layer files to another writable directory/folder.")
    sys.exit(0)
if not os.path.isdir(outputLayers):
    arcpy.AddError("It doesn't like "+ outputLayers+" is a directory/folder. Try writing output layer files to a writable directory/folder.")
    sys.exit(0)
if not os.access(outputLayers, os.W_OK):
    arcpy.AddError("It doesn't look like you can write to "+ outputLayers+". Try writing output layer files to a writable directory/folder.")
    sys.exit(0)

# for output table
outTbl = []
n = 0        
keys= ["OBJECTID","FEATUREDATASET","FEATURECLASS","DUPLICATEIDS","SUMMARY"]   
outTbl.append(keys) 
keysLen = len(keys)


FDSs = arcpy.ListDatasets()
if len(FDSs) == 0:
    arcpy.AddError("Zero feature datasets found in " + workpath+". \n Try migrating your feature classes to a feature datasets.")    
    sys.exit(0)
else:
    for dataset in FDSs:  
        for fc in arcpy.ListFeatureClasses('','',dataset):
            fcCount = arcpy.GetCount_management(fc)
            if int(fcCount[0]) == 0:
                arcpy.AddMessage("No features in "+fc+" ... skipping!")
                pass
            else:
                # Find duplicate geometry
                dupeTable = "in_memory\\tmp"
                arcpy.FindIdentical_management(fc, "in_memory\\tmp", ["Shape"],xy_tolerance= xyTolerance, z_tolerance = zTolerance, output_record_option="ONLY_DUPLICATES")
                
                # Get table count and pass the dataset if no duplicates exist
                tblCount = arcpy.GetCount_management(dupeTable)
                print fc + " duplicate feature count: " + str(tblCount)
                arcpy.AddMessage(fc + " duplicate feature count: " + str(tblCount))
                if int(tblCount[0]) == 0:
                    arcpy.Delete_management("in_memory\\tmp") 
                    continue
                
                
                
                else:
        			# Get Object IDs of duplicate values to build expression for layer file
                    fidList=[]
                    with arcpy.da.SearchCursor(dupeTable,["IN_FID"]) as cursor:
                        for row in cursor:
                            fidList.append(row[0])
                    expression = 'OBJECTID IN ({0})'.format(', '.join(map(str, fidList)) or 'NULL')
        
        			# Save Find Identical table and delete in memory table
                    outLyrName = "_dupeGeom_"+fc
                    uniqdupCount = len(unique_values(dupeTable , "FEAT_SEQ"))
                    dupCount = len(unique_values(dupeTable , "IN_FID"))
                    
                    fidList.sort()
                    FIDs =  ', '.join(map(str, fidList))
                    if len(FIDs) > 32767: #excel cell character limit
                        FIDs = "Listing of FIDs with duplicate geometries exceeds Excel cell character limit."
                    n= n+1
                    values= [n,dataset,fc,FIDs,str(dupCount) +" duplicates across "+str(uniqdupCount)+" features. "]
        
                    outTbl.append(values)
                      
                    #arcpy.TableToTable_conversion(dupeTable, outputDir, outLyrName)
                    arcpy.MakeFeatureLayer_management(fc, outLyrName, expression)
                    
                    
                    arcpy.SaveToLayerFile_management(outLyrName, os.path.join(outputLayers,outLyrName),"ABSOLUTE","10.3")
                    arcpy.Delete_management(dupeTable)
                    del outLyrName
                    del dupeTable

import csv

if not outTbl:
    arcpy.AddMessage("No duplicate geometries found!")
else:
    with open(outputCSV, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(outTbl)
# Save duplicate geometry results to layer file









