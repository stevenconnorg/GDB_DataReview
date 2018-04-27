# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:46:58 2018

@author: stevenconnorg
"""
import arcpy 

gdb = arcpy.GetParameterAsText(0)
inMetadataDir = arcpy.GetParameterAsText(1)
importType = arcpy.GetParameterAsText(2) # "FROM_FGDC"
autoUpdate = arcpy.GetParameterAsText(3) # "ENABLED"

FDSs = arcpy.ListDatasets(gdb)

if not FDSs:
    FCs = arcpy.ListFeatureClasses(gdb)
    for fc in FCs:
        arcpy.ImportMetadata_conversion(Source_Metadata = inMetadataDir+"/"+fc+".xml", Import_Type=importType, Target_Metadata = fc, Enable_automatic_updates=autoUpdate)


for fds in FDSs:
    arcpy.ImportMetadata_conversion(inMetadataDir+"/"+fds+".xml", Import_Type=importType, Target_Metadata = fc, Enable_automatic_updates=autoUpdate)
    FCs = arcpy.ListFeatureClasses(feature_dataset=fds)
    for fc in FCs:        
        arcpy.ImportMetadata_conversion(inMetadataDir+"/"+fds+"_"+fc+".xml", Import_Type=importType, Target_Metadata = fc, Enable_automatic_updates=autoUpdate)

