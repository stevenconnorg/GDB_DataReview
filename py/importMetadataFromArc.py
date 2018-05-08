# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:46:58 2018

@author: stevenconnorg
"""
import arcpy , os

sourceGDB = arcpy.GetParameterAsText(0)
targetGDB = arcpy.GetParameterAsText(1)
syncType = arcpy.GetParameterAsText(2)#"ALWAYS"
# =============================================================================
# importType = arcpy.GetParameterAsText(2) # "FROM_ARCGIS"
# autoUpdate = arcpy.GetParameterAsText(3) # "ENABLED"
# 
# 
# targetGDB = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\DataPackage\NEW_CIP\GeoBASE_3101_CIP_FINAL_20180502.gdb"
# sourceGDB = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\DataPackage\NEW_CIP\GeoBASE_3101_CIP_FINAL_with_metadata.gdb"
# importType = "FROM_ARCGIS"
# autoUpdate = "ENABLED"
# 
# 
# =============================================================================
#image = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\AF_Installation_Feedback\DataPackage\thumbnail.
arcpy.env.workspace = targetGDB
FDSs = arcpy.ListDatasets()
arcpy.MetadataImporter_conversion(source =  sourceGDB, target = targetGDB)

if not FDSs:
    FCs = arcpy.ListFeatureClasses()
    if not FCs:
        arcpy.AddMessage("No feature classes found in "+os.path.join(sourceGDB)+" to import!")
    else:
        for fc in FCs:
            if arcpy.Exists(os.path.join(sourceGDB,fc)):
                arcpy.AddMessage("Importing "+os.path.join(sourceGDB,fc)+" to "+ fc)
                arcpy.MetadataImporter_conversion(source =  os.path.join(sourceGDB,fc), target = os.path.join(targetGDB,fc))
                arcpy.SynchronizeMetadata_conversion (source = os.path.join(targetGDB,fc), synctype=syncType )
                #arcpy.ImportMetadata_conversion(Source_Metadata = os.path.join(sourceGDB,fc), Import_Type=importType, Target_Metadata = os.path.join(targetGDB,fc), Enable_automatic_updates=autoUpdate)
            else:
                arcpy.AddMessage("No metadata found for "+ fc + "...skipping!")
else:
    for fds in FDSs:
        if arcpy.Exists( os.path.join(sourceGDB,fds)):
            arcpy.AddMessage("Importing "+ os.path.join(sourceGDB,fds)+" to "+ fds)
            arcpy.MetadataImporter_conversion(source =  os.path.join(sourceGDB,fds), target = os.path.join(targetGDB,fds))
            arcpy.SynchronizeMetadata_conversion (source = os.path.join(targetGDB,fds), synctype=syncType )
            #arcpy.ImportMetadata_conversion( os.path.join(sourceGDB,fds), Import_Type=importType, Target_Metadata = os.path.join(targetGDB,fds), Enable_automatic_updates=autoUpdate)
            FCs = arcpy.ListFeatureClasses(feature_dataset=fds)
            if not FCs:
                arcpy.AddMessage("No feature classes found in "+os.path.join(sourceGDB,fds)+" to import!")
            else:
                for fc in FCs:   
                    if arcpy.Exists(os.path.join(sourceGDB,fds,fc)):
                        arcpy.AddMessage("Importing "+os.path.join(sourceGDB,fds,fc)+" to "+ fc)
                        arcpy.MetadataImporter_conversion(source =  os.path.join(sourceGDB,fds,fc), target = os.path.join(targetGDB,fds,fc))
                        arcpy.SynchronizeMetadata_conversion (source = os.path.join(targetGDB,fds,fc), synctype=syncType)
                        #arcpy.ImportMetadata_conversion(Source_Metadata =os.path.join(sourceGDB,fds,fc),  Target_Metadata = os.path.join(targetGDB,fds,fc), Enable_automatic_updates=autoUpdate)
                    else:
                        arcpy.AddMessage("No metadata found for "+ fc + "...skipping!")
        else:
            arcpy.AddMessage("No metadata found for "+ fds + "...skipping!")

       
                
