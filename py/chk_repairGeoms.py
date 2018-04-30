#-------------------------------------------------------------------------------
# Name:           Check and Repair Geometry Errors
# Purpose:        Check datasets for geometry errors.  Repair if found.  Recheck
#                 after repair is complete.
# Author:         Marie Cline Delgado
#
# Created:        
# Last updated:
#-------------------------------------------------------------------------------

import arcpy, os

#Get path to the geodatabase
workpath = arcpy.GetParameterAsText(0)
outputGDB = arcpy.GetParameterAsText(1)
repairGeom = arcpy.GetParameterAsText(2)
deleteNull = arcpy.GetParameterAsText(3)

#Workspace
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True

#Variables
fcsAll = []
fcsRepair = []
outTable = "CheckGeometry"
outTablePath = os.path.join(outputGDB, outTable)

#Build list of feature classes to test for valid geometry
for dataset in arcpy.ListDatasets():
    fcsAll += arcpy.ListFeatureClasses('*','',dataset)

#Check geometry
print("Running the check geometry tool on {} feature classes".format(len(fcsAll)))
arcpy.AddMessage("Running the check geometry tool on {} feature classes".format(len(fcsAll)))
arcpy.CheckGeometry_management(fcsAll, outTablePath)

geoErrorCount = arcpy.GetCount_management(outTablePath)[0]
print("{} geometry problems found, results table at {}.".format(geoErrorCount,outTablePath))
arcpy.AddMessage("{} geometry problems found, results table at {}.".format(geoErrorCount,outTablePath))

#Release lock
arcpy.ClearWorkspaceCache_management()

if geoErrorCount > 0:
    #Loop through Geometry Error Table to get list of feature needing repair
    for row in arcpy.da.SearchCursor(outTablePath, ('CLASS')):
        if not row[0] in fcsRepair:
            fcsRepair.append(row[0])

    #Loop through the repair list
    print("> Processing {0} feature classes".format(len(fcsRepair)))
    arcpy.AddMessage("> Processing {0} feature classes".format(len(fcsRepair)))
    for fc in fcsRepair:
        print("Processing " + fc)
        arcpy.AddMessage("Processing " + fc)
        lyr = 'temporary_layer'
        if arcpy.Exists(lyr):
            arcpy.Delete_management(lyr)

        tblVw = "checkGeomTblView"
        if arcpy.Exists(tblVw):
            arcpy.Delete_management(tblVw)

        arcpy.MakeTableView_management(outTablePath, tblVw, ("\"CLASS\" = '%s'" % fc))
        arcpy.MakeFeatureLayer_management(fc, lyr)
        arcpy.AddJoin_management(lyr, arcpy.Describe(lyr).OIDFieldName, tblVw, "FEATURE_ID")
        arcpy.CopyFeatures_management(lyr, fc+"_bad_geom")
        arcpy.RemoveJoin_management(lyr, outTable)
        if repairGeom:
            arcpy.AddMessage("Repairing geometries...")
            if deleteNull:
                arcpy.AddMessage("...Deleting null geometries!")
                arcpy.RepairGeometry_management (lyr,"DELETE_NULL")
            else:
                arcpy.AddMessage("...Keeping null geometries!")
                arcpy.RepairGeometry_management (lyr,"KEEP_NULL")

if len(fcsRepair) > 0:
    #Recheck Geometry after repair
    arcpy.CheckGeometry_management(fcsRepair, outTablePath+"2")
    print("Re-checking geometry tool on {} feature classes".format(len(fcsRepair)))
    arcpy.AddMessage("Re-checking geometry tool on {} feature classes".format(len(fcsRepair)))
    
    #Recount geometry errors after geometry repair
    geoErrorRecount = arcpy.GetCount_management(outTablePath+"2")[0]
    print("{} geometry problems found, results table at {}.".format(geoErrorRecount,outTablePath+"2"))
    arcpy.AddMessage("{} geometry problems found, results table at {}.".format(geoErrorRecount,outTablePath+"2"))