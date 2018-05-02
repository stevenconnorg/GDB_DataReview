# -*- #################
"""
Created on Thu Apr 26 11:15:52 2018

@author: stevenconnorg
"""

import arcpy
#Get path to the geodatabase
workpath = arcpy.GetParameterAsText(0)
xyTol = arcpy.GetParameterAsText(1)
zTol = arcpy.GetParameterAsText(2)

# Workspace
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True

def unique_values(table , field):
                with arcpy.da.SearchCursor(table, [field]) as cursor:
                    return sorted({row[0] for row in cursor})
                
for dataset in arcpy.ListDatasets():  
    for fc in arcpy.ListFeatureClasses('','',dataset):
        fcCount = arcpy.GetCount_management(fc)
        ignoreType = ['OID', 'Guid',  'GlobalID', 'Blob','Raster']
        ignoreFld = ['LAST_EDITED_DATE','LAST_EDITED_USER','CREATED_USER','CREATED_DATE']
        if int(fcCount[0]) == 0:
            arcpy.AddMessage("No features in "+fc+" ... skipping!")
            pass
        else:
            # Find duplicate geometry
            flds = arcpy.ListFields(fc)
            fldNames = []
            for fld in flds:
                if fld.type not in ignoreType:
                    if fld.name.lower() not in [x.lower() for x in ignoreFld]:
                        fldNames.append(str(fld.name))
                    
                #if fld.name.lower() not in [x.lower() for x in ignoreFLD]:
            dupeTable = "in_memory\\tmp"
            arcpy.FindIdentical_management(fc, dupeTable, fldNames,xy_tolerance= xyTol, z_tolerance = zTol, output_record_option="ONLY_DUPLICATES")
            
            # Get table count and pass the dataset if no duplicates exist
            fidList=[]
            with arcpy.da.SearchCursor(dupeTable,["IN_FID"]) as cursor:
                    for row in cursor:
                        fidList.append(row[0])
            #expression = 'OBJECTID IN ({0})'.format(', '.join(map(str, fidList)) or 'NULL')
            tblCount = arcpy.GetCount_management(dupeTable)
            
            uniqdupCount = len(unique_values(dupeTable , "FEAT_SEQ"))
            dupCount = len(unique_values(dupeTable , "IN_FID"))

            fidList.sort()
            FIDs =  ', '.join(map(str, fidList))
                
            if int(tblCount[0]) == 0:
                arcpy.AddMessage("No duplicate features found in " + fc)
                continue
            else:
                arcpy.AddMessage("Deleting "+ str(dupCount) +" duplicates across "+str(uniqdupCount)+" features in " + fc)
                arcpy. DeleteIdentical_management (fc, fldNames, xy_tolerance=xyTol, z_tolerance=zTol)
            arcpy.Delete_management("in_memory\\tmp") 
