#-------------------------------------------------------------------------------
# Name:        GIS Viewer Attribution Evaluation
# Version:     V_2.0
# Purpose:     Produce report for installation geodatabase detailing data attribution
#
# Author:      Steven Connor Gonzalez
#
# Created:     2018/01/26
# Last Update: 2018/04/30
#-------------------------------------------------------------------------------

# Import modules
import arcpy, os, collections, time
from datetime import datetime
from operator import itemgetter
from datetime import date

# Start time
timenow = datetime.now()
arcpy.AddMessage(timenow)


# within the main directory, create a directory called "gdbs" that houses all the geodatabase you want to compare.
installGDB = arcpy.GetParameterAsText(0)
compGDB = arcpy.GetParameterAsText(1)


# create table for missing data 
def createNullTable(installGDB,nullTableName="MissingData"):
    errorTable = os.path.join(installGDB,nullTableName)
    arcpy.CreateTable_management(installGDB,nullTableName)
    # Installation Name
    arcpy.AddField_management(errorTable, "INSTALLATION", "TEXT", field_length = 50) 
    # Name of Field
    arcpy.AddField_management(errorTable, "FDS", "TEXT", field_length = 50) 
    # Name of Field
    arcpy.AddField_management(errorTable, "FC", "TEXT", field_length = 50) 
    # Name of Field
    arcpy.AddField_management(errorTable, "FIELD", "TEXT", field_length = 50) 
    # is field missing? True/False
    arcpy.AddField_management(errorTable, "FIELD_NONSDS", "TEXT", field_length = 1)   
    # is feature class empty? True/False
    arcpy.AddField_management(errorTable, "EMPTY_FC", "TEXT", field_length = 1)         
    # How many NULL values per field?
    arcpy.AddField_management(errorTable, "NULL_FC_COUNT", "LONG",field_length =  50)      
    # How many TBD values per field?
    arcpy.AddField_management(errorTable, "TBD_FC_COUNT", "LONG", field_length = 50)      
    # How many OTHER values per field?
    arcpy.AddField_management(errorTable, "OTHER_FC_COUNT", "LONG",field_length =  50)     
    # break out of individual values and counts for Null, None, NA, etc...
    arcpy.AddField_management(errorTable, "NULL_VALUE_COUNTS", "TEXT", field_length = 32766)    # this is limit of characters that a cell can contain in .xlsx - 1
    # break out of individual values and counts for Null, None, NA, etc...
    arcpy.AddField_management(errorTable, "TBD_VALUE_COUNTS", "TEXT", field_length = 32766)     
    # break out of individual values and counts for Null, None, NA, etc...
    arcpy.AddField_management(errorTable, "OTHER_VALUE_COUNTS", "TEXT", field_length = 32766)   
    # total number of indeterminant values (NULLS + Others + TBD)
    arcpy.AddField_management(errorTable, "TOTAL_INDT_COUNT", "LONG", field_length = 50)   
    # total number of indeterminant values (NULLS + Others + TBD)
    arcpy.AddField_management(errorTable, "TOTAL_DET_COUNT", "LONG", field_length = 50)   
    # Total Number of populated values (not null, tbd, or other)
    arcpy.AddField_management(errorTable, "POP_VALS_COUNT", "LONG",field_length = 50)    
    # Total Number of populated values (not null, tbd, or other)
    arcpy.AddField_management(errorTable, "POP_VALS", "TEXT",field_length = 32766)
    # Total Number of populated values (not null, tbd, or other)
    arcpy.AddField_management(errorTable, "INC_POP_VALS", "TEXT",field_length = 32766)
    arcpy.AddMessage (nullTableName + " Table Created in " + os.path.splitext(os.path.basename(installGDB) + "gdb")[0])
 
 # create table for missing fields
