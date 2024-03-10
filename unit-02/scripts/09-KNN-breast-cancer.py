# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:17:45 2023

@author: elvia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

import os
os.chdir("D://Python/")
os.getcwd()
df=pd.read_csv("wisc_bc_data.csv")
df.head()
df.info()
df[['diagnosis']]

'''
The diagnosis column is our target variable and you can notice that.
Also note that the ID column has no significance. So, we can remove ID
column.
'''
df.drop(['id'], axis = 1,inplace=True)

#Check whether any of the columns contain null values.
df.isnull().sum()

#The label values are ‘M’ and ‘B’ corresponding to the Malignant and
#Benign classes. We can convert them to 0 and 1 respectively.

ctypes={'M':1,'B':0} #A dictionary is defined.
df['diagnosis']=df['diagnosis'].map(ctypes)


'''
Visualizing the Data
We consider few features like radius_mean,texture_mean and perimeter_mean
to visualize the data distribution.
'''
sns.pairplot(df,vars=['radius_mean','texture_mean','perimeter_mean'],hue='diagnosis')

#Creating the KNN Model
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#Before feeding the data to the algorithm, we split the data into labels
#and features.

X = np.array(df.iloc[:,1:])
y = np.array(df['diagnosis'])

#For evaluating the model we have to take train and test datasets separately.

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20, random_state = 42)

#Identifying the optimal value of k
'''
If we randomly choose the value of K, that will not guarantee a good result.
 One way to help you find the best value of K is to plot the graph of K 
 value and the corresponding error rate for the dataset. We use the cross 
 validation error to find this out. The K value with least CV error will be
 the optimal value.
'''

#Performing 10 fold cross validation
from sklearn.model_selection import cross_val_score
nbrs = []
cv_scores = []
for k in range(1,40):
   nbrs.append(k)
   knn = KNeighborsClassifier(n_neighbors = k)
   scores = cross_val_score(knn,X_train,y_train,cv=10, scoring = 'accuracy')
   cv_scores.append(scores.mean())
print(cv_scores) #The outpu.

#The above are the scores for each k using 10 fold cross validation. 
#You can see that K=2 and K=13 are giving the best score and hence the 
#least error. To be more specific, from this we can calculate the 
#miss-classification error (1-CVScore) and identify the optimal value of k.


##Misclassification error   
MSE = [1-x for x in cv_scores]
##Optimal value of k, with least MSE
optimal_k = nbrs[MSE.index(min(MSE))]
print('The optimal value of K (neighbors) is %d ' %optimal_k)

#We can visualize the scores for each value of k, by the below plot using 
#matplotlib.
plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), MSE, color='red', linestyle='dashed', marker='o',
markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

#Creating the Model with selected optimal value
knn = KNeighborsClassifier(n_neighbors = 3) # It is depend on the optimas k.
knn.fit(X_train,y_train)

#Evaluating the Model
from sklearn.metrics import accuracy_score,precision_score,recall_score,classification_repor

y_pred = knn.predict(X_test)
y_pred
#Evaluating the Model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall:", recall)

from sklearn.metrics import confusion_matrix

#KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=None, n_neighbors=13, p=2,weights='uniform')
print('Confusion Matrix :\n')
cf_matrix=confusion_matrix(y_test,y_pred)
print(cf_matrix)

#Plotting confusion matrix with different modules
import seaborn as sns

#1.-Plot Confusion Matrix For Binary Classes
ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues')
ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()

#2. Plot Confusion Matrix For Binary Classes With Percentage
ax = sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()

#3. Plot Confusion Matrix For Binary Classes With Labels

labels = ['True Neg','False Pos','False Neg','True Pos']
labels = np.asarray(labels).reshape(2,2)
ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')
ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()

#4. Plot Confusion Matrix For Binary Classes With Labels And Percentages
group_names = ['True Neg','False Pos','False Neg','True Pos']
group_counts = ["{0:0.0f}".format(value) for value in
                cf_matrix.flatten()]

group_percentages = ["{0:.2%}".format(value) for value in
                     cf_matrix.flatten()/np.sum(cf_matrix)]

labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]

labels = np.asarray(labels).reshape(2,2)

ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])

## Display the visualization of the Confusion Matrix.
plt.show()

#For multiple classification you can consult
# https://www.stackvidhya.com/plot-confusion-matrix-in-python-and-why/