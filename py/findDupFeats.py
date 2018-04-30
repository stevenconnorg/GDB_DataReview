# -*- #################
"""
Created on Thu Apr 26 11:15:52 2018

@author: stevenconnorg
"""

import arcpy, os
#Get path to the geodatabase
workpath = arcpy.GetParameterAsText(0)
outputCSV = arcpy.GetParameterAsText(1)
outputLayers arcpy.GetParameterAsText(2)



# Workspace
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True


def unique_values(table , field):
                with arcpy.da.SearchCursor(table, [field]) as cursor:
                    return sorted({row[0] for row in cursor})
                
outTbl = []
n = 0        


keys= ["OBJECTID","FEATUREDATASET","FEATURECLASS","DUPLICATEIDS","SUMMARY"]   
outTbl.append(keys) 
keysLen = len(keys)

outTbl[0] = keys
for dataset in arcpy.ListDatasets():  
    for fc in arcpy.ListFeatureClasses('','',dataset):

        # Find duplicate geometry
        dupeTable = "in_memory\\tmp"
        ignoreFLD = ['Shape'.upper(), 'OBJECTID'.upper(), 'Shape_Length'.upper(), 'Shape_Area'.upper()]
        flds = arcpy.ListFields(fc)
        fldNames = []
        for fld in flds:
            if fld.name not in ignoreFLD:
                fldNames.append(fld.name)
        arcpy.FindIdentical_management(fc, "in_memory\\tmp", fields = fldNames,output_record_option="ONLY_DUPLICATES")
        
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
            outLyrName = "_dupeFeats_"+fc
            uniqdupCount = len(unique_values(dupeTable , "FEAT_SEQ"))
            dupCount = len(unique_values(dupeTable , "IN_FID"))
            
            fidList.sort()
            FIDs =  ', '.join(map(str, fidList))
            n= n+1
            values= [n,dataset,fc,FIDs,str(dupCount) +" duplicates across "+str(uniqdupCount)+" features. "]

            outTbl.append(values)
              
            #arcpy.TableToTable_conversion(dupeTable, outputDir, outLyrName)
            arcpy.MakeFeatureLayer_management(fc, outLyrName, expression)
            
            
            arcpy.SaveToLayerFile_management(outLyrName, os.path.join(outputDir,outLyrName),"ABSOLUTE","10.3")
            arcpy.Delete_management(dupeTable)
            del outLyrName
            del dupeTable

import csv

if not outTbl:
    arcpy.AddMessage("No duplicate features found!")
else:
    with open(outputDir+"/Duplicate_Feature_Summary.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(outTbl)
# Save duplicate geometry results to layer file






