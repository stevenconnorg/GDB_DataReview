# CIP Data Review

## Overview

This repository provides various Python and R files to expedite common processes in reviewing AF Installation geodatabases for compliance to the SDSFIE 3.101 data model. In particular, this reposity provides custom ArcMap toolboxes to analyze a geodatabase's compliance with the SDSFIE 3.101 schema. 

## CIP_dataReview ArcMap Toolbox

The CIP_dataReview ArcMap Toolbox provides numerous Python script tools to expedite the review of AF Installation geodatabases in comparison with the SDSFIE 3.101 data model. The individual script tools included in the toolbox are described below.

### Find Duplicate Geometry
The Find Duplicate Geometry tool allows users to search an entire geodatabase's Feature Classes within Feature Datasets for features with duplicate geometries. This tool loops through each Feature Dataset's Feature Class features and searches for duplicate geometries. All features with duplicate geometries are written to the output .csv file, as specified, and describes the Feature Dataset and Feature Class with duplicate geometries, the OBJECTIDs of the duplicate geometries, and a summary, which gives the count of duplicate geometries spread over unique geometries, Further, this tool creates layer files for each Feature Class' duplicate features, allowing users to edit their geodatabase directory from a temporary, filtered layer of only duplicate features to be evaluated further.

### Clip GDB Features to Geometry

....


### Calculate Feature RPSUIDs from Overlapping Polygons

....


### Check and/or Repair Geometries

....


### Find Duplicate Features

....


### Join Fields and Calculate
This tool may be used to update the destination values in a target feature layer field with the values in another table's fields using a common key (join fields). This script is faster and more versatile than using a manual join/relate with ArcMap's Field Calculator.

### Standardize 'Building_A' Addresses

....


### Parse 'roadCenterline_L' Names with Prefix and Suffix
The purpose of this tool is to standardize the road prefix, road name, and road suffix values within the AF SDSFIE RoadCenterline_L feature class. This tool works by first searching the ROADNAME field within the RoadCenterline_L feature class, then removes any prefixes or suffixes within the field and moves them to the appropriate field. For all prefixes and suffixes found, the prefixes are reformatted to "N", "S", "E", and "W." For all suffixes found, the suffixes are reformatted to standard USPS suffixes.

### Batch Export Metadata to Directory

....


### Batch Import Metadata to Geodatabase Features

....


### Search for Indeterminant Data
Search a 'source' geodatabase for indeterminate data from feature dataset/feature class combinations in a target geodatabase. First, searches for missing feature datasets in target geodatabase not in source geodatabase. Then, searches for feature classes in 'x' feature dataset. Then, for each feature class in the source geodatabase, this tool searches for 'indeterminate' values in each field. Indeterminate values, here, means any null, to be determined (TBD), or 'other' values.

This tool creates 4 output tables, each prepended with the name of the Model_Geodatabase (e.g.: If you 'model' geodatabase is the SDSFIE CIP geodatabase, the tables will be called (CIP_MissingFDS, CIP_Missing_FCs, CIP_MissingFields, and CIP_MissingData). These tables include: 

	[modelGeodatabaseName]_MissingFDS


	[modelGeodatabaseName]_MissingFCs


	[modelGeodatabaseName]_MissingFields


	[modelGeodatabaseName]_MissingData 



### Summarise Indeterminant Data Tables

This script tool requires a few non-standard Python modules to run successfully, including the modules: numpy, pandas. To install these modules for use in ArcGIS, install the modules using the commands "pip install pandas" and "pip install numpy." To do this, 

	(1) press the windows key on your keyboard

	(2) type "cmd" to open the command prompt window

	(3) set your working directory as your ArcGIS Python scripts directory. This is typically located at C:\Python27\ArcGIS[versionNumber]\Scripts

	(3.1) (do this by typing 'cd C:\Python27\ArcGIS[versionNumber]\Scripts' and clicking enter). Replace [versionNumber] with you ArcGIS version number (e.g.: if you are running ArcMap10.6, input: "C:\Python27\ArcGIS10.6\Scripts"

	(4) type 'pip install numpy' and press enter, then type 'pip install pandas' and press enter. If all goes well, you will have these modules successfully installed for use in ArcGIS' Python distribution 

The inputs required for this tool to work are the 4 output tables created with the "Search for Indeterminate Data" script tool (please ensure these are all from the same comparison geodatabase):

	"[comparison GDB]_MissingFDS"

	"[comparison GDB]_MissingFCs"

	"[comparison GDB]_MissingFields"

	"[comparison GDB]_MissingData" 


This tool takes these 4 input tables and creates an outbook Excel Workbook (last parameter), which includes the following sheets:

Summary_by_FC gives: 
	the counts and percentages of 'Other', 'Null', and 'TBD' cells by Feature Class, as well as the total counts and percentages of indeterminate (Other + Null + TBD) and determinate cells (not Other, Null, or TBD), 

Summary_by_Field gives: 
	the same statistics as the Summary_by_FC sheet, but broken down further by Feature Class Fields,

Empty Feature Classes gives: 
	the standard Feature Classes in the comparison geodatabase not included in the input geodatabase(i.e.: Feature Classes included in comparison geodatabases)

Indeterminate_Overview, gives :

	total count of feature classes that are empty

	total number of standard feature classes that are empty

	the source geodatabase installation name

	the total number of missing feature classes

	the total number of missing feature datasets

	the total number of empty fields from empty feature classes

	the total number of empty fields from non-empty feature classes. 

## Indeterminant Data Reporting

First, using the 'fc2fds.py' script, move any lose feature classes within each geodatabase in the directory called "gdbs" to feature classes inside respective feature datasets in a new geodatabase in "gdbs-cleaned" directory, according to target geodatabase "Full.gdb"

Then, using the 'compareGDB_MissingData.py' file, compare a directory of geodatabases inside a 'gdbs-cleaned' directory with a directory of target directories in a 'gdbs-target' directory inside the main directory.  The 'compareGDB_MissingData.py' script searches the source geodatabase's feature datasets, feature classes, and fields for 'indeterminant' data (i.e.: Null, TBD, or 'other) compared with a series of target geodatabases. The output data is added to the source geodatabase (now in the 'gdbs-cleaned' directory) with the name of the target geodatabase prepended in front of the table name (e.g.: "Full_MissingData").

Then, after all source gdb/target gdb combinations are completed, the 'compareGDB_MissingData.py' script calls the 'Installation_Reports.R' script to knit the output data into pdf and html reports using the 'Installation_Report.Rmd' and 'Installation_Report-html.Rmd' files for each combination of source gdbs/target-gdbs.

All R packages utilized for the R Markdown pdf/html reports are maintained using the R package 'packrat' and recognized when utilizing the Installation_Feedpack.Rproj R project for reproducability. Do not manually edit any files in the 'packrat' directory -- only use packrat functions to maintain these dependencies. Please see packrat/bundles for the packrat project bundle.

