# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:23:22 2023

@author: elvia
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import seaborn as sns
from seaborn import load_dataset
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

#from imblearn.over_sampling import SMOTE  
# It is applied to data balance
#SMOTE(Synthetic Minority Over-sampling Technique)
# It is compatible with scikit-learn and is part of scikit-learn-contrib projects.
#conda install -c conda-forge imbalanced-learn
import statsmodels.api as sm
import math
from sklearn import metrics
from sklearn.metrics import confusion_matrix

import os
os.chdir("D:\\Python/")
os.getcwd()

df=pd.read_csv("Titanic2.csv")
#You can download titanic dataset from seaboarn module as:
#df=load_dataset("titanic")
df.shape
df.columns
df.dtypes
df.describe
#To verify how many variables are null.
df.info()

plt.hist(df["Age"])
plt.title("Distribución de la edad del Titanic-age")
plt.xlabel("Edad-Age")
plt.ylabel("Total de miembros ")

#Percentage of survivers
x,y='Pclass','Survived'

df1=df.groupby(x)[y].value_counts(normalize=True)
df1=df1.mul(100)
df1=df1.rename('percent').reset_index()

g=sns.catplot(x=x,y='percent',hue=y,kind='bar',data=df1)
g.ax.set_ylim(0,100)
g.fig.set_size_inches(20,10)

for p in g.ax.patches:
    txt=str(p.get_height().round(1))+ '%'
    txt_x=p.get_x()
    txt_y=p.get_height()
    g.ax.text(txt_x,txt_y,txt)

#1st and second class (63%) and retired (47%%) individuals show the highest percentage of survivers.

# Percentage of famale and male. 
df.dtypes
df.select_dtypes(include='object')
df["Sex"].index
Sex=['female','male']

for i in Sex:
    dfSex=df[df['Sex']==i]
    labels='unsurvived','survived'
    sizes=(dfSex['Survived'].value_counts()).to_list()
    explode=(0,0.1) #Only "explode" the 2nd slice (i.e. 'Hogs')
    fig1,ax1=plt.subplots()
    ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',shadow=True,startangle=90)
    ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(i)
    plt.show()
    
##Pre-processing the data

df.info()

#Exploring variables that have null values.

#Filling and cathegorizing Age column.
print(f"Max value of age column : {df['Age'].max()}")
print(f"Min value of age column : {df['Age'].min()}")
 #It is filling all null values in Age with the mode of this column.   
df_f1 = df.fillna({'Age':df['Age'].mode()[0]})
df_f1.info()

bins = [0, 5, 17, 25, 50, 80]
labels = ['Infant', 'Kid', 'Young', 'Adult', 'Old']
df_f1['Age'] = pd.cut(df_f1['Age'], bins = bins, labels=labels)
df_f1.info()

#Embarked null values
print(f"How many 'S' on embarked column : {df[df['Embarked'] == 'S'].shape[0]}")
print(f"How many 'C' on embarked column : {df[df['Embarked'] == 'C'].shape[0]}")
print(f"How many 'Q' on embarked column : {df[df['Embarked'] == 'Q'].shape[0]}")
         #AQUI ESTABA LA FALLA---
df_f1 = df_f1.fillna({'Embarked' : 'S'})
df_f1[['Pclass', 'Survived']].groupby(['Pclass']).sum().sort_values(by='Survived')
df_f1.info()

df_f1[['Sex', 'Survived']].groupby(['Sex']).sum().sort_values(by='Survived')

#Cathegorization of fare
bins = [-1, 7.9104, 14.4542, 31, 512.330]
labels = ['low','medium-low','medium','high']
df_f1['Fare'] = pd.cut(df_f1["Fare"], bins = bins, labels = labels)

#Droping non required variables
columns = ['PassengerId','Name','Ticket','Cabin']
df_f2 = df_f1.drop(columns, axis=1)

#Finally, we have all variables completed and cathegorized, then dummies
#variables should be created for non-numeric values.
 '''
 1. For categorical variables, we will have to create dummy variables. Creating dummy variables 
 is nothing but assigning a numerical value to each category. And then transforming the rows 
 with categories to multiple columns. 
 '''
dummies = ['Sex','Age','Fare','Embarked']
dummy_data = pd.get_dummies(df_f2[dummies])
df_f2=df_f2.drop(dummies,axis=1)

dummy_data.shape
dummy_data.info()
dummy_data.describe()

df_final=pd.concat([df_f2,dummy_data],axis=1)
#Guess what!!!!
##Creation of the Logistic Regression Model

'''
   MODEL GENERATION
'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


X = df_final.drop('Survived', axis = 1)
y = df_final['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
# X contains independent values, y contains dependent value

#Model Building 
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
y_pred

#We can check the accuracy score of our model.
y_pred.shape
accuracy_score(y_pred, y_test)
confusion_matrix(y_pred, y_test)
 # 31 + 26 = 57 wrong prediction
 
 
 #
 from sklearn.metrics import roc_auc_score
 from sklearn.metrics import roc_curve

 logit_roc_auc=roc_auc_score(y_test,log_reg.predict(X_test))
 fpr,tpr,thresholds=roc_curve(y_test,log_reg.predict_proba(X_test)[:,1])
 plt.figure()
 plt.plot(fpr,tpr,label='Logistic Regression (area=%0.2f)'% logit_roc_auc)
 plt.plot([0,1],[0,1],'r--')
 plt.xlim([0.0,1.0])
 plt.ylim([0.0,1.05])
 plt.xlabel('False positive Rate')
 plt.ylabel('True Positive Rate')
 plt.title('Receiver operating characteristic')
 plt.legend(loc="lower right")
 plt.savefig('Log_ROC')
 plt.show()
 