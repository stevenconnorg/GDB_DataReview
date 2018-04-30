# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:59:28 2018

@author: stevenconnorg
"""

import arcpy, os
from arcpy import env
env.overwriteOutput = True

# input geodatabase
gdb =arcpy.GetParameterAsText(0)

# source feature
siteA =arcpy.GetParameterAsText(1)
# source RPSUID field
sourceRPSUID =arcpy.GetParameterAsText(2)

targetFDSWildcard =arcpy.GetParameterAsText(3)

targetFCWildcard =arcpy.GetParameterAsText(4)

targetFieldWildcard =arcpy.GetParameterAsText(5)

overlap_type=arcpy.GetParameterAsText(6)


def unique_values(table , field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({str(row[0]) for row in cursor})


RPSUIDs = unique_values(siteA,sourceRPSUID)
arcpy.env.workspace = gdb

theFDSs = list(arcpy.ListDatasets(wild_card=targetFDSWildcard))
arcpy.AddMessage("Starting loop")
for fds in theFDSs:
    theFCs = list(arcpy.ListFeatureClasses(wild_card = targetFCWildcard,feature_dataset=fds))
    for fc in theFCs:
        if arcpy.GetCount_management(fc) == 0:
            pass
        else:
            for RPSUID in RPSUIDs:
                sourceLayer = "siteLayer_"+RPSUID
                arcpy.MakeFeatureLayer_management(siteA,sourceLayer)
                arcpy.SelectLayerByAttribute_management (sourceLayer,"NEW_SELECTION", where_clause=sourceRPSUID+" = '"+RPSUID+"'")
                arcpy.CopyFeatures_management(sourceLayer,"in_memory\\source")
                arcpy.AddMessage( sourceRPSUID+" = '"+RPSUID+"'")
                with arcpy.da.SearchCursor("in_memory\\source", sourceRPSUID) as cursor:
                    targetLayer = "pointFC"+RPSUID
                    if arcpy.Exists(targetLayer):   
                        arcpy.Delete_management(targetLayer)
                    arcpy.MakeFeatureLayer_management(os.path.join(gdb,fds,fc),targetLayer)
                    arcpy.SelectLayerByLocation_management (targetLayer, overlap_type=overlap_type,select_features="in_memory\\source",selection_type="NEW_SELECTION")
                    for fld in arcpy.ListFields(targetLayer,wild_card=targetFieldWildcard):
                        with arcpy.da.UpdateCursor(targetLayer, fld.name) as cursor2:
                            for row in cursor:
                                for row2 in cursor2:
                                    arcpy.AddMessage( "Updating "+fc+"/"+fld.name+" from "+ row2[0]+" to "+row[0])
                                    row2[0] = row[0]
                                    cursor2.updateRow(row2)
                                    del row2   
                                del row          
                            del cursor
                        del cursor2 
                        arcpy.Delete_management(sourceLayer)
                        arcpy.Delete_management("in_memory\\source")
                        del sourceLayer
                    arcpy.Delete_management(targetLayer)
                    del targetLayer
