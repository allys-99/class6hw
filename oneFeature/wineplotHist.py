#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def WineMain():
    myTable = LoadDataSet()
    print(myTable)
    getSS(myTable)
    PlotFeatures(myTable)

def getSS(myTable):
    print('\t\t\t\t     Mean')
    print(myTable.mean())
    print('\t\t\t   Standard Deviation')
    print(myTable.std())

def LoadDataSet():
    df = pd.read_table("wine.data.txt", delimiter=",",header=None)
    df.columns =['C','Alcohol','Malic Acid','Ash','Alcalinity of Ash',
            'Magnesium','Total Phenols','Flavanoids','Nonflavanoid Phenols',
            'Proanthocyanins','Colour Intensity','Hue','OD280_OD315 of diluted wines','Proline']
    return df

def PlotFeatures(df):
    c1 = df.loc[df['C'] == 1]
    c2 = df.loc[df['C'] == 2]
    c3 = df.loc[df['C'] == 3]
    for idx in range(1,len(characteristics)):
        feat = characteristics[idx]
        c1feat = c1.loc[:,feat]
        c2feat = c2.loc[:,feat]
        c3feat = c3.loc[:,feat]
        PlotHistogram(c1feat,c2feat,c3feat,feat)
    
def PlotHistogram(c1,c2,c3,v):
    plt.xlabel(v)
    plt.ylabel('number of samples')
    mytitle=v+' in Wine'
    plt.title(mytitle)
    plt.hist([c1,c2,c3], bins=30, rwidth=0.8,color=['green','yellow','orange'],label=['c1','c2','c3'])
    plt.legend()
    fig1=plt.gcf()
    plt.draw()
    plt.show()
    fname="hist_"+v+".png"
    fig1.savefig(fname)



print ("\n . . . . . W I N E . . . . . \n")
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
characteristics = ['cultivator','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash',
        'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols',
        'Proanthocyanins', 'Colour Intensity', 'Hue',
        'OD280_OD315 of diluted wines', 'Proline']
WineMain()

