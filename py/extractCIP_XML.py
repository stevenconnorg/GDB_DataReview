#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      Marie Cline Delgado
#
#-------------------------------------------------------------------------------

import arcpy, os, time

timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
arcpy.GetMessage("Start time: " + timestamp)

# Variables
inGDB = arcpy.GetParameterAsText(0) # GDB to extract CIP from
name = arcpy.GetParameterAsText(1) # Installation name - string, no spaces
path = arcpy.GetParameterAsText(2) # Output location - folder directory
xmlWorkspace = arcpy.GetParameterAsText(3) # XML Shell Document - file variable
name = str(name+".gdb").replace(" ","_")

# Create CIP shell with empty GDB and XML Workspace Document
arcpy.GetMessage("Creating empty FGDB")
arcpy.CreateFileGDB_management(path, name)
arcpy.GetMessage("Importing XML schema into FGDB")
arcpy.ImportXMLWorkspaceDocument_management(name, xmlWorkspace, "SCHEMA_ONLY", "DEFAULTS")
cipLoc = os.path.join(path,name)

arcpy.env.workspace = inGDB # Location of GDB to extract CIP from

CIP_Datasets = ('Auditory', 'Cadastre', 'environmentalCulturalResources', 'environmentalNaturalResources', 'environmentalRestoration', 'MilitaryRangeTraining', 'Pavements',
                'Planning', 'RealProperty', 'Recreation', 'Security', 'Transportation', 'WaterWays')

CIP_Layers = ('NoiseZone_A', 'Installation_A', 'LandParcel_A', 'Outgrant_A', 'Site_A', 'Site_P', 'HistoricDistrict_A', 'Wetland_A', 'EnvRemediationSite_A', 'ImpactArea_A',
              'MilQuantityDistCombinedArc_A', 'MilRange_A', 'MilTrainingLoc_A', 'PavementBranch_A', 'PavementSection_A', 'AirAccidentZone_A', 'LandUse_A', 'Building_A',
              'Tower_P', 'GolfCourse_A', 'RecArea_A', 'AccessControl_L', 'AccessControl_P', 'Fence_L', 'Bridge_A', 'Bridge_L', 'RailSegment_L', 'RailTrack_L', 'RoadCenterline_L',
              'RoadPath_L', 'RoadSeg_L', 'VehicleParking_A', 'DocksAndWharfs_A', 'Test_A')

CIP_RP = ('Building_A', 'DocksAndWharfs_A', 'Fence_L', 'GolfCourse_A', 'LandParcel_A', 'PavementBranch_A', 'PavementSection_A', 'RailSegment_L', 'RailTrack_L',
          'RoadCenterline_L', 'Tower_P')

CIP_RPUID = ('Building_A', 'Tower_P')

CIP_RPUIdentifier = ('DocksAndWharfs_A', 'Fence_L', 'GolfCourse_A', 'LandParcel_A', 'PavementBranch_A', 'PavementSection_A', 'RailSegment_L', 'RailTrack_L', 'RoadCenterline_L')

