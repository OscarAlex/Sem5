"""
Created on Tue Oct  1 16:51:07 2019
Examen 2° Parcial
4 algoritmos
@author: Oscar
"""

from sklearn.utils import shuffle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#Leer archivo y meterlo en una matriz
with open('dataset.csv') as archivo:
    df = [l.strip().split(",") for l in archivo]
#Borrar primera fila
df = np.delete(df, (0), axis=0)
#Mezclar datos
df= shuffle(df)

#Hacer lista con las clases y matriz con las features
labels= []
features= np.zeros((190,6))
index=0
for i in df:
    fila2 = df[index]
    features[index,:] = fila2[0:6]
    labels.append(fila2[-1])
    index+= 1

#Normalizar features
scaler= MinMaxScaler()
Normfeat= scaler.fit_transform(features)

#Particionar dataset 85%
trlen= int(190*.85)
telen= 190-trlen
trainF= np.zeros((trlen,6))#Features del train
testF= np.zeros((telen,6))#Features del test
trainL= []#Labels del train
testL= [] #Labels del test

index=0
index2=0
for i in Normfeat:
    fila2 = Normfeat[index]
    if (index < trlen):
        trainF[index,:] = fila2
        trainL.append(labels[index])
        index+= 1
    else:
        testF[index2,:] = fila2
        testL.append(labels[index])
        index+= 1
        index2+= 1

#Clasificador
#Nearest Neighbors
neigh= KNeighborsClassifier(5)
neigh.fit(trainF,trainL)
index= 0
errorCount= 0
for i in testF:
    if(neigh.predict([testF[index]]) != testL[index]):
        errorCount+= 1
    index+= 1

print("Nearest Neighbors")
print("Accuracy: %f" % neigh.score(testF,testL))
print("Errors: %d" % errorCount)
print("\n")

#Decision trees
dtree= DecisionTreeClassifier()
dtree.fit(trainF,trainL)
index= 0
errorCount= 0
for i in testF:
    if(dtree.predict([testF[index]]) != testL[index]):
        errorCount+= 1
    index+= 1

print("Decision Trees")
print("Accuracy: %f" % dtree.score(testF,testL))
print("Errors: %d" % errorCount)
print("\n")

#Logistic Regression
log= LogisticRegression(solver='lbfgs',multi_class='multinomial')
log.fit(trainF,trainL)
index= 0
errorCount= 0
for i in testF:
    if(log.predict([testF[index]]) != testL[index]):
        errorCount+= 1
    index+= 1

print("Logistic Regression")
print("Accuracy: %f" % log.score(testF,testL))
print("Errors: %d" % errorCount)
print("\n")

#Support Vector Machine
svm = SVC(gamma='auto')
svm.fit(trainF,trainL)
index= 0
errorCount= 0
for i in testF:
    if(svm.predict([testF[index]]) != testL[index]):
        errorCount+= 1
    index+= 1

print("Support Vector Machines")
print("Accuracy: %f" % svm.score(testF,testL))
print("Errors: %d" % errorCount)




