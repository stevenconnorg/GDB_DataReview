# -*- #################
"""
Created on Thu Apr 26 11:15:52 2018

@author: stevenconnorg # 
"""

import arcpy, os
#Get path to the geodatabase
features = arcpy.GetParameterAsText(0)
outputGDB = arcpy.GetParameterAsText(1)
repairGeom = arcpy.GetParameterAsText(2)
deleteNull = arcpy.GetParameterAsText(3)
outputDir = arcpy.Describe(outputGDB).path


def get_geodatabase_path(input_table):
  '''Return the Geodatabase path from the input table or feature class.
  :param input_table: path to the input table or feature class 
  '''
  workspace = os.path.dirname(input_table)
  if [any(ext) for ext in ('.gdb', '.mdb', '.sde') if ext in os.path.splitext(workspace)]:
    return workspace
  else:
    return os.path.dirname(workspace)

gdbPath = get_geodatabase_path(features[0])

# Workspace
arcpy.env.workspace = gdbPath
arcpy.env.overwriteOutput = True

# Find duplicate geometry
arcpy.CheckGeometry_management (features, os.path.join(outputGDB,"geomCheck"))

if repairGeom:
    arcpy.AddMessage("Repairing geometries...")
    if deleteNull:
        arcpy.AddMessage("...Deleting null geometries!")
        arcpy.RepairGeometry_management (features,"DELETE_NULL")
    else:
        arcpy.AddMessage("...Keeping null geometries!")
        arcpy.RepairGeometry_management (features,"KEEP_NULL")
else:
    pass


