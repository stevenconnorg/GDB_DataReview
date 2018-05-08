# -*- #################
"""
Created on Mon Apr 23 12:59:28 2018

@author: stevenconnorg
"""

import arcpy, os, sys
from arcpy import env
env.overwriteOutput = True

# source feature
gdb =arcpy.GetParameterAsText(0)
siteA =arcpy.GetParameterAsText(1)
# source RPSUID field
sourceRPSUID =arcpy.GetParameterAsText(2)

targetFDSWildcard =arcpy.GetParameterAsText(3)

targetFCWildcard =arcpy.GetParameterAsText(4)

targetFieldWildcard =arcpy.GetParameterAsText(5)

overlap_type=arcpy.GetParameterAsText(6)

searchDistance =arcpy.GetParameterAsText(7)

def unique_values(table , field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({str(row[0]) for row in cursor})


RPSUIDs = unique_values(siteA,sourceRPSUID)
arcpy.env.workspace = gdb

theFDSs = list(arcpy.ListDatasets(wild_card=targetFDSWildcard))
arcpy.AddMessage("Starting loop")

if len(theFDSs) == 0:
    arcpy.AddError("Zero feature datasets found in " + gdb+" using targetFDSWildcard = "+targetFDSWildcard+". \n Try migrating your feature classes to a feature datasets or alter your targetFDSWildcard value.")
    sys.exit(0)
else:
    for fds in theFDSs:
        theFCs = list(arcpy.ListFeatureClasses(wild_card = targetFCWildcard,feature_dataset=fds))
        if len(theFCs) == 0:    
            arcpy.AddMessage("Zero feature classes found in feature dataset " + fds+" using targetFCWildcard = "+targetFCWildcard+ " ...skipping! \n Try migrating your feature classes to a feature datasets or alter your targetFDSWildcard value.")
            pass
        else:
            for fc in theFCs:
                if arcpy.GetCount_management(fc) == 0:
                    arcpy.AddMessage("Zero features found in " + fds+"/"+fc +" ...skipping!")
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
                            if overlap_type in ["WITHIN_A_DISTANCE_GEODESIC", "WITHIN_A_DISTANCE", "WITHIN_A_DISTANCE_3D", "INTERSECT", "INTERSECT_3D", "HAVE_THEIR_CENTER_IN", "CONTAINS", "WITHIN"]:
                                if len(searchDistance) == 0:
                                    arcpy.AddError("You must supply a Search Distance value for overlap type "+ overlap_type+"! Try again")
                                    sys.exit(0)
                                else:
                                    arcpy.SelectLayerByLocation_management (targetLayer, overlap_type=overlap_type,select_features="in_memory\\source",selection_type="NEW_SELECTION",search_distance=searchDistance)
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
                            else:
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