# GDB Data Review

## Overview

This repository provides various Python and R files to expedite common processes in reviewing geodatabases for compliance to a template geodatabase data model. In particular, this reposity provides custom ArcMap toolboxes to analyze a geodatabase's compliance with a template geodatabase schema. 

## GDB_DataReview ArcMap Toolbox

The GDB_DataReview ArcMap Toolbox provides numerous Python script tools to expedite the review of geodatabases in comparison with a template geodatabase model. The individual script tools included in the toolbox are described below.

### Find Duplicate Geometry
The Find Duplicate Geometry tool allows users to search an entire geodatabase's Feature Classes within Feature Datasets for features with duplicate geometries. This tool loops through each Feature Dataset's Feature Class features and searches for duplicate geometries. All features with duplicate geometries are written to the output .csv file, as specified, and describes the Feature Dataset and Feature Class with duplicate geometries, the OBJECTIDs of the duplicate geometries, and a summary, which gives the count of duplicate geometries spread over unique geometries, Further, this tool creates layer files for each Feature Class' duplicate features, allowing users to edit their geodatabase directory from a temporary, filtered layer of only duplicate features to be evaluated further.

### Clip GDB Features to Geometry

This tool loops through all Feature Classes within Feature Datasets in a source geodatabase, then clips each feature within each Feature Class to the 'Clip Feature' parameter. All clipped Feature Classes are added to a new, output geodatabase that follows the same Feature Dataset/Feature Class geodatabase structure and has the same coordiante reference system as the source geodatabase.

### Calculate Feature RPSUIDs from Overlapping Polygons
This tool utilizes spatial joins to update field values in the target Feature Classes field to equal the source Feature Class fields in a source geodatabase. Using 'wildcard' fitlers, this tool allows users to update particular target Feature Datasets, Feature Classes, and Fields. For the purposes of this tool within the scope of the CIP Data Review task, target Fields are, by default, any fields that begin with "realPropertySiteUnique," in order to udpate RPSUID fields called either "realPropertySiteUniqueIdentifier" or "realPropertySiteUniqueID"; however, this tool could be extended to any number of source/target Feature Class/Field values. 

### Check and/or Repair Geometries
The Check and/or Repair Geometries tool allows users to search an entire geodatabase’s Feature Classes for
geometry problems. This tool loops through each Feature Dataset’s Feature Class features and searches for
geometry problems, including null geometry, self intersections, duplicate vertexes, and more.
If geometry problems exists, an output table is created containing the following fields: CLASS, FEATURE_
ID, and PROBLEM. The feature classes which contain geometry problems are then repaired.
After the repair is conducted, the subset of feature classes with repaired geometry problems are checked
again for geometry problems to confirm their repair. Another output table is generated for the subset of
feature classes. An empty output table confirms the geometry problems were correctly repaired.

### Find Duplicate Features
The Find Duplicate Features tool allows users to search an entire geodatabase's Feature Classes within Feature Datasets for features with duplicate features. For this tool, duplicate features include any Feature Class' fields not including the geometry, Shape_Area, or Shape_Length fields. This tool loops through each Feature Dataset's Feature Class features and searches for duplicate features across all other fields. All features with duplicate features are written to the output .csv file, as specified, and describes the Feature Dataset and Feature Class with duplicate features, the OBJECTIDs of the duplicate features, and a summary narrative, which gives the count of unique duplicate features. Further, this tool creates layer files for each Feature Class' duplicate features, allowing users to edit their geodatabase directory from a temporary, filtered layer of only duplicate features to be evaluated further.



### Join Fields and Calculate
This tool may be used to update the destination values in a target feature layer field with the values in another table's fields using a common key (join fields). This script is faster and more versatile than using a manual join/relate with ArcMap's Field Calculator.

