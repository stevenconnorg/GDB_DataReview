#-------------------------------------------------------------------------------
# Name:        Create Site Data
# Purpose:     Create Site Areas and Site Points from Installation Area
# 
# Author:      Marie Cline Delgado
#
# Created:     04/30/2018
# Last update: 05/02/2018
#
# ArcToolbox Configuration:
#              Highly advised that background processing is disabled when configuring
#              this tool.  The tool provides messages and warnings that should be 
#              included in the CIP processing notes.               
#-------------------------------------------------------------------------------

import arcpy, os

# Location variable
cadDS = arcpy.GetParameterAsText(0)
instAreaFC = "Installation_A"
siteAreaFC = "Site_A"
sitePtFC = "Site_P"

# Bypass Installation_A and Site_A geometry compare to create Site_P from existing Site_A features
bypassInstA = arcpy.GetParameterAsText(1) # default to false

# Spatial selection type when comparing geometry of Installation_A and Site_A
sblOverlapType = arcpy.GetParameterAsText(2) # default to "HAVE_THEIR_CENTER_IN"

# Workspace variables
arcpy.env.workspace = cadDS
arcpy.env.overwriteOutput = True

def createSiteP():
    # Site_P is empty
    if int(arcpy.GetCount_management(os.path.join(cadDS,sitePtFC))[0]) == 0:
        arcpy.MakeFeatureLayer_management(os.path.join(cadDS,siteAreaFC), 'Site_Alyr')
        tempSiteP = arcpy.FeatureToPoint_management('Site_Alyr', "in_memory\\tmp", "INSIDE")
        arcpy.Append_management(tempSiteP, sitePtFC, "NO_TEST")
        arcpy.AddMessage("{} Site points created for empty Site_P".format(arcpy.GetCount_management(tempSiteP)[0]))
    # Site_P contains data
    elif int(arcpy.GetCount_management(os.path.join(cadDS,sitePtFC))[0]) > 0:
        arcpy.MakeFeatureLayer_management(os.path.join(cadDS,siteAreaFC), 'Site_Alyr')
        # Select polygons that do not contain a point
        siteAselection = arcpy.SelectLayerByLocation_management('Site_Alyr', "COMPLETELY_CONTAINS", os.path.join(cadDS,sitePtFC), selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")
        if int(arcpy.GetCount_management(siteAselection)[0]) > 0:
            tempSiteP = arcpy.FeatureToPoint_management(siteAselection, "in_memory\\tmp", "INSIDE")
            arcpy.Append_management(tempSiteP, sitePtFC, "NO_TEST")
            arcpy.AddMessage("{} Additional site points created and appended to Site_P".format(arcpy.GetCount_management(tempSiteP)[0]))

if bypassInstA:

    # Verify Installation_A exists and is populated:
    if arcpy.Exists(os.path.join(cadDS,instAreaFC)) and int(arcpy.GetCount_management(os.path.join(cadDS,instAreaFC))[0]) > 0:

        # Verify Site_A exists
        if arcpy.Exists(os.path.join(cadDS,siteAreaFC)):

            # No data in Site_A
            if int(arcpy.GetCount_management(os.path.join(cadDS,siteAreaFC))[0]) == 0:
                arcpy.Append_management(instAreaFC, siteAreaFC, "NO_TEST")
                arcpy.AddMessage("{} Installation_A features appended to empty Site_A".format(arcpy.GetCount_management(os.path.join(cadDS,instAreaFC))[0]))

                # No data in Site_P
                if arcpy.Exists(os.path.join(cadDS,sitePtFC)):
                    createSiteP()

                #Site_P does not exist
                elif not arcpy.Exists(os.path.join(cadDS,sitePtFC)):
                    arcpy.AddWarning("WARNING: Site_P feature class does not exist. Can not proceed until Cadastre dataset contains the Installation_A, Site_A, and Site_P feature classes and associated schemas.")

            # Site_A is populated with something
            else:
                # Geometry compare of Installation_A and Site_A
                arcpy.MakeFeatureLayer_management(os.path.join(cadDS,instAreaFC), 'Inst_Alyr')
                lonelyInstA = arcpy.SelectLayerByLocation_management('Inst_Alyr', sblOverlapType, os.path.join(cadDS,siteAreaFC), selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")
                arcpy.MakeFeatureLayer_management(os.path.join(cadDS,siteAreaFC), 'Site_Alyr')
                lonelySiteA = arcpy.SelectLayerByLocation_management('Site_Alyr', sblOverlapType, os.path.join(cadDS,instAreaFC), selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")

                # Installation_A and Site_A same[ish] geometry
                if int(arcpy.GetCount_management(lonelyInstA)[0]) == 0 and int(arcpy.GetCount_management(lonelySiteA)[0]) == 0:
                    arcpy.AddMessage("Installation_A and Site_A share geometry boundaries. No features added to Site_A.")
                    createSiteP()

                # Installation_A and Site_A different geometry
                # Installation_A feature beyond Site_A boundary
                elif int(arcpy.GetCount_management(lonelyInstA)[0]) > 0:
                    arcpy.Append_management(lonelyInstA, siteAreaFC, "NO_TEST")
                    arcpy.AddMessage("Installation_A feature exists beyond the boundaries of Site_A. {} features appended to Site_A.".format(arcpy.GetCount_management(lonelyInstA)[0]))
                    createSiteP()

                # Site_A features beyond Installation_A boundary
                elif int(arcpy.GetCount_management(lonelySiteA)[0]) > 0:
                    arcpy.AddWarning("DATA VERIFICATION NEEDED: {} Site_A feature exists beyond the boundaries of Installation_A. No features appended to Installation_A.".format(arcpy.GetCount_management(lonelySiteA)[0]))
                    createSiteP()

        # WARNING: Site_A does not exist
        elif not acrpy.Exists(os.path.join(cadDS,siteAreaFC)):
            arcpy.AddWarning("WARNING: Site_A feature class does not exist. Can not proceed until Cadastre dataset contains the Installation_A, Site_A, and Site_P feature classes and associated schemas.")

    # Installation_A does not exist
    elif not arcpy.Exists(os.path.join(cadDS,instAreaFC)):
        arcpy.AddWarning("WARNING: Installation_A feature class does not exist. Can not proceed until Cadastre dataset contains the Installation_A, Site_A, and Site_P feature classes and associated schemas.")

# Bypass Installation_A and Site_A comparison
elif not bypassInstA:
    # Verify Site_A exists
    if arcpy.Exists(os.path.join(cadDS,siteAreaFC)) and arcpy.Exists(os.path.join(cadDS,sitePtFC)):
        # Verify Site_A contains data
        if int(arcpy.GetCount_management(os.path.join(cadDS,siteAreaFC))[0]) > 0:
            # Create Site points
            createSiteP()
        # Empty Site_A
        elif int(arcpy.GetCount_management(os.path.join(cadDS,siteAreaFC))[0]) == 0:
            arcpy.AddWarning("WARNING: Site_A contains no features. Can not create Site_P features while Site_A feature class is empty.")
    # Missing needed feature classes
    elif not arcpy.Exists(os.path.join(cadDS,siteAreaFC)) or not arcpy.Exists(os.path.join(cadDS,sitePtFC)):
        arcpy.AddWarning("WARNING: Can not proceed until Cadastre dataset contains both the Site_A and Site_P feature classes and associated schemas.")
