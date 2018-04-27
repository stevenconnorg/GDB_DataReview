# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:39:46 2018

@author: stevenconnorg
"""

import arcpy

gdb = arcpy.GetParameterAsText(0)
translator = arcpy.GetParameterAsText(1)
outDir = arcpy.GetParameterAsText(2)

# =============================================================================
# gdb = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\CIP_DataReview\archive\ANG_Peoria  - Copy\Non_Network_CIP\ANG_Peoria_CIP.gdb"
# translator = r"C:\Program Files (x86)\ArcGIS\Desktop10.6\Metadata\Translator\ARCGIS2FGDC.xml"
# outDir = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\CIP_DataReview\archive\ANG_Peoria  - Copy\Non_Network_CIP\METADATA"
# 
# =============================================================================
arcpy.env.workspace = gdb

FDSs = arcpy.ListDatasets()
arcpy.AddMessage(FDSs)

if not FDSs:
    FCs = arcpy.ListFeatureClasses(gdb)
    for fc in FCs:
        outFile = outDir+"/"+fc+".xml"
        if arcpy.Exists(outFile):
            arcpy.Delete_management(outFile)
        arcpy.ExportMetadata_conversion(fc,Translator = translator,Output_File = outDir+"/"+fc+".xml")
else:
    for fds in FDSs:
        outFile = outDir+"/"+fds+".xml"
        if arcpy.Exists(outFile):
            arcpy.Delete_management(outFile)
        arcpy.ExportMetadata_conversion(fds,Translator = translator,Output_File = outFile)
        FCs = arcpy.ListFeatureClasses(feature_dataset = fds)
        for fc in FCs:   
            outFile = outDir+"/"+fds+"_"+fc+".xml"
            if arcpy.Exists(outFile):
                arcpy.Delete_management(outFile)
            arcpy.ExportMetadata_conversion(fc,Translator = translator,Output_File = outFile)
