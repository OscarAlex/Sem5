"""
Created on Tue Nov 12 15:56:58 2019

@author: Oscar
"""
import pandas as pd
telescope_data= pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data', header=None)

telescope_data.head()

from sklearn.utils import shuffle
tele= shuffle(telescope_data)
tele.columns = ['fLength', 'fWidth','fSize','fConc','fConcl','fAsym','fM3Long','fM3Trans','fAlpha','fDist','class']
tele['class']= tele['class'].map({'g':0,'h':1})
tele_class= tele['class'].values

from sklearn.model_selection import train_test_split
training_indices, validation_indices = training_indices, testing_indices = train_test_split(tele.index,stratify = tele_class, train_size=0.75, test_size=0.25)

from tpot import TPOTClassifier
tpot = TPOTClassifier(generations=5, verbosity=2)

tpot.fit(tele.drop('class',axis=1).loc[training_indices].values, tele.loc[training_indices,'class'].values)
tpot.score(tele.drop('class',axis=1).loc[validation_indices].values, tele.loc[validation_indices, 'class'].values)

