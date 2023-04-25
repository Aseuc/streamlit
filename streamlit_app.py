import csv
import pandas as pd
import numpy as np
import matplotlib as mp
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sklearn as sk





data = pd.read_excel('TestData.xlsx')
np.random.seed(42)
X = data.drop('target',axis=1)
y = data["target"]
X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(X,y,test_size=0.2)
clf = RandomForestClassifier(n_estimators =100)
clf.fit(X_train, y_train)
X_data = pd.read_csv('newTest.csv')
clf.predict(X_data)
X_test.head()
prob = clf.predict_proba(new_data[:100])
print(prob)
X_data["prediction_prob"] = clf.predict(X_data)
pd.set_option('display.max_rows',None)
X_data
