import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr
from math import sqrt


def correlations_pvalues(data):

# Calculate correlations and p-values


    list_corr = []
    list_pvalue = []

    for x in data.columns:
        for y in data.columns:
            corr, pvalue = stats.pearsonr(data[x],data[y])
            list_corr.append(corr)
            list_pvalue.append(pvalue)
            
    return list_corr,list_pvalue


def matrices(data, list_corr,list_pvalue, decimals):
    
# Make 2 matrices: correlations and p-values
    matrix_corr = np.reshape(list_corr, (len(data.columns),len(data.columns)))
    matrix_pvalue = np.reshape(list_pvalue, (len(data.columns), len(data.columns)))
    
    matrix_corr = matrix_corr.round(decimals)
    matrix_pvalue = matrix_pvalue.round(decimals)
    
    return matrix_corr, matrix_pvalue


def dataframes(data,matrix_corr,matrix_pvalue):

# Make 2 pandas DataFrames: correlations and p-values

    df_corr = pd.DataFrame(matrix_corr, columns=data.columns)
    df_pvalue = pd.DataFrame(matrix_pvalue, columns=data.columns)

    df_corr.index = data.columns
    df_pvalue.index = data.columns
    
    return df_corr, df_pvalue


def final_dataframe(df_corr,df_pvalue):

# Significance levels to Dataframe correlations

    sig1 = df_corr.applymap(lambda x: '{}*'.format(x))
    sig2 = df_corr.applymap(lambda x: '{}**'.format(x))
    sig3 = df_corr.applymap(lambda x: '{}***'.format(x))

# Replace values where significance condition is true
    df_corr = df_corr.mask(df_pvalue<=0.1,sig1)
    df_corr = df_corr.mask(df_pvalue<=0.05,sig2)
    df_corr = df_corr.mask(df_pvalue<=0.01,sig3)
    
    return df_corr, df_pvalue


def correlation_matrix(data, decimals):
    list_corr, list_pvalue = correlations_pvalues(data)
    matrix_corr, matrix_pvalue = matrices(data, list_corr,list_pvalue, decimals)
    df_corr, df_pvalue = dataframes(data,matrix_corr,matrix_pvalue)
    df_corr, df_pvalue = final_dataframe(df_corr,df_pvalue)
    return df_corr


def pvalue_matrix(data,decimals):
    list_corr, list_pvalue = correlations_pvalues(data)
    matrix_corr, matrix_pvalue = matrices(data, list_corr,list_pvalue, decimals)
    df_corr, df_pvalue = dataframes(data,matrix_corr,matrix_pvalue)
    return df_pvalue