# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 07:33:44 2018

@author: stevenconnorg
"""
import os, pandas, arcpy

def getGDBpath(input_table):
  '''Return the Geodatabase path from the input table or feature class.
  :param input_table: path to the input table or feature class 
  '''
  workspace = os.path.dirname(input_table)
  if [any(ext) for ext in ('.gdb', '.mdb', '.sde') if ext in os.path.splitext(workspace)]:
    return workspace
  else:
    return os.path.dirname(workspace)

def getFeaturesdf(GDB):
    '''
    # to get unique FDS, FC, and FIELDS across a geodatabase
    Parameters
    ----------
    GDB = path to GDB
    
    Returns
    -------
    pandas dataframe of with two columns: Feature Dataset, Feature Class for each fc in gdb.
    '''

    d = pandas.DataFrame([])
    arcpy.env.workspace = GDB
    for theFDS in arcpy.ListDatasets():
        for theFC in arcpy.ListFeatureClasses(feature_dataset=theFDS):
            minFields = (fld.name.upper() for fld in arcpy.ListFields(os.path.join(GDB,theFDS,theFC)) if str(fld.name) not in ['Shape', 'OBJECTID', 'Shape_Length', 'Shape_Area'])
            minFields = list(minFields)
            for FLD in minFields:
                d = d.append(pandas.DataFrame({'FDS': str(theFDS), 'FC': str(theFC), 'FLD': str(FLD.name)}, index=[0]), ignore_index=True)
    return(d)