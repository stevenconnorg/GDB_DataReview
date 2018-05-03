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


gdb = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\dat\gdbs-complete\Example.gdb"
inMetadataDir = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\out\metadata"
importType = "FROM_FGDC"
autoUpdate = "ENABLED"

arcpy.env.workspace = gdb
FDSs = arcpy.ListDatasets()

if not FDSs:
    print "not fds"
    FCs = arcpy.ListFeatureClasses()
    for fc in FCs:
        inFile = glob.glob(inMetadataDir+"/"+fc+"*")
        if not inFile:
                arcpy.AddMessage("No metadata found for "+ fc + "...skipping!")
        else:
            arcpy.AddMessage("Importing "+os.path.basename(inFile[0])+" to "+ fc)
            arcpy.ImportMetadata_conversion(Source_Metadata = inFile[0], Import_Type=importType, Target_Metadata = os.path.join(gdb,fc), Enable_automatic_updates=autoUpdate)

else:
    for fds in FDSs:
        print fds
        inFile = glob.glob(inMetadataDir+"/"+fds+".xml")
        if not inFile:
                arcpy.AddMessage("No metadata found for "+ fds + "...skipping!")
        else:
            arcpy.AddMessage("Importing "+os.path.basename(inFile[0])+" to "+ fds)
            arcpy.ImportMetadata_conversion(inFile[0], Import_Type=importType, Target_Metadata = os.path.join(gdb,fds), Enable_automatic_updates=autoUpdate)
        FCs = arcpy.ListFeatureClasses(feature_dataset=fds)
        for fc in FCs:        
            inFile = glob.glob(inMetadataDir+"/"+"*"+fc+"*")
            if not inFile:
                arcpy.AddMessage("No metadata found for "+ fc + "...skipping!")
            else:
                arcpy.AddMessage("Importing "+os.path.basename(inFile[0])+" to "+ fc)
                arcpy.ImportMetadata_conversion(Source_Metadata = inFile[0],  Target_Metadata = os.path.join(gdb,fds,fc), Enable_automatic_updates=autoUpdate)
# Import_Type=importType,