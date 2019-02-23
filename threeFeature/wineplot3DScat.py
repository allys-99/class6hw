#!/usr/bin/env python

import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

def WineMain():
    df = LoadDataSet()
    print(df)
    getSS(df)
    Plot3D(df)

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

def Plot3D(df):
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
            for kdx in range(jdx+1, len(characteristics)):
                feat3 = characteristics[kdx]
                c1feat3 = c1.loc[:,feat3]
                c2feat3 = c2.loc[:,feat3]
                c3feat3 = c3.loc[:,feat3]
                Plot3DFig(c1feat1,c2feat1,c3feat1,
                          c1feat2,c2feat2,c3feat2,
                          c1feat3,c2feat3,c3feat3,
                          feat1,feat2,feat3)

def Plot3DFig(c1feat1,c2feat1,c3feat1,
              c1feat2,c2feat2,c3feat2,
              c1feat3,c2feat3,c3feat3,
              feat1,feat2,feat3):
    c1feat1.reset_index(drop=True,inplace=True)
    c2feat1.reset_index(drop=True,inplace=True)
    c3feat1.reset_index(drop=True,inplace=True)
    c1feat2.reset_index(drop=True,inplace=True)
    c2feat2.reset_index(drop=True,inplace=True)
    c3feat2.reset_index(drop=True,inplace=True)
    c1feat3.reset_index(drop=True,inplace=True)
    c2feat3.reset_index(drop=True,inplace=True)
    c3feat3.reset_index(drop=True,inplace=True)
    mylabel=feat1+" vs. "+feat2+" vs. "+feat3
    print("plotting 3D figure for : ",mylabel)
    plt.close()
    fig = plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    plt.xlabel(feat1)
    plt.ylabel(feat2)
    mytitle="Wine Attributes"
    plt.title(mytitle)
    ax=Axes3D(fig)
    for idx in range(len(c1feat1)):
        c1=ax.scatter(c1feat1[idx],c1feat2[idx],c1feat3[idx],label='c1',color='green',s=200, marker='o')
    for jdx in range(len(c2feat1)):
        c2=ax.scatter(c2feat1[jdx],c2feat2[jdx],c2feat3[jdx],label='c2',color='yellow',s=200, marker='s')
    for kdx in range(len(c3feat1)):
        c3=ax.scatter(c3feat1[kdx],c3feat2[kdx],c3feat3[kdx],label='c3',color='orange',s=200, marker='d')
    ax.set_xlabel(feat1)
    ax.set_ylabel(feat2)
    ax.set_zlabel(feat3)
    ax.legend((c1,c2,c3),('c1','c2','c3'), loc='upper right',shadow=True)
    ax.set_title(mytitle)
    fig1=plt.gcf()
    plt.draw()
    plt.show()
    fname="3D_"+feat1+"_"+feat2+"_"+feat3+".png"
    fig1.savefig(fname)
    #print("    fname=",fname)


print ("\n . . . . . W I N E . . . . . \n")
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
characteristics = ['cultivator','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash',
        'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols',
        'Proanthocyanins', 'Colour Intensity', 'Hue',
        'OD280_OD315 of diluted wines', 'Proline']
WineMain()

