# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 09:09:49 2018

@author: stevenconnorg
"""

# -*- #################
"""
Created on Thu Apr 26 11:15:52 2018

@author: stevenconnorg
"""

import arcpy
#Get path to the geodatabase
workpath = arcpy.GetParameterAsText(0)
clipFeat = arcpy.GetParameterAsText(1)
clusterTolerance = arcpy.GetParameterAsText(2)
clippedGDB = arcpy.GetParameterAsText(3)
# Workspace
arcpy.env.workspace = workpath
arcpy.env.overwriteOutput = True


for fds in arcpy.ListDatasets():  
    arcpy.CreateFeatureDataset_management (out_dataset_path=clippedGDB, out_name=fds, spatial_reference=fds)
    for fc in arcpy.ListFeatureClasses('','',fds):


        # Get table count and pass the dataset if no duplicates exist
        fcCount = arcpy.GetCount_management(fc)
        if int(fcCount[0]) == 0:
            arcpy.AddMessage("No features found in "+fc+ " ... skipping!")
            pass

        else:
            inLayer = fc+"_lyr"
            clipLayer = clipFeat+"_lyr"
            arcpy.MakeFeatureLayer_management(fc,clipLayer)
            arcpy.MakeFeatureLayer_management(fc,inLayer)
            arcpy.AddMessage("Clipping "+ fc+ " to " + clipFeat + " with "+clusterTolerance+" cluster tolerance!")
            arcpy.Clip_analysis(in_features = clipLayer, clip_features = inLayer, out_feature_class = clippedGDB+"/"+fds+"/"+fc, cluster_tolerance = clusterTolerance)