### Standardize Feature Class Addresses
The purpose of this tool is to standardize 1 field a feature class. This tool works by first searching the address field within the input feature class, then replaces any street prefixes (e.g.: North, north, East, West) are reformatted to "N", "S", "E", and "W," while all suffixes (e.g.: AVE, Avenue, Street) are reformatted to [standard USPS suffixes](https://github.com/allanbreyes/udacity-data-science/blob/master/p2/data/suffixes.csv).


### Parse Feature Class Road Names, Prefixes, and Suffixes
The purpose of this tool is to standardize the 3 field (road prefix, road name, and road suffix) values within a feature class. This tool works by first searching the ROADNAME field within that feature class, then removes any prefixes or suffixes within the field and moves them to the appropriate field. For all prefixes and suffixes found, the prefixes are reformatted to "N", "S", "E", and "W." For all suffixes found, the suffixes are reformatted to standard USPS suffixes.

### Batch Export Metadata to Directory
For each Feature Dataset and Feature Class (within Feature Datasets) in the input geodatabase, this tool exports each item's metadata to an .xml file to an output directory. This tool allows you to specify a metadata translator, by defaulting using one of ArcGIS standard translators "ARCGIS2FGDC.xml" (typically located at "C:\Program Files (x86)\ArcGIS\Desktop10.6\Metadata\Translator\", but you may specify any translator. If the source metadata is a Feature Dataset, the output .xml file is named after the Feature Dataset. Alternatively, the out .xml metadata for Feature Classes are exported with the Feature Dataset name prepended before the Feature Class name.

### Batch Import Metadata to Geodatabase Features
Similar to the 'Batch Export Metadata to Directory tool,' this tool imports a directory of .xml metadata files geodatabase feature classes. Using the .xml naming conventions explicated in the 'Batch Export Metadata to Directory,' this tool automatically matches the .xml file to the respective Feature Dataset or Feature Class.


### Search for Indeterminant Data
Search a 'source' geodatabase for indeterminate data from feature dataset/feature class combinations in a target geodatabase. First, searches for missing feature datasets in target geodatabase not in source geodatabase. Then, searches for feature classes in 'x' feature dataset. Then, for each feature class in the source geodatabase, this tool searches for 'indeterminate' values in each field. Indeterminate values, here, means any null, to be determined (TBD), or 'other' values.

This tool creates 4 output tables, each prepended with the name of the Model_Geodatabase (e.g.: If your 'model' geodatabase called 'CIP', the tables will be called (CIP_MissingFDS, CIP_Missing_FCs, CIP_MissingFields, and CIP_MissingData). These tables include: 

	[modelGeodatabaseName]_MissingFDS
	[modelGeodatabaseName]_MissingFCs
	[modelGeodatabaseName]_MissingFields
	[modelGeodatabaseName]_MissingData

### Summarise Indeterminant Data Tables

This script tool requires a few non-standard Python modules to run successfully, including the modules: numpy, pandas. To install these modules for use in ArcGIS, install the modules using the commands "pip install pandas" and "pip install numpy." To do this, 

	(1) Press the windows key on your keyboard
	(2) Type "cmd" to open the command prompt window
	(3) Set your working directory as your ArcGIS Python scripts directory. This is typically located at C:\Python27\ArcGIS[versionNumber]\Scripts
	(3.1) Do this by typing 'cd C:\Python27\ArcGIS[versionNumber]\Scripts' and clicking enter. Replace [versionNumber] with you ArcGIS version number (e.g.: if you are running ArcMap10.6, input: "C:\Python27\ArcGIS10.6\Scripts"
	(4) Type 'pip install numpy' and press enter, then type 'pip install pandas' and press enter. If all goes well, you will have these modules successfully installed for use in ArcGIS' Python distribution 

The inputs required for this tool to work are the 4 output tables created with the "Search for Indeterminate Data" script tool (please ensure these are all from the same comparison geodatabase):

	"[comparison GDB]_MissingFDS"
	"[comparison GDB]_MissingFCs"
	"[comparison GDB]_MissingFields"
	"[comparison GDB]_MissingData" 


This tool takes these 4 input tables and creates an outbook Excel Workbook (last parameter), which includes the following sheets:

The **Summary_by_FC** table gives: 

	the counts and percentages of 'Other', 'Null', and 'TBD' cells by Feature Class, as well as the total counts and percentages of indeterminate (Other + Null + TBD) and determinate cells (not Other, Null, or TBD), 

The **Summary_by_Field** table gives: 

	the same statistics as the Summary_by_FC sheet, but broken down further by Feature Class Fields,

The **Empty Feature Classes** table gives: 

	the standard Feature Classes in the comparison geodatabase not included in the input geodatabase(i.e.: Feature Classes included in comparison geodatabases)

The **Indeterminate_Overview** table , gives :

	(a) The total count of feature classes that are empty
	(b) The total number of standard feature classes that are empty
	(c) The source geodatabase installation name
	(d) The total number of missing feature classes
	(e) The total number of missing feature datasets
	(f) The total number of empty fields from empty feature classes
	(g) The total number of empty fields from non-empty feature classes. 

## Indeterminant Data Reporting

First, using the 'fc2fds.py' script, move any lose feature classes within each geodatabase in the directory called "gdbs" to feature classes inside respective feature datasets in a new geodatabase in "gdbs-cleaned" directory, according to target geodatabase "Full.gdb"

Then, using the 'compareGDB_MissingData.py' file, compare a directory of geodatabases inside a 'gdbs-cleaned' directory with a directory of target directories in a 'gdbs-target' directory inside the main directory.  The 'compareGDB_MissingData.py' script searches the source geodatabase's feature datasets, feature classes, and fields for 'indeterminant' data (i.e.: Null, TBD, or 'other) compared with a series of target geodatabases. The output data is added to the source geodatabase (now in the 'gdbs-cleaned' directory) with the name of the target geodatabase prepended in front of the table name (e.g.: "Full_MissingData").

Then, after all source gdb/target gdb combinations are completed, the 'compareGDB_MissingData.py' script calls the 'Installation_Reports.R' script to knit the output data into pdf and html reports using the 'Installation_Report.Rmd' and 'Installation_Report-html.Rmd' files for each combination of source gdbs/target-gdbs.

All R packages utilized for the R Markdown pdf/html reports are maintained using the R package 'packrat' and recognized when utilizing the Installation_Feedpack.Rproj R project for reproducability. Do not manually edit any files in the 'packrat' directory -- only use packrat functions to maintain these dependencies. Please see packrat/bundles for the packrat project bundle.

