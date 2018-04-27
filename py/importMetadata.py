# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:46:58 2018

@author: stevenconnorg
"""
import arcpy , glob, os

gdb = arcpy.GetParameterAsText(0)
inMetadataDir = arcpy.GetParameterAsText(1)
importType = arcpy.GetParameterAsText(2) # "FROM_FGDC"
autoUpdate = arcpy.GetParameterAsText(3) # "ENABLED"


gdb = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\CIP_DataReview\archive\ANG_Peoria  - Copy\Non_Network_CIP\ANG_Peoria_CIP.gdb"
inMetadataDir = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\CIP_DataReview\archive\ANG_Peoria  - Copy\Non_Network_CIP\METADATA"
importType = "FROM_FGDC"
autoUpdate = "ENABLED"

arcpy.env.workspace = gdb
FDSs = arcpy.ListDatasets()

if not FDSs:
    FCs = arcpy.ListFeatureClasses(feature_dataset=gdb)
    for fc in FCs:
        inFile = glob.glob(inMetadataDir+"/"+fc+"*")[0]
        arcpy.ImportMetadata_conversion(Source_Metadata = inFile, Import_Type=importType, Target_Metadata = os.path.join(gdb,fc), Enable_automatic_updates=autoUpdate)

for fds in FDSs:
    inFile = glob.glob(inMetadataDir+"/"+fds+".xml")[0]
    arcpy.ImportMetadata_conversion(inFile, Import_Type=importType, Target_Metadata = fc, Enable_automatic_updates=autoUpdate)
    FCs = arcpy.ListFeatureClasses(feature_dataset=fds)
    for fc in FCs:        
        inFile = glob.glob(inMetadataDir+"/"+"*"+fc+"*")[0]
        arcpy.ImportMetadata_conversion(Source_Metadata = inFile,  Target_Metadata = os.path.join(gdb,fds,fc), Enable_automatic_updates=autoUpdate)

# Import_Type=importType,