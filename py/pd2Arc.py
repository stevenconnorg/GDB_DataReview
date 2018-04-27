# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 07:50:13 2018

@author: stevenconnorg
"""

import arcpy, numpy,  os, pandas 

def pandas_to_table(gdb,pddf,tablename):
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
    x.dtype.names = tuple(names)
    gdbTbl = os.path.join(gdb,tablename)
    if arcpy.Exists(gdbTbl):
        arcpy.Delete_management(gdbTbl)
    arcpy.da.NumPyArrayToTable(x, gdbTbl)
    
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