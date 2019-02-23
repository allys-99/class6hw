#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def WineMain():
    df = LoadDataSet()
    print(df)
    getSS(df)
    PlotScatter(df)

def LoadDataSet():
    df = pd.read_table("wine.data.txt", delimiter=",",header=None)
    df.columns =['C','Alcohol','Malic Acid','Ash','Alcalinity of Ash',
            'Magnesium','Total Phenols','Flavanoids','Nonflavanoid Phenols',
            'Proanthocyanins','Colour Intensity','Hue','OD280_OD315 of diluted wines','Proline']
    return df

def getSS(myTable):
    print('\t\t\t\t     Mean')
    print(myTable.mean())
    print('\t\t\t   Standard Deviation')
    print(myTable.std())

def PlotScatter(df):
    c1 = df.loc[df['C'] == 1]
    c2 = df.loc[df['C'] == 2]
    c3 = df.loc[df['C'] == 3]
    for idx in range(1,len(characteristics)):
        feat1 = characteristics[idx]
        c1feat1 = c1.loc[:,feat1]
        c2feat1 = c2.loc[:,feat1]
        c3feat1 = c3.loc[:,feat1]
        for jdx in range(idx+1, len(characteristics)):
            feat2 = characteristics[jdx]
            c1feat2 = c1.loc[:,feat2]
            c2feat2 = c2.loc[:,feat2]
            c3feat2 = c3.loc[:,feat2]
            PlotScatterFile(c1feat1,c2feat1,c3feat1,c1feat2,c2feat2,c3feat2,feat1,feat2)

def PlotScatterFile(c1f1,c2f1,c3f1,c1f2,c2f2,c3f2,feat1,feat2):
    mylabel=feat1+" vs. "+feat2
    plt.xlabel(feat1)
    plt.ylabel(feat2)
    mytitle=feat1+' & '+feat2+' in Wine'
    plt.title(mytitle)
    plt.scatter(c1f1, c1f2, label='c1', color='green', s=300, marker='*')
    plt.scatter(c2f1, c2f2, label='c2', color='yellow', s=300, marker='o')
    plt.scatter(c3f1, c3f2, label='c3', color='orange', s=300, marker='d')
    plt.legend()
    fig1=plt.gcf()
    plt.draw()
    plt.show()
    fname="scat_"+feat1+feat2+".png"
    fig1.savefig(fname)
    print("    fname=",fname)


print ("\n . . . . . W I N E . . . . . \n")
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
characteristics = ['cultivator','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash',
        'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols',
        'Proanthocyanins', 'Colour Intensity', 'Hue',
        'OD280_OD315 of diluted wines', 'Proline']
WineMain()