def createMissingFLDtbl(installGDB,missingFLDTblName="MissingFields"):
    errorTable = os.path.join(installGDB,missingFLDTblName)
    arcpy.CreateTable_management(installGDB,missingFLDTblName)
    # is feature class empty? True/False
    arcpy.AddField_management(errorTable, "FDS", "TEXT", field_length = 50)
    # is feature class missing? True/False
    arcpy.AddField_management(errorTable, "FC", "TEXT",field_length =  50)   
    # is feature class missing? True/False
    arcpy.AddField_management(errorTable, "FIELD_MISSING", "TEXT", field_length = 50)   
    # Installation Name
    arcpy.AddField_management(errorTable, "INSTALLATION", "TEXT", field_length = 100)  
    arcpy.AddMessage (missingFLDTblName + " Table Created in " + os.path.splitext(os.path.basename(installGDB) + "gdb")[0])

# create table for missing feature classes 
  
def createMissingFCtbl(installGDB,missingFCTblName="MissingFCs"):
    errorTable = os.path.join(installGDB,missingFCTblName)
    arcpy.CreateTable_management(installGDB,missingFCTblName)
    # is feature class missing? True/False
    arcpy.AddField_management(errorTable, "FC_MISSING", "TEXT", field_length = 50)   
    # is feature class missing? True/False
    arcpy.AddField_management(errorTable, "FDS", "TEXT",field_length =  50)  
    # Installation Name
    arcpy.AddField_management(errorTable, "INSTALLATION", "TEXT",field_length =  100)  
    arcpy.AddMessage (missingFCTblName + " Table Created in " + os.path.splitext(os.path.basename(installGDB) + "gdb")[0])

	# create table for missing feature datasets 
def createMissingFDstbl(installGDB,missingFDTblName="MissingFDS"):
    errorTable = os.path.join(installGDB,missingFDTblName)
    arcpy.CreateTable_management(installGDB,missingFDTblName)
    # is feature class empty? True/False
    arcpy.AddField_management(errorTable, "FDS_MISSING", "TEXT",field_length =  50)
    # Installation Name
    arcpy.AddField_management(errorTable, "INSTALLATION", "TEXT", field_length = 100)         
    arcpy.AddMessage (missingFDTblName + " Table Created in " + os.path.splitext(os.path.basename(installGDB) + "gdb")[0])


# to get field name of a ArcGIS table
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