datasets = arcpy.ListDatasets()
for ds in datasets:
    dsName = os.path.basename(ds)
    if dsName not in CIP_Datasets:
        pass
    else:
        fClass = arcpy.ListFeatureClasses("*", "All", dsName)
        for fc in fClass:
            fcName = os.path.basename(fc)
            if fcName not in CIP_Layers:
                pass
            else:
                arcpy.MakeFeatureLayer_management(inGDB + "/" + dsName + "/" + fcName, fcName + "_lyr")
                count = int(arcpy.GetCount_management(fcName + "_lyr").getOutput(0))
                if count == 0:
                    arcpy.GetMessage("No features in CIP layer " + fcName + " to append")
                    pass
                else:
                    if fcName in CIP_RP:
                        if fcName in CIP_RPUID:
                            field_names = [field.name.lower() for field in arcpy.ListFields(fcName)]
                            if "realpropertyuniqueid" in field_names:
                                arcpy.GetMessage("***CORRECT RPUID FIELD EXISTS FOR " + fcName + "***")
                                pass
                            else:
                                arcpy.GetMessage("***RPUID FIELD ADDED BY GEOBASE; INSTALLATION STILL NEEDS TO BE MADE AWARE OF ERROR FOR " + fcName + "***")
                                arcpy.AddField_management(inGDB + "/" + dsName + "/" + fcName, "realPropertyUniqueID", "TEXT","","", "20","realPropertyUniqueID","","","")
                            if "realpropertyuniqueidentifier" in field_names:
                                arcpy.GetMessage("***NULLS COULD EXIST--BUT CALCULATED RPUID FROM RPUIdentifier FIELD WHERE RPUID = NULL***")
                                where = '"realPropertyUniqueID" IS NULL'
                                arcpy.SelectLayerByAttribute_management(fcName + "_lyr", "NEW_SELECTION", where)
                                arcpy.CalculateField_management(fcName + "_lyr", "realPropertyUniqueID", "!realPropertyUniqueIdentifier!","PYTHON","")
                                arcpy.SelectLayerByAttribute_management(fcName + "_lyr", "CLEAR_SELECTION", "")
                            else:
                                arcpy.GetMessage("***NULLS COULD EXIST--NO RPUIdentifier FIELD EXISTS FOR CALCULATION OF NULL RPUID FIELDS***")
                                pass
                        elif fcName in CIP_RPUIdentifier:
                            fields_names = [fields.name.lower() for fields in arcpy.ListFields(fcName)]
                            if "realpropertyuniqueidentifier" in fields_names:
                                arcpy.GetMessage("***CORRECT RPUIdentifier FIELD EXISTS FOR " + fcName + "***")
                                pass
                            else:
                                arcpy.GetMessage("***RPUIdentifier FIELD ADDED BY GEOBASE; INSTALLATION STILL NEEDS TO BE MADE AWARE OF ERROR FOR " + fcName + "***")
                                arcpy.AddField_management(inGDB + "/" + dsName + "/" + fcName, "realPropertyUniqueIdentifier", "TEXT","","", "18","realPropertyUniqueIdentifier","","","")
                            if "realpropertyuniqueid" in fields_names:
                                arcpy.GetMessage("***NULLS COULD EXIST--BUT CALCULATED RPUIdentifier FROM RPUID FIELD WHERE RPUIdentifier = NULL***")
                                where1 = '"realPropertyUniqueIdentifier" IS NULL'
                                arcpy.SelectLayerByAttribute_management(fcName + "_lyr", "NEW_SELECTION", where1)
                                arcpy.CalculateField_management(fcName + "_lyr", "realPropertyUniqueIdentifier", "!realPropertyUniqueID!","PYTHON","")
                                arcpy.SelectLayerByAttribute_management(fcName + "_lyr", "CLEAR_SELECTION", "")
                            else:
                                arcpy.GetMessage("***NULLS COULD EXIST--NO RPUID FIELD EXISTS FOR CALCULATION OF NULL RPUIdentifier FIELDS***")
                                pass
                        else:
                            pass
                    else:
                        pass
                    arcpy.env.workspace = cipLoc
                    destDS = arcpy.ListDatasets()
                    for d in destDS:
                        destDSname = os.path.basename(d)
                        destFC = arcpy.ListFeatureClasses("*", "All", destDSname)
                        for f in destFC:
                            fname = os.path.basename(f)
                            if fcName == fname:
                                arcpy.GetMessage("Appending " + str(count) + " features from " + dsName + " dataset, " + fcName + " feature class to the " + fname + " feature class in the " + destDSname + " dataset in the " + name)
                                arcpy.Append_management(fcName + "_lyr", cipLoc + "/" + destDSname + "/" + fname, "NO_TEST","","")
                                arcpy.Delete_management(fcName + "_lyr")
                                arcpy.env.workspace = inGDB
                            else:
                                pass

timestamp_end = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
arcpy.GetMessage("End time: " + timestamp_end)
