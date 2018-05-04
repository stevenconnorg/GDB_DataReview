# -*- coding: utf-8 -*-

import contextlib
import os
import sys

import arcpy


# Export of toolbox C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx

import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = u'GDB_DataReview'
        self.alias = ''
        self.tools = [joinCalc, fixRoadNames, indeterminateData, summariseMissingData, calcRPSUIDfromPoly, FindDuplicateGeometry, chkRepairGeoms, batchExportMetadata, batchImportMetadata, clipFeats2geom, delDupFeats, standardizeBuildingAddress]

# Tool implementation code

class joinCalc(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\joinCalc"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(06) Join Fields and Calculate'
        self.description = u'Update the destination values in a destinate feature layer using a join with a source table field values.'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Transfer_From
        param_1 = arcpy.Parameter()
        param_1.name = u'Transfer_From'
        param_1.displayName = u'Transfer From'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Table View'

        # Using_Join_Field
        param_2 = arcpy.Parameter()
        param_2.name = u'Using_Join_Field'
        param_2.displayName = u'Using Join Field'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Field'

        # Source_Field
        param_3 = arcpy.Parameter()
        param_3.name = u'Source_Field'
        param_3.displayName = u'Source Field'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'Field'

        # Destination_Feature
        param_4 = arcpy.Parameter()
        param_4.name = u'Destination_Feature'
        param_4.displayName = u'Destination Feature'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'Feature Class'

        # Destination_Join_Field
        param_5 = arcpy.Parameter()
        param_5.name = u'Destination_Join_Field'
        param_5.displayName = u'Destination Join Field'
        param_5.parameterType = 'Required'
        param_5.direction = 'Input'
        param_5.datatype = u'Field'
        param_5.parameterDependencies = [3]

        # Destination_Field
        param_6 = arcpy.Parameter()
        param_6.name = u'Destination_Field'
        param_6.displayName = u'Destination Field'
        param_6.parameterType = 'Required'
        param_6.direction = 'Input'
        param_6.datatype = u'Field'
        param_6.parameterDependencies = [3]

        # Where_Clause
        param_7 = arcpy.Parameter()
        param_7.name = u'Where_Clause'
        param_7.displayName = u'Where Clause'
        param_7.parameterType = 'Required'
        param_7.direction = 'Input'
        param_7.datatype = u'String'
        param_7.value = u'IS NOT NULL'

        # Remove_Leading_Zeros_
        param_8 = arcpy.Parameter()
        param_8.name = u'Remove_Leading_Zeros_'
        param_8.displayName = u'Remove Leading Zeros?'
        param_8.parameterType = 'Required'
        param_8.direction = 'Input'
        param_8.datatype = u'Boolean'
        param_8.value = u'false'

        # Remove_Blank_Spaces_
        param_9 = arcpy.Parameter()
        param_9.name = u'Remove_Blank_Spaces_'
        param_9.displayName = u'Remove Blank Spaces?'
        param_9.parameterType = 'Required'
        param_9.direction = 'Input'
        param_9.datatype = u'Boolean'

        # Source_RPSUID_Field
        param_10 = arcpy.Parameter()
        param_10.name = u'Source_RPSUID_Field'
        param_10.displayName = u'Source_RPSUID_Field'
        param_10.parameterType = 'Required'
        param_10.direction = 'Input'
        param_10.datatype = u'Field'
        param_10.value = u'RPSUID'

        # Update_RPSUID_Field
        param_11 = arcpy.Parameter()
        param_11.name = u'Update_RPSUID_Field'
        param_11.displayName = u'Update RPSUID Field'
        param_11.parameterType = 'Required'
        param_11.direction = 'Input'
        param_11.datatype = u'Field'
        param_11.parameterDependencies = [3]

        return [param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, param_10, param_11]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\GDB_DataReview\\GDB_DataReview\\toolboxes\\joinCalc.py'

class fixRoadNames(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\fixRoadNames"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(08) Standardize 3 Address Fields'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Road_Feature_Class
        param_1 = arcpy.Parameter()
        param_1.name = u'Road_Feature_Class'
        param_1.displayName = u'Road Feature Class'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Feature Class'

        # Prefix_Field
        param_2 = arcpy.Parameter()
        param_2.name = u'Prefix_Field'
        param_2.displayName = u'Prefix Field'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Field'
        param_2.value = u'roadPrefix'

        # Name_Field
        param_3 = arcpy.Parameter()
        param_3.name = u'Name_Field'
        param_3.displayName = u'Name Field'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'Field'
        param_3.value = u'roadName'

        # Suffix_Field
        param_4 = arcpy.Parameter()
        param_4.name = u'Suffix_Field'
        param_4.displayName = u'Suffix Field'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'Field'
        param_4.value = u'roadSuffix'

        return [param_1, param_2, param_3, param_4]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\py\\standardizedRoadNames.py'

class indeterminateData(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\indeterminateData"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(11) Search for Indeterminant Data'
        self.description = u"Search a 'source' geodatabase for indeterminate data from feature dataset/feature class combinations in a target geodatabase. First, searches for missing feature datasets in target geodatabase not in source geodatabase. Then, searches for feature classes in 'x' feature dataset. Then, for each feature class in the source geodatabase, this tool searches for 'indeterminate' values in each field. Indeterminate values, here, means any null, to be determined (TBD), or 'other' values."
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Source_Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Source_Geodatabase'
        param_1.displayName = u'Source Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # Model_Geodatabase
        param_2 = arcpy.Parameter()
        param_2.name = u'Model_Geodatabase'
        param_2.displayName = u'Model Geodatabase'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Workspace'

        return [param_1, param_2]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\GDB_DataReview\\GDB_DataReview\\AF_Installation_Feedback\\py\\compareGDB_MissingData_gp.py'

class summariseMissingData(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\summariseMissingData"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(12) Summarise Indeterminant Data Tables'
        self.description = u'!!! IMPORTANT !!!\r\nThis script tool requires a few non-standard Python modules to run successfully, including the modules: numpy, pandas. To install these modules for use in ArcGIS, install the modules using the commands "pip install pandas" and "pip install numpy." To do this, (1) press the windows key on your keyboard, (2) type "cmd" to open the command prompt, (3) set your working directory as your ArcGIS Python scripts directory, typically located at C:\\Python27\\ArcGIS[versionNumber]\\Scripts (do this by typing \'cd C:\\Python27\\ArcGIS[versionNumber]\\Scripts\' and clicking enter). Replace [versionNumber] with you ArcGIS version number (e.g.: 10.6) - > C:\\Python27\\ArcGIS10.6\\Scripts, (4) type \'pip install numpy\' and press enter, then type  \'pip install pandas\' and press enter. If all goes well, you will have these modules successfully installed for use in ArcGIS\' Python distribution\r\n\r\n\r\nUse the 4 output tables created with the "Search for Indeterminate Data" script tool -- [comparison GDB]_MissingFDS", [comparison GDB]_MissingFCs", [comparison GDB]_MissingFields", [comparison GDB]_MissingData" -- to summarise into an Excel workbook. This tool creates an Excel workbook with 4 sheets that summarise (1) Summary_by_FC, which gives the counts and percentages of \'Other\', \'Null\', and \'TBD\' cells by Feature Class, as well as the total counts and percentages of indeterminate (Other + Null + TBD) and determinate cells (not Other, Null, or TBD), (2) Summary_by_Field, which gives the same statistics as the Summary_by_FC sheet, but broken down further by Feature Class Fields, (3) Empty Feature Classes from source geodatabase\'s standard Feature Classes (i.e.: Feature Classes included in comparison geodatabases), and (4) Indeterminate_Overview, which gives (a) total count of feature classes that are empty, (b) total number of standard feature classes that are empty, (c) the source geodatabase installation name, (d) the total number of missing feature classes, (e) the total number of missing feature datasets, (f) the total number of empty fields from empty feature classes, and (g) the total number of empty fields from non-empty feature classes.\r\n'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Missing_Feature_Dataset_Table
        param_1 = arcpy.Parameter()
        param_1.name = u'Missing_Feature_Dataset_Table'
        param_1.displayName = u'Missing Feature Dataset Table'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Table'

        # Missing_Feature_Class_Table
        param_2 = arcpy.Parameter()
        param_2.name = u'Missing_Feature_Class_Table'
        param_2.displayName = u'Missing Feature Class Table'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Table'

        # Missing_Field_Table
        param_3 = arcpy.Parameter()
        param_3.name = u'Missing_Field_Table'
        param_3.displayName = u'Missing Field Table'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'Table'

        # Missing_Data_Table
        param_4 = arcpy.Parameter()
        param_4.name = u'Missing_Data_Table'
        param_4.displayName = u'Missing Data Table'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'Table'

        # Output_Excel_Workbook_Location
        param_5 = arcpy.Parameter()
        param_5.name = u'Output_Excel_Workbook_Location'
        param_5.displayName = u'Output Excel Workbook Location'
        param_5.parameterType = 'Required'
        param_5.direction = 'Output'
        param_5.datatype = u'File'

        return [param_1, param_2, param_3, param_4, param_5]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\GDB_DataReview\\GDB_DataReview\\AF_Installation_Feedback\\py\\compareGDB_summariseMissingData_gp.py'

class calcRPSUIDfromPoly(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\calcRPSUIDfromPoly"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(03) Spatial Join and Calculate Field'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Geodatabase'
        param_1.displayName = u'Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # Source_Feature
        param_2 = arcpy.Parameter()
        param_2.name = u'Source_Feature'
        param_2.displayName = u'Source Feature'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Feature Class'

        # Source_Field
        param_3 = arcpy.Parameter()
        param_3.name = u'Source_Field'
        param_3.displayName = u'Source Field'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'Field'
        param_3.parameterDependencies = [1]

        # Target_Feature_Dataset_Wildcard
        param_4 = arcpy.Parameter()
        param_4.name = u'Target_Feature_Dataset_Wildcard'
        param_4.displayName = u'Target Feature Dataset Wildcard'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'String'
        param_4.value = u'*'

        # Target_Feature_Class_Wildcard
        param_5 = arcpy.Parameter()
        param_5.name = u'Target_Feature_Class_Wildcard'
        param_5.displayName = u'Target Feature Class Wildcard'
        param_5.parameterType = 'Required'
        param_5.direction = 'Input'
        param_5.datatype = u'String'
        param_5.value = u'*'

        # Target_Field_Wildcard
        param_6 = arcpy.Parameter()
        param_6.name = u'Target_Field_Wildcard'
        param_6.displayName = u'Target Field Wildcard'
        param_6.parameterType = 'Required'
        param_6.direction = 'Input'
        param_6.datatype = u'String'
        param_6.value = u'realPropertySiteUnique*'

        # Overlap_Type
        param_7 = arcpy.Parameter()
        param_7.name = u'Overlap_Type'
        param_7.displayName = u'Overlap Type'
        param_7.parameterType = 'Required'
        param_7.direction = 'Input'
        param_7.datatype = u'String'
        param_7.value = u'WITHIN'

        return [param_1, param_2, param_3, param_4, param_5, param_6, param_7]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\GDB_DataReview\\GDB_DataReview\\toolboxes\\joinAttsSpatJoin.py'

class FindDuplicateGeometry(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\FindDuplicateGeometry"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(01) Find Duplicate Geometry'
        self.description = u'Testing'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Input_Geodatabsae
        param_1 = arcpy.Parameter()
        param_1.name = u'Input_Geodatabsae'
        param_1.displayName = u'Input Geodatabsae'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # XY_Tolerance
        param_2 = arcpy.Parameter()
        param_2.name = u'XY_Tolerance'
        param_2.displayName = u'XY Tolerance'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'String'
        param_2.value = u'0'

        # Z_Tolerance
        param_3 = arcpy.Parameter()
        param_3.name = u'Z_Tolerance'
        param_3.displayName = u'Z Tolerance'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'String'
        param_3.value = u'0'

        # Output_CSV
        param_4 = arcpy.Parameter()
        param_4.name = u'Output_CSV'
        param_4.displayName = u'Output CSV'
        param_4.parameterType = 'Required'
        param_4.direction = 'Output'
        param_4.datatype = u'File'
        param_4.value = u'pathtofile.csv'

        # Output_Layers_Directory
        param_5 = arcpy.Parameter()
        param_5.name = u'Output_Layers_Directory'
        param_5.displayName = u'Output Layers Directory'
        param_5.parameterType = 'Required'
        param_5.direction = 'Input'
        param_5.datatype = u'Folder'
        param_5.value = u'path/to/directory'

        return [param_1, param_2, param_3, param_4, param_5]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\1528874122E\\Desktop\\GeoBase_FindDuplicates.py'

class chkRepairGeoms(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\chkRepairGeoms"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(04) Check and/or Repair Geometries'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Input_Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Input_Geodatabase'
        param_1.displayName = u'Input Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # Output_Geodatabase
        param_2 = arcpy.Parameter()
        param_2.name = u'Output_Geodatabase'
        param_2.displayName = u'Output Geodatabase'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Workspace'

        # Repair_Geometry_
        param_3 = arcpy.Parameter()
        param_3.name = u'Repair_Geometry_'
        param_3.displayName = u'Repair Geometry?'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'Boolean'

        # Delete_Null_Geometries_
        param_4 = arcpy.Parameter()
        param_4.name = u'Delete_Null_Geometries_'
        param_4.displayName = u'Delete Null Geometries?'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'Boolean'

        return [param_1, param_2, param_3, param_4]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\py\\CkRepairCkGeom.py'

class batchExportMetadata(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\batchExportMetadata"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(09) Batch Export Metadata to Directory'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Geodatabase'
        param_1.displayName = u'Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # Metadata_Translator
        param_2 = arcpy.Parameter()
        param_2.name = u'Metadata_Translator'
        param_2.displayName = u'Metadata Translator'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'String'
        param_2.value = u'C:\\Program Files (x86)\\ArcGIS\\Desktop10.6\\Metadata\\Translator\\ARCGIS2FGDC.xml'

        # Output_Directory
        param_3 = arcpy.Parameter()
        param_3.name = u'Output_Directory'
        param_3.displayName = u'Output Directory'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'Folder'

        return [param_1, param_2, param_3]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\py\\exportMetadata.py'

class batchImportMetadata(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\batchImportMetadata"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(10) Batch Import Metadata to Geodatabase Features'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Geodatabase'
        param_1.displayName = u'Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # Input_Metadata_Directory
        param_2 = arcpy.Parameter()
        param_2.name = u'Input_Metadata_Directory'
        param_2.displayName = u'Input Metadata Directory'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Workspace'

        # Import_Type
        param_3 = arcpy.Parameter()
        param_3.name = u'Import_Type'
        param_3.displayName = u'Import Type'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'String'
        param_3.value = u'FROM_FGDC'

        # Auto_Upate_
        param_4 = arcpy.Parameter()
        param_4.name = u'Auto_Upate_'
        param_4.displayName = u'Auto Upate?'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'String'
        param_4.value = u'ENABLED'

        return [param_1, param_2, param_3, param_4]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\py\\importMetadata.py'

class clipFeats2geom(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\clipFeats2geom"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(02) Clip GDB Features to Geometry'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Input_Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Input_Geodatabase'
        param_1.displayName = u'Input Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # Clip_Feature
        param_2 = arcpy.Parameter()
        param_2.name = u'Clip_Feature'
        param_2.displayName = u'Clip Feature'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Feature Class'

        # Cluster_Tolerance
        param_3 = arcpy.Parameter()
        param_3.name = u'Cluster_Tolerance'
        param_3.displayName = u'Cluster Tolerance'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'String'
        param_3.value = u'0'

        # Output_Clipped_Geodatabase
        param_4 = arcpy.Parameter()
        param_4.name = u'Output_Clipped_Geodatabase'
        param_4.displayName = u'Output Clipped Geodatabase'
        param_4.parameterType = 'Required'
        param_4.direction = 'Input'
        param_4.datatype = u'Workspace'

        return [param_1, param_2, param_3, param_4]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        # u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\py\\clipFeatstoGeom.py'

class delDupFeats(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\delDupFeats"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(05) Delete Duplicate Features'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Input_Geodatabase
        param_1 = arcpy.Parameter()
        param_1.name = u'Input_Geodatabase'
        param_1.displayName = u'Input Geodatabase'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Workspace'

        # XY_Tolerance
        param_2 = arcpy.Parameter()
        param_2.name = u'XY_Tolerance'
        param_2.displayName = u'XY Tolerance'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'String'
        param_2.value = u'0'

        # Z_Tolerance
        param_3 = arcpy.Parameter()
        param_3.name = u'Z_Tolerance'
        param_3.displayName = u'Z Tolerance'
        param_3.parameterType = 'Required'
        param_3.direction = 'Input'
        param_3.datatype = u'String'
        param_3.value = u'0'

        return [param_1, param_2, param_3]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        with script_run_as(u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\GDB_DataReview\\GDB_DataReview\\py\\delDupFeats.py'):
            # -*- #################
            """
            Created on Thu Apr 26 11:15:52 2018
            
            @author: stevenconnorg
            """
            
            import arcpy
            #Get path to the geodatabase
            workpath = parameters[0].valueAsText
            xyTol = parameters[1].valueAsText
            zTol = parameters[2].valueAsText
            
            # Workspace
            arcpy.env.workspace = workpath
            arcpy.env.overwriteOutput = True
            
            def unique_values(table , field):
                            with arcpy.da.SearchCursor(table, [field]) as cursor:
                                return sorted({row[0] for row in cursor})
                            
            for dataset in arcpy.ListDatasets():  
                for fc in arcpy.ListFeatureClasses('','',dataset):
                    fcCount = arcpy.GetCount_management(fc)
                    ignoreType = ['OID', 'Guid',  'GlobalID', 'Blob','Raster']
                    ignoreFld = ['LAST_EDITED_DATE','LAST_EDITED_USER','CREATED_USER','CREATED_DATE']
                    if int(fcCount[0]) == 0:
                        messages.AddMessage("No features in "+fc+" ... skipping!")
                        pass
                    else:
                        # Find duplicate geometry
                        flds = arcpy.ListFields(fc)
                        fldNames = []
                        for fld in flds:
                            if fld.type not in ignoreType:
                                if fld.name.lower() not in [x.lower() for x in ignoreFld]:
                                    fldNames.append(str(fld.name))
                                
                            #if fld.name.lower() not in [x.lower() for x in ignoreFLD]:
                        dupeTable = "in_memory\\tmp"
                        arcpy.FindIdentical_management(fc, dupeTable, fldNames,xy_tolerance= xyTol, z_tolerance = zTol, output_record_option="ONLY_DUPLICATES")
                        
                        # Get table count and pass the dataset if no duplicates exist
                        fidList=[]
                        with arcpy.da.SearchCursor(dupeTable,["IN_FID"]) as cursor:
                                for row in cursor:
                                    fidList.append(row[0])
                        #expression = 'OBJECTID IN ({0})'.format(', '.join(map(str, fidList)) or 'NULL')
                        tblCount = arcpy.GetCount_management(dupeTable)
                        
                        uniqdupCount = len(unique_values(dupeTable , "FEAT_SEQ"))
                        dupCount = len(unique_values(dupeTable , "IN_FID"))
            
                        fidList.sort()
                        FIDs =  ', '.join(map(str, fidList))
                            
                        if int(tblCount[0]) == 0:
                            messages.AddMessage("No duplicate features found in " + fc)
                            continue
                        else:
                            messages.AddMessage("Deleting "+ str(dupCount) +" duplicates across "+str(uniqdupCount)+" features in " + fc)
                            arcpy. DeleteIdentical_management (fc, fldNames, xy_tolerance=xyTol, z_tolerance=zTol)
                        arcpy.Delete_management("in_memory\\tmp") 
            

class standardizeBuildingAddress(object):
    """C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\toolboxes\GDB_DataReview.tbx\standardizeBuildingAddress"""
    import arcpy
    class ToolValidator(object):
      """Class for validating a tool's parameter values and controlling
      the behavior of the tool's dialog."""
    
      def __init__(self, parameters):
        """Setup arcpy and the list of tool parameters."""
        self.params = parameters
    
      def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""
        return
    
      def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
    
      def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
    
    def __init__(self):
        self.label = u'(07) Standardize 1 Address Field'
        self.canRunInBackground = False
    def getParameterInfo(self):
        # Feature_Class
        param_1 = arcpy.Parameter()
        param_1.name = u'Feature_Class'
        param_1.displayName = u'Feature Class'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'Feature Class'

        # Address_Field
        param_2 = arcpy.Parameter()
        param_2.name = u'Address_Field'
        param_2.displayName = u'Address Field'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'Field'
        param_2.value = u'buildingAddress'

        return [param_1, param_2]
    def isLicensed(self):
        return True
    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateParameters()
    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
             return validator(parameters).updateMessages()
    def execute(self, parameters, messages):
        with script_run_as(u'C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\GDB_DataReview\\GDB_DataReview\\py\\standardizedBuildingAddresses.py'):
            # -*- coding: utf-8 -*-
            """
            Created on Wed Apr 25 07:53:08 2018
            
            @author: stevenconnorg
            """
            
            
            
            import arcpy, os
            from arcpy import env
            env.overwriteOutput = True
            
            # usps suffix data from https://github.com/allanbreyes/udacity-data-science/tree/master/p2/data
                 
            fc =  parameters[0].valueAsText
            fld =  parameters[1].valueAsText
            
            def get_geodatabase_path(input_table):
              '''Return the Geodatabase path from the input table or feature class.
              :param input_table: path to the input table or feature class 
              '''
              workspace = os.path.dirname(input_table)
              if [any(ext) for ext in ('.gdb', '.mdb', '.sde') if ext in os.path.splitext(workspace)]:
                return workspace
              else:
                return os.path.dirname(workspace)
            
            gdbPath = get_geodatabase_path(fc[0])
            
            
            arcpy.env.workspace=gdbPath
            # column names: 
            # PrimaryStreetSuffixName
            # CommonlyUsed
            # PostalServiceStandardSuffixAbbreviation
            suffixes = [['ALLEY', 'ALLEE', 'ALY'],
             ['ALLEY', 'ALLEY', 'ALY'],
             ['ALLEY', 'ALLY', 'ALY'],
             ['ALLEY', 'ALY', 'ALY'],
             ['ANNEX', 'ANEX ', 'ANX'],
             ['ANNEX', 'ANNEX', 'ANX'],
             ['ANNEX', 'ANNX', 'ANX'],
             ['ANNEX ', 'ANX', 'ANX'],
             ['ARCADE', 'ARC', 'ARC'],
             ['ARCADE', 'ARCADE', 'ARC'],
             ['AVENUE', 'AV', 'AVE'],
             ['AVENUE', 'AVE', 'AVE'],
             ['AVENUE', 'AVEN', 'AVE'],
             ['AVENUE', 'AVENU', 'AVE'],
             ['AVENUE', 'AVENUE', 'AVE'],
             ['AVENUE', 'AVN', 'AVE'],
             ['AVENUE', 'AVNUE', 'AVE'],
             ['BAYOO', 'BAYOO', 'BYU'],
             ['BAYOO', 'BAYOU', 'BYU'],
             ['BEACH', 'BCH', 'BCH'],
             ['BEACH', 'BEACH', 'BCH'],
             ['BEND', 'BEND', 'BND'],
             ['BEND', 'BND', 'BND'],
             ['BLUFF', 'BLF', 'BLF'],
             ['BLUFF', 'BLUF', 'BLF'],
             ['BLUFF', 'BLUFF', 'BLF'],
             ['BLUFFS', 'BLUFFS', 'BLFS'],
             ['BOTTOM', 'BOT', 'BTM'],
             ['BOTTOM', 'BOTTM', 'BTM'],
             ['BOTTOM', 'BOTTOM', 'BTM'],
             ['BOTTOM ', 'BTM', 'BTM'],
             ['BOULEVARD', 'BLVD', 'BLVD'],
             ['BOULEVARD', 'BOUL', 'BLVD'],
             ['BOULEVARD', 'BOULEVARD', 'BLVD'],
             ['BOULEVARD', 'BOULV', 'BLVD'],
             ['BRANCH', 'BR', 'BR'],
             ['BRANCH', 'BRANCH', 'BR'],
             ['BRANCH', 'BRNCH', 'BR'],
             ['BRIDGE', 'BRDGE', 'BRG'],
             ['BRIDGE', 'BRG', 'BRG'],
             ['BRIDGE', 'BRIDGE', 'BRG'],
             ['BROOK', 'BRK', 'BRK'],
             ['BROOK', 'BROOK', 'BRK'],
             ['BROOKS', 'BROOKS', 'BRKS'],
             ['BURG', 'BURG', 'BG'],
             ['BURGS', 'BURGS', 'BGS'],
             ['BYPASS', 'BYP', 'BYP'],
             ['BYPASS', 'BYPA', 'BYP'],
             ['BYPASS', 'BYPAS', 'BYP'],
             ['BYPASS', 'BYPASS', 'BYP'],
             ['BYPASS', 'BYPS', 'BYP'],
             ['CAMP ', 'CAMP', 'CP'],
             ['CAMP ', 'CMP', 'CP'],
             ['CAMP ', 'CP', 'CP'],
             ['CANYON ', 'CANYN', 'CYN'],
             ['CANYON ', 'CANYON', 'CYN'],
             ['CANYON ', 'CNYN', 'CYN'],
             ['CANYON ', 'CYN', 'CYN'],
             ['CAPE ', 'CAPE', 'CPE'],
             ['CAPE ', 'CPE', 'CPE'],
             ['CAUSEWAY ', 'CAUSEWAY', 'CSWY'],
             ['CAUSEWAY ', 'CAUSWAY', 'CSWY'],
             ['CAUSEWAY ', 'CSWY', 'CSWY'],
             ['CENTER ', 'CEN', 'CTR'],
             ['CENTER ', 'CENT', 'CTR'],
             ['CENTER ', 'CENTER ', 'CTR'],
             ['CENTER ', 'CENTR ', 'CTR'],
             ['CENTER ', 'CENTRE', 'CTR'],
             ['CENTER ', 'CNTER ', 'CTR'],
             ['CENTER ', 'CNTR ', 'CTR'],
             ['CENTER ', 'CTR ', 'CTR'],
             ['CENTERS ', 'CENTERS ', 'CTRS'],
             ['CIRCLE ', 'CIR ', 'CIR'],
             ['CIRCLE ', 'CIRC ', 'CIR'],
             ['CIRCLE ', 'CIRCL ', 'CIR'],
             ['CIRCLE ', 'CIRCLE ', 'CIR'],
             ['CIRCLE ', 'CRCL ', 'CIR'],
             ['CIRCLE ', 'CRCLE ', 'CIR'],
             ['CIRCLES ', 'CIRCLES ', 'CIRS'],
             ['CLIFF ', 'CLF ', 'CLF'],
             ['CLIFF ', 'CLIFF ', 'CLF'],
             ['CLIFFS ', 'CLFS ', 'CLFS'],
             ['CLIFFS ', 'CLIFFS ', 'CLFS'],
             ['CLUB ', 'CLB ', 'CLB'],
             ['CLUB ', 'CLUB ', 'CLB'],
             ['COMMON ', 'COMMON ', 'CMN'],
             ['CORNER ', 'COR ', 'COR'],
             ['CORNER ', 'CORNER ', 'COR'],
             ['CORNERS ', 'CORNERS ', 'CORS'],
             ['CORNERS ', 'CORS ', 'CORS'],
             ['COURSE ', 'COURSE ', 'CRSE'],
             ['COURSE ', 'CRSE ', 'CRSE'],
             ['COURT ', 'COURT ', 'CT'],
             ['COURT ', 'CRT ', 'CT'],
             ['COURT ', 'CT ', 'CT'],
             ['COURTS ', 'COURTS ', 'CTS'],
             ['COURTS ', 'CT ', 'CTS'],
             ['COVE ', 'COVE ', 'CV'],
             ['COVE ', 'CV ', 'CV'],
             ['COVES ', 'COVES ', 'CVS'],
             ['CREEK ', 'CK ', 'CRK'],
             ['CREEK ', 'CR ', 'CRK'],
             ['CREEK ', 'CREEK ', 'CRK'],
             ['CREEK ', 'CRK ', 'CRK'],
             ['CRESCENT ', 'CRECENT ', 'CRES'],
             ['CRESCENT ', 'CRES ', 'CRES'],
             ['CRESCENT ', 'CRESCENT ', 'CRES'],
             ['CRESCENT ', 'CRESENT ', 'CRES'],
             ['CRESCENT ', 'CRSCNT ', 'CRES'],
             ['CRESCENT ', 'CRSENT ', 'CRES'],
             ['CRESCENT ', 'CRSNT ', 'CRES'],
             ['CREST ', 'CREST ', 'CRST'],
             ['CROSSING ', 'CROSSING ', 'XING'],
             ['CROSSING ', 'CRSSING ', 'XING'],
             ['CROSSING ', 'CRSSNG ', 'XING'],
             ['CROSSING ', 'XING ', 'XING'],
             ['CROSSROAD ', 'CROSSROAD ', 'XRD'],
             ['CURVE ', 'CURVE ', 'CURV'],
             ['DALE', 'DALE', 'DL'],
             ['DALE', 'DL', 'DL'],
             ['DAM', 'DAM', 'DM'],
             ['DAM', 'DM ', 'DM'],
             ['DIVIDE', 'DIV', 'DV'],
             ['DIVIDE', 'DIVIDE', 'DV'],
             ['DIVIDE', 'DV', 'DV'],
             ['DIVIDE', 'DVD', 'DV'],
             ['DRIVE', 'DRIV', 'DR'],
             ['DRIVE', 'DRIVE', 'DR'],
             ['DRIVE', 'DRV', 'DR'],
             ['DRIVE ', 'DR', 'DR'],
             ['DRIVES', 'DRIVES', 'DRS'],
             ['ESTATE', 'EST', 'EST'],
             ['ESTATE', 'ESTATE', 'EST'],
             ['ESTATES', 'ESTATES', 'ESTS'],
             ['ESTATES', 'ESTS', 'ESTS'],
             ['EXPRESSWAY', 'EXP', 'EXPY'],
             ['EXPRESSWAY', 'EXPR', 'EXPY'],
             ['EXPRESSWAY', 'EXPRESS', 'EXPY'],
             ['EXPRESSWAY', 'EXPRESSWAY', 'EXPY'],
             ['EXPRESSWAY', 'EXPW', 'EXPY'],
             ['EXPRESSWAY', 'EXPY', 'EXPY'],
             ['EXTENSION', 'EXT', 'EXT'],
             ['EXTENSION', 'EXTENSION', 'EXT'],
             ['EXTENSION', 'EXTN', 'EXT'],
             ['EXTENSION', 'EXTNSN', 'EXT'],
             ['EXTENSIONS', 'EXTENSIONS', 'EXTS'],
             ['EXTENSIONS', 'EXTS', 'EXTS'],
             ['FALL', 'FALL', 'FALL'],
             ['FALLS', 'FALLS', 'FLS'],
             ['FALLS', 'FLS', 'FLS'],
             ['FERRY', 'FERRY', 'FRY'],
             ['FERRY', 'FRRY', 'FRY'],
             ['FERRY', 'FRY', 'FRY'],
             ['FIELD', 'FIELD', 'FLD'],
             ['FIELD', 'FLD', 'FLD'],
             ['FIELDS', 'FIELDS', 'FLDS'],
             ['FIELDS', 'FLDS', 'FLDS'],
             ['FLAT', 'FLAT', 'FLT'],
             ['FLAT', 'FLT', 'FLT'],
             ['FLATS', 'FLATS', 'FLTS'],
             ['FLATS', 'FLTS', 'FLTS'],
             ['FORD', 'FORD', 'FRD'],
             ['FORD', 'FRD', 'FRD'],
             ['FORDS', 'FORDS', 'FRDS'],
             ['FOREST', 'FOREST', 'FRST'],
             ['FOREST', 'FORESTS', 'FRST'],
             ['FOREST', 'FRST', 'FRST'],
             ['FORGE', 'FORG', 'FRG'],
             ['FORGE', 'FORGE', 'FRG'],
             ['FORGE', 'FRG', 'FRG'],
             ['FORGES', 'FORGES', 'FRGS'],
             ['FORK', 'FORK', 'FRK'],
             ['FORK', 'FRK', 'FRK'],
             ['FORKS', 'FORKS', 'FRKS'],
             ['FORKS', 'FRKS', 'FRKS'],
             ['FORT', 'FORT', 'FT'],
             ['FORT', 'FRT', 'FT'],
             ['FORT', 'FT', 'FT'],
             ['FREEWAY', 'FREEWAY', 'FWY'],
             ['FREEWAY', 'FREEWY', 'FWY'],
             ['FREEWAY', 'FRWAY', 'FWY'],
             ['FREEWAY', 'FRWY', 'FWY'],
             ['FREEWAY', 'FWY', 'FWY'],
             ['GARDEN', 'GARDEN', 'GDN'],
             ['GARDEN', 'GARDN', 'GDN'],
             ['GARDEN', 'GDN', 'GDN'],
             ['GARDEN', 'GRDEN', 'GDN'],
             ['GARDEN', 'GRDN', 'GDN'],
             ['GARDENS', 'GARDENS', 'GDNS'],
             ['GARDENS', 'GDNS', 'GDNS'],
             ['GARDENS', 'GRDNS', 'GDNS'],
             ['GATEWAY', 'GATEWAY', 'GTWY'],
             ['GATEWAY', 'GATEWY', 'GTWY'],
             ['GATEWAY', 'GATWAY', 'GTWY'],
             ['GATEWAY', 'GTWAY', 'GTWY'],
             ['GATEWAY', 'GTWY', 'GTWY'],
             ['GLEN', 'GLEN', 'GLN'],
             ['GLEN', 'GLN', 'GLN'],
             ['GLENS', 'GLENS', 'GLNS'],
             ['GREEN', 'GREEN', 'GRN'],
             ['GREEN', 'GRN', 'GRN'],
             ['GREENS', 'GREENS', 'GRNS'],
             ['GROVE', 'GROV', 'GRV'],
             ['GROVE', 'GROVE', 'GRV'],
             ['GROVE', 'GRV', 'GRV'],
             ['GROVES', 'GROVES', 'GRVS'],
             ['HARBOR', 'HARB', 'HBR'],
             ['HARBOR', 'HARBOR', 'HBR'],
             ['HARBOR', 'HARBR', 'HBR'],
             ['HARBOR', 'HBR', 'HBR'],
             ['HARBOR', 'HRBOR', 'HBR'],
             ['HARBORS', 'HARBORS', 'HBRS'],
             ['HAVEN', 'HAVEN', 'HVN'],
             ['HAVEN', 'HAVN', 'HVN'],
             ['HAVEN', 'HVN', 'HVN'],
             ['HEIGHTS', 'HEIGHT', 'HTS'],
             ['HEIGHTS', 'HEIGHTS', 'HTS'],
             ['HEIGHTS', 'HGTS', 'HTS'],
             ['HEIGHTS', 'HT', 'HTS'],
             ['HEIGHTS', 'HTS', 'HTS'],
             ['HIGHWAY', 'HIGHWAY', 'HWY'],
             ['HIGHWAY', 'HIGHWY', 'HWY'],
             ['HIGHWAY', 'HIWAY', 'HWY'],
             ['HIGHWAY', 'HIWY', 'HWY'],
             ['HIGHWAY', 'HWAY', 'HWY'],
             ['HIGHWAY', 'HWY', 'HWY'],
             ['HILL', 'HILL', 'HL'],
             ['HILL', 'HL', 'HL'],
             ['HILLS', 'HILLS', 'HLS'],
             ['HILLS', 'HLS', 'HLS'],
             ['HOLLOW ', 'HLLW', 'HOLW'],
             ['HOLLOW ', 'HOLLOW', 'HOLW'],
             ['HOLLOW ', 'HOLLOWS', 'HOLW'],
             ['HOLLOW ', 'HOLW', 'HOLW'],
             ['HOLLOW ', 'HOLWS', 'HOLW'],
             ['INLET', 'INLET', 'INLT'],
             ['INLET ', 'INLT', 'INLT'],
             ['ISLAND', 'IS', 'IS'],
             ['ISLAND ', 'ISLAND', 'IS'],
             ['ISLAND ', 'ISLND', 'IS'],
             ['ISLANDS', 'ISS', 'ISS'],
             ['ISLANDS ', 'ISLANDS', 'ISS'],
             ['ISLANDS ', 'ISLNDS', 'ISS'],
             ['ISLE', 'ISLE', 'ISLE'],
             ['ISLE ', 'ISLES', 'ISLE'],
             ['JUNCTION', 'JCT', 'JCT'],
             ['JUNCTION', 'JCTION', 'JCT'],
             ['JUNCTION', 'JCTN', 'JCT'],
             ['JUNCTION', 'JUNCTION', 'JCT'],
             ['JUNCTION', 'JUNCTN', 'JCT'],
             ['JUNCTION', 'JUNCTON', 'JCT'],
             ['JUNCTIONS', 'JCTNS', 'JCTS'],
             ['JUNCTIONS', 'JCTS', 'JCTS'],
             ['JUNCTIONS', 'JUNCTIONS', 'JCTS'],
             ['KEY', 'KEY', 'KY'],
             ['KEY', 'KY', 'KY'],
             ['KEYS', 'KEYS', 'KYS'],
             ['KEYS', 'KYS', 'KYS'],
             ['KNOLL', 'KNL', 'KNL'],
             ['KNOLL', 'KNOL', 'KNL'],
             ['KNOLL', 'KNOLL', 'KNL'],
             ['KNOLLS', 'KNLS', 'KNLS'],
             ['KNOLLS', 'KNOLLS', 'KNLS'],
             ['LAKE', 'LAKE', 'LK'],
             ['LAKE', 'LK', 'LK'],
             ['LAKES', 'LAKES', 'LKS'],
             ['LAKES', 'LKS', 'LKS'],
             ['LAND', 'LAND', 'LAND'],
             ['LANDING', 'LANDING', 'LNDG'],
             ['LANDING', 'LNDG', 'LNDG'],
             ['LANDING', 'LNDNG', 'LNDG'],
             ['LANE', 'LA', 'LN'],
             ['LANE', 'LANE', 'LN'],
             ['LANE', 'LANES', 'LN'],
             ['LANE', 'LN', 'LN'],
             ['LIGHT', 'LGT', 'LGT'],
             ['LIGHT', 'LIGHT', 'LGT'],
             ['LIGHTS', 'LIGHTS', 'LGTS'],
             ['LOAF ', 'LF', 'LF'],
             ['LOAF ', 'LOAF', 'LF'],
             ['LOCK ', 'LCK', 'LCK'],
             ['LOCK ', 'LOCK', 'LCK'],
             ['LOCKS', 'LOCKS', 'LCKS'],
             ['LOCKS ', 'LCKS', 'LCKS'],
             ['LODGE', 'LDGE', 'LDG'],
             ['LODGE ', 'LDG', 'LDG'],
             ['LODGE ', 'LODG', 'LDG'],
             ['LODGE ', 'LODGE', 'LDG'],
             ['LOOP ', 'LOOP', 'LOOP'],
             ['LOOP ', 'LOOPS', 'LOOP'],
             ['MALL', 'MALL', 'MALL'],
             ['MANOR', 'MANOR', 'MNR'],
             ['MANOR', 'MNR', 'MNR'],
             ['MANORS', 'MANORS', 'MNRS'],
             ['MANORS', 'MNRS', 'MNRS'],
             ['MEADOW', 'MDW', 'MDW'],
             ['MEADOW', 'MEADOW', 'MDW'],
             ['MEADOWS', 'MDWS', 'MDWS'],
             ['MEADOWS', 'MEADOWS', 'MDWS'],
             ['MEADOWS', 'MEDOWS', 'MDWS'],
             ['MEWS', 'MEWS', 'MEWS'],
             ['MILL', 'MILL', 'ML'],
             ['MILL', 'ML', 'ML'],
             ['MILLS', 'MILLS', 'MLS'],
             ['MILLS', 'MLS', 'MLS'],
             ['MISSION', 'MISSION', 'MSN'],
             ['MISSION', 'MSN', 'MSN'],
             ['MISSION', 'MSSN', 'MSN'],
             ['MISSION ', 'MISSN', 'MSN'],
             ['MOTORWAY', 'MOTORWAY', 'MTWY'],
             ['MOUNT', 'MNT', 'MT'],
             ['MOUNT', 'MOUNT', 'MT'],
             ['MOUNT', 'MT', 'MT'],
             ['MOUNTAIN', 'MNTAIN', 'MTN'],
             ['MOUNTAIN', 'MNTN', 'MTN'],
             ['MOUNTAIN', 'MOUNTIN', 'MTN'],
             ['MOUNTAIN', 'MTIN', 'MTN'],
             ['MOUNTAIN ', 'MOUNTAIN', 'MTN'],
             ['MOUNTAIN ', 'MTN', 'MTN'],
             ['MOUNTAINS', 'MOUNTAINS', 'MTNS'],
             ['MOUNTAINS ', 'MNTNS', 'MTNS'],
             ['NECK', 'NCK', 'NCK'],
             ['NECK', 'NECK', 'NCK'],
             ['ORCHARD', 'ORCH', 'ORCH'],
             ['ORCHARD', 'ORCHARD', 'ORCH'],
             ['ORCHARD', 'ORCHRD', 'ORCH'],
             ['OVAL', 'OVAL', 'OVAL'],
             ['OVAL', 'OVL', 'OVAL'],
             ['OVERPASS', 'OVERPASS', 'OPAS'],
             ['PARK', 'PARK', 'PARK'],
             ['PARK', 'PK', 'PARK'],
             ['PARK', 'PRK', 'PARK'],
             ['PARKS', 'PARKS', 'PARK'],
             ['PARKWAY', 'PARKWAY', 'PKWY'],
             ['PARKWAY', 'PARKWY', 'PKWY'],
             ['PARKWAY', 'PKWAY', 'PKWY'],
             ['PARKWAY', 'PKWY', 'PKWY'],
             ['PARKWAY', 'PKY', 'PKWY'],
             ['PARKWAYS', 'PARKWAYS', 'PKWY'],
             ['PARKWAYS', 'PKWYS', 'PKWY'],
             ['PASS', 'PASS', 'PASS'],
             ['PASSAGE', 'PASSAGE', 'PSGE'],
             ['PATH', 'PATH', 'PATH'],
             ['PATH', 'PATHS', 'PATH'],
             ['PIKE', 'PIKE', 'PIKE'],
             ['PIKE', 'PIKES', 'PIKE'],
             ['PINE', 'PINE', 'PNE'],
             ['PINES', 'PINES', 'PNES'],
             ['PINES', 'PNES', 'PNES'],
             ['PLACE', 'PL', 'PL'],
             ['PLACE', 'PLACE', 'PL'],
             ['PLAIN', 'PLAIN', 'PLN'],
             ['PLAIN', 'PLN', 'PLN'],
             ['PLAINS', 'PLAINES', 'PLNS'],
             ['PLAINS', 'PLAINS', 'PLNS'],
             ['PLAINS ', 'PLNS', 'PLNS'],
             ['PLAZA', 'PLAZA', 'PLZ'],
             ['PLAZA', 'PLZA', 'PLZ'],
             ['PLAZA ', 'PLZ', 'PLZ'],
             ['POINT ', 'POINT', 'PT'],
             ['POINT ', 'PT', 'PT'],
             ['POINTS', 'POINTS', 'PTS'],
             ['POINTS', 'PTS', 'PTS'],
             ['PORT', 'PRT', 'PRT'],
             ['PORT ', 'PORT', 'PRT'],
             ['PORTS', 'PRTS', 'PRTS'],
             ['PORTS ', 'PORTS', 'PRTS'],
             ['PRAIRIE', 'PR', 'PR'],
             ['PRAIRIE', 'PRR', 'PR'],
             ['PRAIRIE ', 'PRAIRIE', 'PR'],
             ['PRAIRIE ', 'PRARIE', 'PR'],
             ['RADIAL', 'RAD', 'RADL'],
             ['RADIAL', 'RADIAL', 'RADL'],
             ['RADIAL', 'RADIEL', 'RADL'],
             ['RADIAL', 'RADL', 'RADL'],
             ['RAMP', 'RAMP', 'RAMP'],
             ['RANCH', 'RANCH', 'RNCH'],
             ['RANCH', 'RANCHES', 'RNCH'],
             ['RANCH', 'RNCH', 'RNCH'],
             ['RANCH', 'RNCHS', 'RNCH'],
             ['RAPID', 'RAPID', 'RPD'],
             ['RAPID', 'RPD', 'RPD'],
             ['RAPIDS', 'RAPIDS', 'RPDS'],
             ['RAPIDS', 'RPDS', 'RPDS'],
             ['REST', 'REST', 'RST'],
             ['REST', 'RST', 'RST'],
             ['RIDGE', 'RDG', 'RDG'],
             ['RIDGE', 'RDGE', 'RDG'],
             ['RIDGE', 'RIDGE', 'RDG'],
             ['RIDGES', 'RDGS', 'RDGS'],
             ['RIDGES', 'RIDGES', 'RDGS'],
             ['RIVER', 'RIV', 'RIV'],
             ['RIVER', 'RIVER', 'RIV'],
             ['RIVER', 'RIVR', 'RIV'],
             ['RIVER', 'RVR', 'RIV'],
             ['ROAD', 'RD', 'RD'],
             ['ROAD ', 'ROAD', 'RD'],
             ['ROADS', 'RDS', 'RDS'],
             ['ROADS ', 'ROADS', 'RDS'],
             ['ROUTE', 'ROUTE', 'RTE'],
             ['ROW ', 'ROW', 'ROW'],
             ['RUE ', 'RUE', 'RUE'],
             ['RUN', 'RUN', 'RUN'],
             ['SHOAL', 'SHL', 'SHL'],
             ['SHOAL', 'SHOAL', 'SHL'],
             ['SHOALS', 'SHLS', 'SHLS'],
             ['SHOALS', 'SHOALS', 'SHLS'],
             ['SHORE', 'SHOAR', 'SHR'],
             ['SHORE', 'SHORE', 'SHR'],
             ['SHORE', 'SHR', 'SHR'],
             ['SHORES', 'SHOARS', 'SHRS'],
             ['SHORES', 'SHORES', 'SHRS'],
             ['SHORES', 'SHRS', 'SHRS'],
             ['SKYWAY', 'SKYWAY', 'SKWY'],
             ['SPRING', 'SPG', 'SPG'],
             ['SPRING', 'SPNG', 'SPG'],
             ['SPRING', 'SPRING', 'SPG'],
             ['SPRING', 'SPRNG', 'SPG'],
             ['SPRINGS', 'SPNGS', 'SPGS'],
             ['SPRINGS', 'SPRINGS', 'SPGS'],
             ['SPRINGS', 'SPRNGS', 'SPGS'],
             ['SPRINGS ', 'SPGS', 'SPGS'],
             ['SPUR', 'SPUR', 'SPUR'],
             ['SPURS', 'SPURS', 'SPUR'],
             ['SQUARE', 'SQ', 'SQ'],
             ['SQUARE', 'SQR', 'SQ'],
             ['SQUARE', 'SQRE', 'SQ'],
             ['SQUARE', 'SQUARE', 'SQ'],
             ['SQUARE ', 'SQU', 'SQ'],
             ['SQUARES', 'SQRS', 'SQS'],
             ['SQUARES ', 'SQUARES', 'SQS'],
             ['STATION', 'STATION', 'STA'],
             ['STATION', 'STATN', 'STA'],
             ['STATION ', 'STA', 'STA'],
             ['STATION ', 'STN', 'STA'],
             ['STRAVENUE', 'STRAV', 'STRA'],
             ['STRAVENUE', 'STRAVE', 'STRA'],
             ['STRAVENUE', 'STRAVN', 'STRA'],
             ['STRAVENUE', 'STRVN', 'STRA'],
             ['STRAVENUE ', 'STRA', 'STRA'],
             ['STRAVENUE ', 'STRAVEN', 'STRA'],
             ['STRAVENUE ', 'STRAVENUE', 'STRA'],
             ['STRAVENUE ', 'STRVNUE', 'STRA'],
             ['STREAM', 'STREME', 'STRM'],
             ['STREAM ', 'STREAM', 'STRM'],
             ['STREAM ', 'STRM', 'STRM'],
             ['STREET', 'ST', 'ST'],
             ['STREET', 'STRT', 'ST'],
             ['STREET ', 'STR', 'ST'],
             ['STREET ', 'STREET', 'ST'],
             ['STREETS', 'STREETS', 'STS'],
             ['SUMMIT', 'SUMIT', 'SMT'],
             ['SUMMIT', 'SUMMIT', 'SMT'],
             ['SUMMIT ', 'SMT', 'SMT'],
             ['SUMMIT ', 'SUMITT', 'SMT'],
             ['TERRACE', 'TER', 'TER'],
             ['TERRACE', 'TERR', 'TER'],
             ['TERRACE', 'TERRACE', 'TER'],
             ['THROUGHWAY', 'THROUGHWAY', 'TRWY'],
             ['TRACE', 'TRACE', 'TRCE'],
             ['TRACE', 'TRACES', 'TRCE'],
             ['TRACE', 'TRCE', 'TRCE'],
             ['TRACK', 'TRACK', 'TRAK'],
             ['TRACK', 'TRACKS', 'TRAK'],
             ['TRACK', 'TRAK', 'TRAK'],
             ['TRACK', 'TRK', 'TRAK'],
             ['TRACK', 'TRKS', 'TRAK'],
             ['TRAFFICWAY', 'TRAFFICWAY', 'TRFY'],
             ['TRAFFICWAY', 'TRFY', 'TRFY'],
             ['TRAIL', 'TR', 'TRL'],
             ['TRAIL', 'TRAILS', 'TRL'],
             ['TRAIL', 'TRL', 'TRL'],
             ['TRAIL', 'TRLS', 'TRL'],
             ['TRAIL ', 'TRAIL', 'TRL'],
             ['TUNNEL', 'TUNEL', 'TUNL'],
             ['TUNNEL', 'TUNL', 'TUNL'],
             ['TUNNEL', 'TUNLS', 'TUNL'],
             ['TUNNEL', 'TUNNEL', 'TUNL'],
             ['TUNNEL', 'TUNNELS', 'TUNL'],
             ['TUNNEL ', 'TUNNL', 'TUNL'],
             ['TURNPIKE', 'TPK', 'TPKE'],
             ['TURNPIKE', 'TPKE', 'TPKE'],
             ['TURNPIKE', 'TRPK', 'TPKE'],
             ['TURNPIKE', 'TURNPIKE', 'TPKE'],
             ['TURNPIKE', 'TURNPK', 'TPKE'],
             ['TURNPIKE ', 'TRNPK', 'TPKE'],
             ['UNDERPASS', 'UNDERPASS', 'UPAS'],
             ['UNION', 'UN', 'UN'],
             ['UNION', 'UNION', 'UN'],
             ['UNIONS', 'UNIONS', 'UNS'],
             ['VALLEY', 'VALLEY', 'VLY'],
             ['VALLEY', 'VALLY', 'VLY'],
             ['VALLEY', 'VLLY', 'VLY'],
             ['VALLEY', 'VLY', 'VLY'],
             ['VALLEYS', 'VALLEYS', 'VLYS'],
             ['VALLEYS', 'VLYS', 'VLYS'],
             ['VIADUCT', 'VDCT', 'VIA'],
             ['VIADUCT', 'VIA', 'VIA'],
             ['VIADUCT', 'VIADCT', 'VIA'],
             ['VIADUCT', 'VIADUCT', 'VIA'],
             ['VIEW', 'VIEW', 'VW'],
             ['VIEW', 'VW', 'VW'],
             ['VIEWS', 'VIEWS', 'VWS'],
             ['VIEWS', 'VWS', 'VWS'],
             ['VILLAGE', 'VILL', 'VLG'],
             ['VILLAGE', 'VILLAGE', 'VLG'],
             ['VILLAGE', 'VILLG', 'VLG'],
             ['VILLAGE', 'VILLIAGE', 'VLG'],
             ['VILLAGE', 'VLG', 'VLG'],
             ['VILLAGE ', 'VILLAG', 'VLG'],
             ['VILLAGES', 'VILLAGES', 'VLGS'],
             ['VILLAGES', 'VLGS', 'VLGS'],
             ['VILLE', 'VILLE', 'VL'],
             ['VILLE', 'VL', 'VL'],
             ['VISTA', 'VIST', 'VIS'],
             ['VISTA', 'VISTA', 'VIS'],
             ['VISTA', 'VSTA', 'VIS'],
             ['VISTA ', 'VIS', 'VIS'],
             ['VISTA ', 'VST', 'VIS'],
             ['WALK', 'WALK', 'WALK'],
             ['WALKS', 'WALKS', 'WALK'],
             ['WALL', 'WALL', 'WALL'],
             ['WAY', 'WAY', 'WAY'],
             ['WAY', 'WY', 'WAY'],
             ['WAYS', 'WAYS', 'WAYS'],
             ['WELL', 'WELL', 'WL'],
             ['WELLS', 'WELLS', 'WLS'],
             ['WELLS', 'WLS', 'WLS']]
                
            
            
            
            
            
            def checkEnds(line, ends):
                for end in ends:
                    if line.endswith(end):
                        return True
            
            nullValues = [None, "0",0,"None", "none", "NONE", "","-99999","77777",77777, " ", "NA", "na", "N/A", "n/a","NULL","Null","<NULL>","null","<null>""<Null>","  ","   ","    ","     "]
            otherValues = [ "Other", "other", "OTHER","88888",88888]
            tbdValues = ["tbd","TBD","To be determined","Tbd",99999,"99999"]
            indetVals = nullValues+otherValues+tbdValues                         
            
            
            commonSuffixes = [el[1] for el in suffixes]
            standardSuffixes = [el[2] for el in suffixes]
            
            prefixes = [["NORTH","N"],
                        ["north","N"],
                        ["North","N"],
                        ["North ","N"],
                        ["N","N"],
                        ["N.","N"],
                        ["SOUTH", "S"],
                        ["south","S"],
                        ["South","S"],
                        ["South ","S"],
                        ["S","S"],
                        ["S.","S"],
                        ["WEST","W"],
                        ["west","W"],
                        ["West","W"],
                        ["West ","W"],
                        ["W","W"],
                        ["W.","W"],
                        ["EAST","E"],
                        ["east","E"],
                        ["East","E"],
                        ["East ","E"],
                        ["E","E"],
                        ["E.","E"]]
            
            commonPrefixes = [el[0] for el in prefixes]
            #commonPrefixes =[item for sublist in commonPrefixes for item in sublist]
            standardPrefixes = [el[-1] for el in prefixes]
            
            streetFields = [fld]
            
            with arcpy.da.UpdateCursor(fc, streetFields) as cursor:
                for row in cursor:
                    roadName = row[0]
                    if roadName is None:
                        pass
                    else:
                        roadNameVals = roadName.split(" ")
                        if len(roadNameVals) > 1:
                            for n, i in enumerate(roadNameVals):
                                new = str(i)
                                roadNameVals[n] = new
                            
                            for roadNameVal in roadNameVals:
                                roadNameVal = roadNameVal.upper()
                                if roadNameVal in commonSuffixes:
                                    idx1 = commonSuffixes.index(roadNameVal)
                                    newSuffix= standardSuffixes[idx1]
                                    idx2 =   roadNameVals.index(roadNameVal)
                                    roadNameVals[idx2] = newSuffix
                                    
                                if roadNameVal in commonPrefixes:
                                    idx1 = commonPrefixes.index(roadNameVal)
                                    newPrefix= standardPrefixes[idx1]
                                    idx2 =   roadNameVals.index(roadNameVal)
                                    roadNameVals[idx2] = newPrefix
                                else:
                                    pass
                
                            newName = ' '.join(roadNameVals)
                            newRow= [newName]
                            print "old row = "+str(row)
                            print "new row = "+str(newRow)
                            del newName
                            
                
                            del row
                            cursor.updateRow(newRow)
                                    
                        else:
                            pass