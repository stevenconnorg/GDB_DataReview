# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:40:13 2018

@author: stevenconnorg
"""

# 
import os
import pandas
import arcpy
import numpy

xlsx = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\CIP_DataReview\OSD RPI Site (For Components) FOUO.xlsx"
fc = "C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\installation_archives\\ANG_Peoria  - Copy\\Non_Network_CIP\\ANG_Peoria_CIP.gdb\\Cadastre\\Site_A"
gdb = "C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview\\installation_archives\\ANG_Peoria  - Copy\\Non_Network_CIP\\ANG_Peoria_CIP.gdb"

arcpy.env.workspace


def get_field_names(table):
    """
    Get a list of field names not inclusive of the geometry and object id fields.
    
    Parameters
    ----------
    table: Table readable by ArcGIS
    Returns
    -------
    List of field names.
    """
    # list to store values
    field_list = []

    # iterate the fields
    for field in arcpy.ListFields(table):

        # if the field is not geometry nor object id, add it as is
        if field.type != 'Geometry' and field.type != 'OID':
            field_list.append(field.name)

        # if geomtery is present, add both shape x and y for the centroid
        elif field.type == 'Geometry':
            field_list.append('SHAPE@XY')

    # return the field list
    return field_list

# to convert arcgis table to pandas dataframe
def table_to_pandas_dataframe(table, field_names=None):
    """
    Load data into a Pandas Data Frame from esri geodatabase table for subsequent analysis.
    
    Parameters
    ----------
    table = Table readable by ArcGIS.
    field_names: List of fields.
    Returns
    -------
    Pandas DataFrame object.
    
    """
    # if field names are not specified
    if not field_names:

        # get a list of field names
        field_names = get_field_names(table)

    # create a pandas data frame
    dataframe = pandas.DataFrame(columns=field_names)

    # use a search cursor to iterate rows
    with arcpy.da.SearchCursor(table, field_names) as search_cursor:

        # iterate the rows
        for row in search_cursor:

            # combine the field names and row items together, and append them
            dataframe = dataframe.append(
                dict(zip(field_names, row)), 
                ignore_index=True
            )

    # return the pandas data frame
    return dataframe


# to get a pandas dataframe into a arcgis table
def pandas_to_table(pddf,tablename):
    '''
    Parameters
    ----------
    pddf = pandas dataframe
    tablename = output table name to 'installGDB'
    
    Returns
    -------
    a geodatabase table from pandas dataframe inside 'installGDB' geodatabase object (string to .gdb path)
    '''
    x = numpy.array(numpy.rec.fromrecords(pddf))
    names = pddf.dtypes.index.tolist()
    for i,item in enumerate(names):
        newName = (item,str(item).replace(' ', '_'))[-1]
        names[i] = newName
    x.dtype.names = tuple(names)
    gdbTbl = os.path.join(arcpy.env.workspace,tablename)
    if arcpy.Exists(gdbTbl):
        arcpy.Delete_management(gdbTbl)
    arcpy.da.NumPyArrayToTable(x, gdbTbl)
    
    
def feature_class_to_pandas_data_frame(feature_class, field_list):
    """
    Load data into a Pandas Data Frame for subsequent analysis.
    :param feature_class: Input ArcGIS Feature Class.
    :param field_list: Fields for input.
    :return: Pandas DataFrame object.
    """
    return DataFrame(
        arcpy.da.FeatureClassToNumPyArray(
            in_table=feature_class,
            field_names=field_list,
            skip_nulls=False,
            null_value=-99999
        )
    )
        
        
fcFields = []
arcpy.env.workspace =gdb
from pandas import DataFrame


for fds in arcpy.ListDatasets():
    for fc in arcpy.ListFeatureClasses(wild_card = "Site_A",feature_dataset=fds):
        for fld in arcpy.ListFields(fc):
            fcFields.append(fld.name)

iDat = pandas.DataFrame( [row for row in arcpy.da.SearchCursor(fc, fcFields) ] )

dDat = pandas.read_excel(xlsx)


disDat = dDat.loc[dDat['RPAD Submitter'] == 'AF']

g = disDat.columns.to_series().groupby(disDat.dtypes).groups
g

list(disDat)
dRPSUID = disDat.RPSUID.unique()
dRPSUID = list(dRPSUID)

iDat.columns = fcFields
iRPSUID = iDat.realPropertySiteUniqueID.unique()
iRPSUID = list(iRPSUID)

iRPSUID = [str(x) for x in iRPSUID]
dRPSUID = [str(x) for x in dRPSUID]


# =============================================================================
# missing = set(dRPSUID) - set(iRPSUID)
# mRPSUIDs = [ x for x in missing ]
#  
# extra = set(iRPSUID) - set(dRPSUID)
# exRPSUIDs = [ x for x in extra ]
#  
# =============================================================================

missing = list(numpy.setdiff1d(dRPSUID,iRPSUID))
extra = list(numpy.setdiff1d(iRPSUID,dRPSUID))
isIn=[]
for val in iRPSUID:
    if val in dRPSUID:
        isIn.append(val)


newDf = disDat

pandas.options.mode.chained_assignment = None  # default='warn'
disDat = disDat.assign(missingRPSUID=None)


newDf[['RPSUID']] = newDf[['RPSUID']].astype(str)

## 
len(disDat)
# disDat_M = disDat[disDat['RPSUID'].isin(missing)]
missingIndices = disDat['RPSUID'].isin(missing)
missingIndices = disDat[missingIndices]
missingIndices
# disDat_M = disDat[disDat['RPSUID'].isin(missing)]
extraIndices = disDat['RPSUID'].isin(extra)
extraIndices = disDat[extraIndices]
extraIndices

# disDat_M = disDat[disDat['RPSUID'].isin(missing)]
inIndices = disDat['RPSUID'].isin(isIn)
inIndices = disDat[inIndices]
inIndices

disDat.missingRPSUID.loc[missingIndices.index] = "Missing in Geodatabase"
disDat.missingRPSUID.loc[extraIndices.index] = "Non-SDS"
disDat.missingRPSUID.loc[inIndices.index] = "Not Missing"

outName = (xlsx,xlsx.replace(' ', '_'))[-1]
writer = pandas.ExcelWriter(outName)
disDat.to_excel(writer)
writer.save()

disDat.columns = list(disDat)
pandas_to_table(disDat,"Missing_RPSUIDS")



