# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:46:58 2018

@author: stevenconnorg
"""
import arcpy , os

targetGDB = arcpy.GetParameterAsText(0)
sourceGDB = arcpy.GetParameterAsText(1)
importType = arcpy.GetParameterAsText(2) # "FROM_ARCGIS"
autoUpdate = arcpy.GetParameterAsText(3) # "ENABLED"


targetGDB = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\DataPackage\NEW_CIP\GeoBASE_3101_CIP_FINAL_20180502.gdb"
sourceGDB = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\DataPackage\OLD_CIP_GOOD_M\GeoBASE_3101_CIP_FINAL_2017.gdb"
importType = "FROM_ARCGIS"
autoUpdate = "ENABLED"
#image = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\DataPackage\thumbnail.
arcpy.env.workspace = targetGDB
FDSs = arcpy.ListDatasets()
arcpy.ImportMetadata_conversion(Source_Metadata = sourceGDB, Import_Type=importType, Target_Metadata = targetGDB, Enable_automatic_updates=autoUpdate)

if not FDSs:
    print "not fds"
    FCs = arcpy.ListFeatureClasses()
    if not FCs:
        print("No feature classes found in "+os.path.join(sourceGDB)+" to import!")
    else:
        for fc in FCs:
            if arcpy.Exists(os.path.join(sourceGDB,fc)):
                print("Importing "+os.path.join(sourceGDB,fc)+" to "+ fc)
                arcpy.ImportMetadata_conversion(Source_Metadata = os.path.join(sourceGDB,fc), Import_Type=importType, Target_Metadata = os.path.join(targetGDB,fc), Enable_automatic_updates=autoUpdate)
            else:
                print("No metadata found for "+ fc + "...skipping!")
else:
    for fds in FDSs:
        print fds
        if arcpy.Exists( os.path.join(sourceGDB,fds)):
            print("Importing "+ os.path.join(sourceGDB,fds)+" to "+ fds)
            arcpy.ImportMetadata_conversion( os.path.join(sourceGDB,fds), Import_Type=importType, Target_Metadata = os.path.join(targetGDB,fds), Enable_automatic_updates=autoUpdate)
            FCs = arcpy.ListFeatureClasses(feature_dataset=fds)
            if not FCs:
                print("No feature classes found in "+os.path.join(sourceGDB,fds)+" to import!")
            else:
                for fc in FCs:   
                    if arcpy.Exists(os.path.join(sourceGDB,fds,fc)):
                        print("Importing "+os.path.join(sourceGDB,fds,fc)+" to "+ fc)
                        arcpy.ImportMetadata_conversion(Source_Metadata =os.path.join(sourceGDB,fds,fc),  Target_Metadata = os.path.join(targetGDB,fds,fc), Enable_automatic_updates=autoUpdate)
                    else:
                        print("No metadata found for "+ fc + "...skipping!")
        else:
            print("No metadata found for "+ fds + "...skipping!")

       
                
