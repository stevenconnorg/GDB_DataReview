# -*- #################
"""
Created on Thu Apr 26 11:15:52 2018

@author: stevenconnorg
"""

### borrowed from : https://gis.stackexchange.com/questions/230720/arcpy-importmetadata-conversion-works-for-file-geodatabase-but-not-sde

import traceback
import os
import sys
import arcpy
import xml.etree.ElementTree as ET

def XSLTFilePath():
    installDir = arcpy.GetInstallInfo("desktop")["InstallDir"]
    return os.path.join(installDir, r"Metadata\Stylesheets\gpTools\exact copy of.xslt")

def metadataScratchFilePath(featureClassName):
    metadata_temp_folder = arcpy.env.scratchFolder
    return os.path.join(metadata_temp_folder, featureClassName + ".xml")

def nodeIsDefined(node):
    if node == None:
        return False
    elif len(node) == 0:
        return False
    return True

def updateMetaDataFileAbstract(metadata_file,abstractText):
    # update or add abstract info to the metadata
    doc = ET.parse(metadata_file)
    root_node = doc.getroot()
    dataIdInfo_node = root_node.find("dataIdInfo")
    if nodeIsDefined(dataIdInfo_node):
        abstract_node = dataIdInfo_node.find("idAbs")
    else:
        dataIdInfo_node = ET.SubElement(root_node, "dataIdInfo")
        abstract_node = ET.SubElement(dataIdInfo_node, "idAbs")
    abstract_node.text = abstractText
    tree = ET.ElementTree(root_node)
    tree.write(metadata_file)

def updateFeatureClassAbstract(featureClassLocation,featureClassName,abstractText):
    # set up scratch file location for XML
    metadata_file = metadataScratchFilePath(featureClassName)
    if os.path.exists(metadata_file):
        os.remove(metadata_file)
    # create XML scratch file
    arcpy.env.workspace = featureClassLocation
    arcpy.XSLTransform_conversion(featureClassName, XSLTFilePath(), metadata_file)
    # update XML file with new abstract
    updateMetaDataFileAbstract(metadata_file,abstractText)
    # write updates to the feature class
    arcpy.ImportMetadata_conversion(metadata_file, "FROM_ARCGIS", featureClassName,
                                    Enable_automatic_updates=False)

try:
    print("This works...")
    USERPROFILE = os.getenv('USERPROFILE')
    WS_FILE = USERPROFILE + '\\Documents\\ArcGIS\\Default.gdb'
    updateFeatureClassAbstract(WS_FILE,"myfeatureclass","This is my new abstract text")
    print("This doesn't...")
    updateFeatureClassAbstract('My_DB.sde', "myfeatureclass", "This is my new abstract text")
    # normal completion
except:
    crash_info = traceback.format_exc()
    crash_msg = "Script Crashed."
    print(crash_msg)
    print(crash_info)
    print(crash_msg)
    print(crash_info)
    sys.exit(99)
    # abnormal completion