# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:59:28 2018

@author: stevenconnorg
"""
# for use in an ArcMap Toolbox	
	
# alternative tool to using join with field calculator to update records	
# updates a target feature class using a join with a source table	
# requires two join fields	
# and a target field and update field	
	
# params #	
# 1 
# 2
# 3
# 4


import arcpy, os, csv, pandas as pd
from arcpy import env
env.overwriteOutput = True

gdb = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\CIP_DataReview\installation_archives\ANG_Peoria  - Copy\Non_Network_CIP\ANG_Peoria_CIP.gdb"


        
# source feature
siteA = os.path.join(gdb,"Cadastre","Site_A")
# source RPSUID field
sourceRPSUID = "realPropertySiteUniqueID"

targetFieldWildcard = "realPropertySiteUnique*"

overlap_type="WITHIN"


gdb =arcpy.GetParameterAsText(0)

targetFDSWildcard =arcpy.GetParameterAsText(1)

targetFCWildcard =arcpy.GetParameterAsText(2)

targetFieldWildcard =arcpy.GetParameterAsText(3)


def unique_values(table , field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({str(row[0]) for row in cursor})


arcpy.env.workspace = gdb

theFDSs = list(arcpy.ListDatasets(wild_card=targetFDSWildcard))
arcpy.AddMessage("Starting loop")
for fds in theFDSs:
    theFCs = list(arcpy.ListFeatureClasses(wild_card = targetFCWildcard,feature_dataset=fds))
    for fc in theFCs:
        if arcpy.GetCount_management(fc) == 0:
            pass
        else:
            minFields = (fld.name for fld in arcpy.ListFields(os.path.join(gdb,fds,fc)) if fld.name not in ['Shape', 'OBJECTID', 'Shape_Length', 'Shape_Area'])
            
            arcpy.ListFields()
            arcpy.DeleteIdentical_management (os.path.join(gdb,fds,fc), minFields) 