# main function to compare missing data from source geodatabase compared with target geodatabase schema
def compareGDBs(installGDB,compGDB):
    '''
    Parameters
    ----------
        installGDB = geodatabase to be compared against 'compGDB'
        compGDB    = geodatabase that install GDB is compared against
        
        
    Returns
    -------
        MissingFDS (table)    : which feature datasets are missing in the installGDB that are included in compGDB?
            - fields within MissingFDS Table
                1) INSTALLATION - name of installGDB
                2) FDS_MISSING - name of feature dataset missing
    
        MissingFC  (table)    : within feature datasets correctly included, which feature classes are missing?
            - fields within MissingData Table
                1) INSTALLATION - name of installGDB
                2) FDS - name of feature dataset for feature class being analyzed
                3) FC_MISSING- name of feature class missing
    
    
        MissingFields (table) : within the feature dataset/feature class combo correctly included, which fields are missing?
            - fields within MissingData Table
                1) INSTALLATION - name of installGDB
                2) FDS - name of feature dataset for field being analyzed
                3) FC- name of feature feature class for field being analyzed
                4) FIELD_MISSING - name of field missing from feature dataset/feature class that is included in the comparison GDB.
    
    
        MissingData (table)   : within the feature dataset/feature class combo correctly included, what data is missing?
            - fields within MissingData Table
                1) INSTALLATION - name of installGDB
                2) FDS - name of feature dataset for field being analyzed
                3) FC- name of feature feature class for field being analyzed
                4) FIELD - name of field being analyzed
                5) FIELD_NONSDS - True or False? If the field is not included in compGDB == T
                6) EMPTY_FC - is this feature class empty? T/F
                7) NULL_FC_COUNT - the count of features with NULL values within field. NULL values are counted if cell equals any of following:  [None, "None", "none", "NONE", "",99999,-99999, " ", "NA", "N/A", "n/a","NULL","Null","<NULL>","<Null>"]
                8) TBD_FC_COUNT - the count of features with TBD values within field. TBD values are counted if cell equals any of following: ["tbd","TBD","To be determined"]
                9) OTHER_FC_COUNT - the count of features with OTHER values within field. OTHER values are counted if cell equals any of following:  [ "Other", "other", "OTHER"]
                10) NULL_VALUE_COUNTS - the individual counts of each unique entry for NULL cells. e.g.: " '' has 1 feature. ' '  has 1 feature. 'None' has 2 feature. "
                11) TBD_VALUE_COUNTS - the individual counts of each unique entry for TBD cells. e.g.: " 'tbd' has 1 feature. 'TBD'  has 1 feature. 'To be determined' has 2 feature. "
                12) OTHER_VALUE_COUNTS - the individual counts of each unique entry for OTHER cells. e.g.: " 'OTHER' has 1 feature. 'other'  has 1 feature. 'Other' has 2 feature. "
                13) TOTAL_INDT_COUNT - total count of cells with INDETERMINANT values (i.e.: Null, TBD, or Other values) per field
                14) TOTAL_DET_COUNT - total count of cells with DETERMINANT values (i.e.: NOT Null, NOT TBD, or NOT Other values) per field
                15) POP_VALS_COUNT  - total count of features POPULATED (either INDETERMINANT or DETERMINANT) within fields
                16) POP_VALS - the individual counts of each unique entry for DETERMINED (not null, tbd, or other) cells that are 'correctly' populated (i.e.: adheres to domain-contraint or text in non-domain contrained field) e.g.: "'BX Exchange' has 1 feature. 'Homestead Air Reserve Base' has 2 feature. U.S. 'Customs Ramp Area' has 1 feature."
                17) INC_POP_VALS - the individual counts of each unique entry for DETERMINED (not null, tbd, or other) cells that are 'incorrectly' populated (i.e.: DOES NOT adhere to domain-contrained field)  e.g.: "'9999' has 1 feature. '341' has 1 feature. '343' has 1 feature. "
    
    
    Example
    -------
    compareGDBs(comparisonGDB.gdb,targetGDB.gdb)
    
    '''

    start_time = datetime.now()
    
    arcpy.env.workspace = installGDB
    installationName = os.path.splitext(os.path.basename(installGDB))[0]
    compName = os.path.splitext(os.path.basename(compGDB))[0]
    
    # remove any locks that might exist on the installation gdb
    arcpy.AddMessage("Removing any locks on " + installationName+".gdb")
    def clearWSLocks(inputWS):
        '''Attempts to clear locks on a workspace, returns stupid message.'''
        if all([arcpy.Exists(inputWS), arcpy.Compact_management(inputWS), arcpy.Exists(inputWS)]):
            return 'Workspace (%s) clear to continue...' % inputWS
        else:
            return '!!!!!!!! ERROR WITH WORKSPACE %s !!!!!!!!' % inputWS
    clearWSLocks(installGDB)
    
    # output table names, with comparison geodatabase name prepended
    missingFDTblName=compName+"_MissingFDS"
    missingFCTblName=compName+"_MissingFCs"
    missingFLDTblName=compName+"_MissingFields"
    nullTableName=compName+"_MissingData"

    # IF THE TABLE EXISTS, DELETE ROWS,
    # ELSE CREATE ERROR TABLE FOR EACH FEATURE DATASET IN COMPGDB
    
    ### TK put this table creation part in a loop
    
    # CREATE MISSING FEATURE DATASET TABLE
    if arcpy.Exists(os.path.join(installGDB,missingFDTblName)): 
        arcpy.Delete_management(os.path.join(installGDB,missingFDTblName))
        arcpy.AddMessage (missingFDTblName + " Table already exists in " + os.path.splitext(os.path.basename(installGDB) )[0]+ ".gdb -- REPLACING")
        createMissingFDstbl(installGDB,missingFDTblName)
    else:
        createMissingFDstbl(installGDB,missingFDTblName)
    
    # CREATE MISSING FEATURE CLASS TABLE
    if arcpy.Exists(os.path.join(installGDB,missingFCTblName)): 
        arcpy.Delete_management(os.path.join(installGDB,missingFCTblName))
        arcpy.AddMessage (missingFCTblName + " Table already exists in " + os.path.splitext(os.path.basename(installGDB) )[0]+ ".gdb -- REPLACING")
        createMissingFCtbl(installGDB,missingFCTblName)
    else:
        createMissingFCtbl(installGDB,missingFCTblName)
    
    # CREATE MISSING FIELD TABLE
    if arcpy.Exists(os.path.join(installGDB,missingFLDTblName)): 
        arcpy.Delete_management(os.path.join(installGDB,missingFLDTblName))
        arcpy.AddMessage (missingFLDTblName + " Table already exists in " + os.path.splitext(os.path.basename(installGDB) )[0]+ ".gdb -- REPLACING")
        createMissingFLDtbl(installGDB,missingFLDTblName)
    else:
        createMissingFLDtbl(installGDB,missingFLDTblName)
    
    # CREATE NULL DATA TABLE
    if arcpy.Exists(os.path.join(installGDB,nullTableName)): 
        arcpy.Delete_management(os.path.join(installGDB,nullTableName))
        arcpy.AddMessage (nullTableName + " Table already exists in " + os.path.splitext(os.path.basename(installGDB) )[0]+ ".gdb -- REPLACING")
        createNullTable(installGDB,nullTableName)
    else:
        createNullTable(installGDB,nullTableName)        
    
        
    edit = arcpy.da.Editor(arcpy.env.workspace)
    edit.startEditing(False, False)
    edit.startOperation()

    # WITHIN EACH REQUIRED FEATURE DATASET AND FEATURE CLASS THAT THE INSTALLATION HAS, 
    # WHICH FIELDS ARE MISSING?
    
    nullTable = os.path.join(installGDB,nullTableName)
    nullrows = arcpy.InsertCursor(nullTable)

    # WITHIN EACH REQUIRED FEATURE DATASET AND FEATURE CLASS THAT THE INSTALLATION HAS, 
    # WHICH FIELDS ARE MISSING?
    missFLDTable = os.path.join(installGDB,missingFLDTblName)
    fldrows = arcpy.InsertCursor(missFLDTable)
        
    # WITHIN THE FEATURE DATASETS THAT THE INSTALLATION HAS, 
    # WHICH FEATURE CLASSES ARE MISSING?
    missFCTable = os.path.join(installGDB,missingFCTblName)
    fcrows = arcpy.InsertCursor(missFCTable)

    
    # WHICH FEATURE DATASETS ARE MISSING FROM THE INSTALLATION DATABASE COMPARED TO COMPARISON DATABASE
    missFDSTable = os.path.join(installGDB,missingFDTblName)
    fdrows = arcpy.InsertCursor(missFDSTable)
    

    ## THEN WORK ON MISSING DATA
    arcpy.env.workspace = compGDB
    theFDSs = list(arcpy.ListDatasets())
    for theFDS in theFDSs:
        arcpy.env.workspace = compGDB
        theFCs = list(arcpy.ListFeatureClasses(feature_dataset=theFDS))
        for theFC in theFCs:
            time_elapsed = datetime.now() - start_time  
            arcpy.AddMessage('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
            
            today = date.today()
            timenow = time.strftime('%I:%M:%S-%p')
            printDate = today.strftime('%mm_%dd_%Y')
            arcpy.AddMessage(": Comparing "+installationName + " to " +compName+"      ---  " + printDate + " at " + timenow + " ---  Feature : " + theFDS + "//" + theFC )     
            # CHECK FOR EXISTANCE OF REQUIRED FEATURE DATASET 
            if arcpy.Exists(os.path.join(installGDB,str(theFDS).upper())):
               # CHECK FOR EXISTANCE OF REQUIRED FEATURE CLASS in FEATURE DATASET
                if arcpy.Exists(os.path.join(installGDB,str(theFDS).upper(),str(theFC).upper())):
                    minFields = (fld.name.upper() for fld in arcpy.ListFields(os.path.join(compGDB,theFDS,theFC)) if fld.name not in ['Shape'.upper(), 'OBJECTID', 'Shape_Length'.upper(), 'Shape_Area'.upper()])
                    minFl = list(minFields)
                    minF = [x.upper() for x in minFl]
                    #reqDomains = (fld.domain for fld in arcpy.ListFields(os.path.join(compGDB,theFDS,theFC)) if str(fld.name) not in ['Shape', 'OBJECTID', 'Shape_Length', 'Shape_Area'])
                            
                    minFieldsInstall = (fld.name.upper() for fld in arcpy.ListFields(os.path.join(installGDB,theFDS,theFC)) if fld.name not in ['Shape'.upper(), 'OBJECTID', 'Shape_Length'.upper(), 'Shape_Area'.upper()])
                    minFlInstall_l = list(minFieldsInstall)
                    minFlInstall = [x.upper() for x in minFlInstall_l]
                    
                    # CHECK FOR EXISTANCE OF REQUIRED FIELD in FEATURE CLASS
                    def findField(fc, fi):
                        fieldnames = [field.name.upper() for field in arcpy.ListFields(fc)]
                        if fi.upper() in fieldnames:
                            return True
                        else:
                            return False
                    # IF required field exists....
                    for theFLD in minFlInstall:
                        arcpy.env.workspace = installGDB
                        row = nullrows.newRow()
                        ignoreFLD = ['Shape'.upper(), 'OBJECTID'.upper(), 'Shape_Length'.upper(), 'Shape_Area'.upper()]
                        if theFLD not in ignoreFLD:           
                                                        
                            if theFLD not in minF:
                                arcpy.AddMessage(theFLD + " *NOT* included in "+compName+"/"+theFC+" fields")
                                row.setValue("FIELD_NONSDS", "T")
                            else:
                                arcpy.AddMessage(theFLD + " included in "+compName+"/"+theFC+" fields")
                                row.setValue("FIELD_NONSDS", "F")
                                
                            with arcpy.da.SearchCursor(os.path.join(installGDB,theFDS,theFC), theFLD.upper()) as cur:
                                row.setValue("FIELD", theFLD)
                                
                                instFCFields = [(afld.name.upper(), afld) for afld in arcpy.ListFields(os.path.join(installGDB,theFDS,theFC))]
                                domains = arcpy.da.ListDomains()
                                idx = map(itemgetter(0), instFCFields).index(theFLD)
                                row.setValue("FDS", theFDS)
                                row.setValue("FC", theFC)
                                
                                #CREATE SEARCH CURSOR ON FDS, FC, AND FIELDS TO BUILD LIST OF VALUES AND COUNTS
                                #with arcpy.da.SearchCursor(os.path.join(installGDB,"Recreation","RecArea_A"), str("recreationAreaType").upper()) as cur:
                                nullValues = [None, "None", "none", "NONE", "","-99999","77777",77777, " ", "NA", "na", "N/A", "n/a","NULL","Null","<NULL>","null","<null>""<Null>","  ","   ","    ","     "]
                                otherValues = [ "Other", "other", "OTHER","88888",88888]
                                tbdValues = ["tbd","TBD","To be determined","Tbd",99999,"99999"]
                                #indtList = nullValues + otherValues+ tbdValues
                                
                                ## GET TOTAL COUNT OF VALUES
                                countValues = collections.Counter(row[0] for row in cur)
                                sumValues = sum(collections.Counter(countValues).values())
        
                                # GET TOTAL COUNT OF 'NULL' VALUES for each NULL VALUE 'CODE'
                                countNulls = list((n[0], n[1]) for n in countValues.items() if n[0] in nullValues)
                                sumNulls = sum(n[1] for n in countNulls)
                                
                                # GET TOTAL COUNT OF 'TBD' VALUES for each NULL VALUE 'CODE'
                                countTBD = list((n[0], n[1]) for n in countValues.items() if n[0] in tbdValues)
                                sumTBD = sum(n[1] for n in countTBD)
                                
                                # GET TOTAL COUNT OF 'OTHER' VALUES for each NULL VALUE 'CODE'
                                countOthers = list((n[0], n[1]) for n in countValues.items() if n[0] in otherValues)                             
                                sumOther = sum(n[1] for n in countOthers)

                                sumIndt = sumNulls + sumTBD + sumOther
                                sumDetr = sumValues - sumIndt
                                
                                
                                #populate counts of populated values, nulls, tbds, and others
                                row.setValue("INSTALLATION",installationName)
                                row.setValue("POP_VALS_COUNT",sumValues)
                                row.setValue("NULL_FC_COUNT",sumNulls)
                                row.setValue("TBD_FC_COUNT",sumTBD)
                                row.setValue("OTHER_FC_COUNT",sumOther)             
                                row.setValue("TOTAL_INDT_COUNT", sumIndt)
                                row.setValue("TOTAL_DET_COUNT", sumDetr)
                                                        
                                
                                if sumValues == 0:                                
                                    row.setValue("EMPTY_FC", "T")
                                else:
                                    row.setValue("EMPTY_FC", "F")
                                    
                                indtArray=[[countOthers,"OTHER_VALUE_COUNTS"],[countTBD,"TBD_VALUE_COUNTS"],[countNulls,"NULL_VALUE_COUNTS"]]
                                
                                for indtCounts in indtArray:
                                    Strings = str()
                                    if not indtCounts[0]: # if list is empty, pass
                                        pass
                                    else:
                                        
                                        arcpy.AddMessage (indtCounts[0])
                                        for element in indtCounts[0]:
                                            if element[0] is None:
                                                    value = "NULL"
                                            elif element[0] is int or type(element[0]) is float or type(element[0]) is int or type(element[0]) is datetime or type(element[0]) is tuple:
                                            #elif element[0] is not str:
                                                value =unicode(str(element[0]).encode('utf-8'), errors="ignore")
                                            else:
                                                value =unicode(element[0].encode('utf-8'), errors="ignore")
                                            count =str(element[1])     
                                            if int(count) < 2 :
                                                valCount = count+" feature is '"+value+"'. "
                                                Strings = Strings + valCount
                                            else:
                                                valCount = count+" features are '"+value+"'. "
                                                Strings = Strings + valCount 
                                    row.setValue(indtCounts[1], Strings)
                                
                                
                                domainName = map(itemgetter(1), instFCFields)[idx].domain
                                domainVals = []
                                domainRng = []
                                
                                for domain in domains:
                                        if domain.name == domainName:
                                            if domain.domainType == 'CodedValue':
                                                domainVals = [val for val, desc in domain.codedValues.items()]
                                            elif domain.domainType == 'Range':
                                                domainRng = range(int(domain.range[0]), int((domain.range[1]+1)))
                                        #for domain.name not in reqDomains:
                                            #.... 
                          
            
                                
                                # get list of counts for each unique value in field
                                vals = sorted(countValues.items(), key=lambda x:x[1])
                                
                                # set and remove all values that have TBD, OTHER, or NULL
                                vals = set(vals) - set(countTBD) - set(countOthers) - set(countNulls)
                                
                                # get set back to list
                                vals = list(vals)
                                
                                # create empty string to concatenate each value
                                
                                ## valstr = 'correctly' populated values (either conforms to domain, or text in non-domain contrained field)
                                ## incvalstr = incorrectly populated values (values not in accordance with domain)
                                valstr = str()
                                incvalstr = str()                             
                                
                                if not vals:
                                    pass
                                else:
                                    for v in vals:
                                        # OPEN TEXT FIELDS; NO DOMAIN CONSTRAINT
                                        
                                        if (domainVals == [] and domainRng == []) or (domainVals != [] and v[0] in domainVals) or (domainRng != [] and v[0] in domainRng): 
                                            if v[0] is None:
                                                dom = "NULL"
                                            elif v[0] is int or type(v[0]) is float or type(v[0]) is int or type(v[0]) is datetime or type(v[0]) is tuple:
                                            #elif v[0] is not str:
                                                dom =unicode(str(v[0]).encode('utf-8'), errors="ignore")
                                            else:
                                                dom =unicode(v[0].encode('utf-8'), errors="ignore")
                                            val =str(v[1])
                                            if val < 2:
                                                domCount = val+" feature is '"+dom+"'. "
                                                valstr = valstr + domCount +". "
                                            else:
                                               domCount = val+" features are '"+dom+"'. "
                                               valstr = valstr + domCount 
                                        # INCORRECTLY POPULATED VALUES WITHIN DOMAIN CONSTRAINED FIELDS
                                        else:    
                                            if v[0] is None:
                                                dom = "NULL"
                                            elif v[0] is int or type(v[0]) is float or type(v[0]) is int or type(v[0]) is datetime or type(v[0]) is tuple:
                                            # elif v[0] is not str:
                                                dom =unicode(str(v[0]).encode('utf-8'), errors="ignore")
                                            else:
                                                dom =unicode(v[0].encode('utf-8'), errors="ignore")
                                            val =str(v[1])
                                            if val < 2:
                                                domCount = val+" feature is '"+dom+"'. "
                                                incvalstr = incvalstr + domCount 
                                            else:
                                               domCount = val+" features are '"+dom+"'. "
                                               incvalstr = incvalstr + domCount 
                                
                                if len(valstr) > 32766:
                                    valstr = "Unique value counts exceed field character limit -- not listed here."
                                elif len(incvalstr) > 32766:
                                    incvalstr = "Unique value counts exceed field character limit -- not listed here."
                                else:
                                    # remove last comma at end of value string 
                                    row.setValue("POP_VALS",valstr)  
                                    row.setValue("INC_POP_VALS",incvalstr)  
                                    nullrows.insertRow(row)
                        else:
                            pass
                        del row
                    for mF in minF:
                        if mF not in minFlInstall:
                            fldrow = fldrows.newRow()
                            fldrow.setValue("FDS", theFDS)
                            fldrow.setValue("FC", theFC)
                            fldrow.setValue("FIELD_MISSING", mF)
                            fldrow.setValue("INSTALLATION", installationName)
                            fldrows.insertRow(fldrow)
                            del fldrow
                #required FEATURE CLASS does not exist 
                else:
                    fcrow = fcrows.newRow()
                    fcrow.setValue("FDS", theFDS)
                    fcrow.setValue("FC_MISSING", theFC)
                    fcrow.setValue("INSTALLATION", installationName)
                    fcrows.insertRow(fcrow)
                    del fcrow
        
            #required FEATURE DATASET does not exist
            else:
                fdrow = fdrows.newRow()
                fdrow.setValue("FDS_MISSING", theFDS)
                fdrow.setValue("INSTALLATION", installationName)
                fdrows.insertRow(fdrow)
                del fdrow
        
    # Missing FDS is appended for each record in loop... remove duplicates
    columns_to_check=['FDS_MISSING','INSTALLATION']
    arcpy.DeleteIdentical_management(missFDSTable,fields=columns_to_check)
    
    columns_to_check=['FDS','FC_MISSING','INSTALLATION']
    arcpy.DeleteIdentical_management(missFCTable,fields=columns_to_check)
    
    columns_to_check=['FDS','INSTALLATION','FC','FIELD_MISSING']
    arcpy.DeleteIdentical_management(missFLDTable,fields=columns_to_check)
    
    edit.stopOperation()
    edit.stopEditing(True)  
    del nullrows 
    del fdrows
    del fldrows
    del fcrows
    
    
    arcpy.AddMessage('Comparisons between ' + installationName + " & " + compName + ' Completed!')
    time_elapsed = datetime.now() - start_time  
    arcpy.AddMessage('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
            
compareGDBs(installGDB,compGDB)
    
# =============================================================================
# 
# arcpy.GetInstallInfo ()
# 
# =============================================================================
# =============================================================================
# {'BuildNumber': u'8321',
#  'InstallDate': u'3/19/2018',
#  'InstallDir': u'c:\\program files (x86)\\arcgis\\desktop10.6\\',
#  'InstallTime': u'12:39:29',
#  'InstallType': u'N/A',
#  'Installer': u'stevenconnorg',
#  'ProductName': u'Desktop',
#  'SPBuild': u'N/A',
#  'SPNumber': u'N/A',
#  'SourceDir': u'C:\\Users\\stevenconnorg\\Documents\\ArcGIS 10.6\\Desktop\\SetupFiles\\',
#  'Version': u'10.6'}
# =============================================================================

# =============================================================================
# for name, module in sorted(sys.modules.items()): 
#   if hasattr(module, '__version__'): 
#     print name, module.__version__ 
# =============================================================================

# =============================================================================
# Cython 0.27.3
# Cython.Build.Dependencies 0.27.3
# Cython.Shadow 0.27.3
# IPython 5.4.1
# IPython.core.release 5.4.1
# IPython.utils._signatures 0.3
# PIL 5.0.0
# PIL.version 5.0.0
# _ast 82160
# _csv 1.0
# _ctypes 1.1.0
# _elementtree 1.0.6
# _struct 0.2
# argparse 1.1
# ast 82160
# backports.shutil_get_terminal_size 1.0.0
# bottleneck 1.2.1
# bottleneck.version 1.2.1
# bs4 4.6.0
# cPickle 1.71
# cffi 1.11.4
# cgi 2.6
# chardet 3.0.4
# chardet.version 3.0.4
# cloudpickle 0.5.2
# colorama 0.3.9
# csv 1.0
# ctypes 1.1.0
# cycler 0.10.0
# cython 0.27.3
# dateutil 2.6.1
# decimal 1.70
# decorator 4.2.1
# distutils 2.7.14
# email 4.0.3
# future 0.15.2
# html5lib 1.0.1
# ipykernel 4.8.0
# ipykernel._version 4.8.0
# ipython_genutils 0.2.0
# ipython_genutils._version 0.2.0
# ipywidgets 7.1.1
# ipywidgets._version 7.1.1
# json 2.0.9
# jupyter_client 5.2.2
# jupyter_client._version 5.2.2
# jupyter_core 4.4.0
# jupyter_core.version 4.4.0
# logging 0.5.1.2
# lxml.etree 4.1.1
# matplotlib 2.1.2
# matplotlib.backends.backend_agg 2.1.2
# multiprocessing 0.70a1
# numexpr 2.6.4
# numpy 1.14.0
# numpy.core 1.14.0
# numpy.core.multiarray 3.1
# numpy.core.umath 0.4.0
# numpy.lib 1.14.0
# numpy.linalg._umath_linalg 0.1.5
# pandas 0.22.0
# pandas._libs.json 1.33
# pickle $Revision: 72223 $
# pickleshare 0.7.4
# pkg_resources._vendor.appdirs 1.4.0
# pkg_resources._vendor.packaging 16.8
# pkg_resources._vendor.packaging.__about__ 16.8
# pkg_resources._vendor.pyparsing 2.1.10
# pkg_resources._vendor.six 1.10.0
# pkg_resources.extern.appdirs 1.4.0
# pkg_resources.extern.packaging 16.8
# pkg_resources.extern.pyparsing 2.1.10
# pkg_resources.extern.six 1.10.0
# platform 1.0.7
# prompt_toolkit 1.0.15
# pydoc $Revision: 88564 $
# pyexpat 2.7.14
# pygments 2.2.0
# pyparsing 2.2.0
# pytz 2017.3
# re 2.2.1
# scandir 1.6
# six 1.11.0
# spyder 3.2.6
# spyder.utils.external.binaryornot 0.4.0
# tarfile $Revision: 85213 $
# traitlets 4.3.2
# traitlets._version 4.3.2
# urllib 1.17
# urllib2 2.7
# zlib 1.0
# zmq 16.0.3
# zmq.sugar 16.0.3
# zmq.sugar.version 16.0.3
# =============================================================================


# =============================================================================
# import platform
# platform.machine()
# =============================================================================
# =============================================================================
# 'AMD64'
# =============================================================================
# =============================================================================
# platform.version()
# =============================================================================
# =============================================================================
# '10.0.16299'
# =============================================================================
# =============================================================================
# platform.platform()
# =============================================================================
# =============================================================================
# 'Windows-10-10.0.16299'
# =============================================================================
# =============================================================================
# platform.uname()
# =============================================================================
# =============================================================================
# ('Windows',
#  'LAPTOP-TNLQN6EV',
#  '10',
#  '10.0.16299',
#  'AMD64',
#  'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel')
# =============================================================================

# =============================================================================
# platform.processor()
# =============================================================================
# =============================================================================
# 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel'
# =============================================================================

