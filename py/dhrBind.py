# -*- coding: utf-8 -*-
"""
Created on Tue May 08 16:27:42 2018

@author: stevenconnorg
"""

import sys, os, pandas

mainDir = r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\DHRs"
os.chdir(mainDir)


quarterDirs = [x[0] for x in os.walk(mainDir)]
    
qdir=quarterDirs[2]
dropColumns = ['Geodatabase Features_Pct', 'Geodatabase Feature Classes_Pct','Attribute Statistics_Pct','Geodatabase Cells_Pct']
dropColList = dropColumns
def remove_whitespace(x):
        """
        Helper function to remove any blank space from a string
        x: a string
        """
        try:
            # Remove spaces inside of the string
            x = "".join(x.split())
    
        except:
            pass
        return x
    
def normlExcel(datList,lastcolumn,dropStat,dropColList):
        # dropStat 1 = counts
        # dropStat 0 = pcnt
        DHRs=[]
        for DHR in datList:
            installation=DHR.split("Statistics")[0]
            df = pandas.read_excel(os.path.join(qdir,DHR), delim_whitespace=True)
            df['Installation'] = installation
            DHRs.append(df)
            
        
        def clean(dataframe):
            installation = dataframe.iloc[0]['Installation']
            dataframe = dataframe.drop(['Installation'], axis=1) # drop row with counts

            newDat = dataframe.transpose()
            newDat.columns = newDat.iloc[0,] # replace column names first first row
            newDat = newDat.iloc[1:] # then drop first row of empty values

            newDat.columns = newDat.columns.str.strip() # rename columns within tabs/white spaces
            newDat = newDat.drop(newDat.index[dropStat]) # drop row with counts
            newDat['Installation'] = installation # assign installation name to column variable

            newDat = newDat.iloc[:, :lastcolumn] # keep only first set of columns   
            if dropStat == 0: 
                suffix= '_Pct'
            if dropStat == 1:
                suffix= "_Cnt"
            
            newDat.columns = [str(col) + suffix for col in newDat.columns] # append pct
            newDat['Installation'] = installation
            
            #newDat.set_index('Installation', inplace=True)
            return(newDat)
        
        outDF = clean( DHRs[0]) 
        for dataframe in DHRs[1:]:
            newDat = clean(dataframe)
            outDF = pandas.concat([newDat,outDF], ignore_index=True)
            #outDF = outDF.append(newDat)

        
        #outDF = outDF.drop(dropColList, axis=1)
        outDF.set_index('Installation', inplace=True)
        #outDF = outDF.drop('Installation', axis=1)
        return(outDF)

outDataframes=[]
qdir = quarterDirs[2]
for qdir in quarterDirs[2]:
    qName=str(qdir.split("\\")[-1])
    datList =  os.listdir(qdir)

     # append to final dataframe

    outDF_Counts = normlExcel(datList,lastcolumn=23,dropStat=1,dropColList=dropColumns)
    outDF_Pcnt = normlExcel(datList,lastcolumn=23,dropStat=0,dropColList=dropColumns)
    list(outDF_Pcnt)
    list(outDF_Counts)
    
    # then merge the two dataframes
    outDat = outDF_Pcnt.join(outDF_Counts)
    outDat.to_excel("DHR_Dataframe_Full_"+qName+".xlsx")
    outDataframes.append(outDat)
    
# =============================================================================
diffDataframe = outDataframes[1].subtract(outDataframes[0], axis='columns')
diffDataframe.to_excel("DHR_Dataframe_Full_Q2minusQ1.xlsx")
# 
# =============================================================================
