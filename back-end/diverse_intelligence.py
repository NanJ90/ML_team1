# -*- coding: utf-8 -*-
"""diverse_intelligence.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AsvpMDYy5DhRv-G5jj9WeBvvIXkuY4CV
"""
# import joblib
import pickle
# Data manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Feature engineering
import re
import nltk
from nltk.util import ngrams
 #sklearn feature extraction
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')
from nltk.corpus import stopwords

# Standardization
from sklearn.preprocessing import StandardScaler

#pipeline
from sklearn.pipeline import make_pipeline
"""### EDA Analysis"""

url = 'https://raw.githubusercontent.com/NanJ90/ML_team1/main/inputs.csv'
df1 = pd.read_csv(url)

df1 = df1.reset_index()
df1.head()

df1['category'] = pd.Categorical(df1['category'])

df1.describe()



#convert multi-labels to binary 0:malicious 1:normal
df1['labels'] = [0 if el == 'normal' else 1 for el in df1['category']]

df1.head()

f,ax=plt.subplots(1,2,figsize=(8,4))
df1['labels'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True, wedgeprops={'alpha':0.2})


X = df1['input']
y = df1['labels']

#checking unique value of X
len(np.unique(X))

"""###Functions"""

def feature_extrac_skl(X):
  vectorizer = CountVectorizer(min_df = 2, max_df = 0.8, stop_words = stopwords.words('english'))
  X = vectorizer.fit_transform(X.values.astype('U')).toarray()
  return X

def standadize(X):
  scaler = StandardScaler()
  X_scaled =scaler.fit_transform(X)
  return X_scaled

def metrics_generator(model, X_test, y_test):
  y_test_predicted = gaussianNB_clf.predict(X_test)

  accuracy_score_test = np.mean(y_test_predicted == y_test)
  print('\nAccuracy: ', accuracy_score_test)

  print('\nTest confusion matrix:')
  print(confusion_matrix(y_test, y_test_predicted))

  precision_test = precision_score(y_test, y_test_predicted, average='micro')
  print('\nTest precision = %f'%precision_test)

  recall_test = recall_score(y_test, y_test_predicted, average='micro')
  print('\nTest recall = %f'%recall_test)

  f1_test=f1_score(y_test, y_test_predicted, average='micro')
  print('\nTest F1 score = %f'%f1_test)

  print('\nClassification report: ')
  print(classification_report(y_test, y_test_predicted))

"""### Feature exaction by sklearn """



vectorizer = CountVectorizer(min_df = 2, max_df = 0.8, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(X.values.astype('U')).toarray()
#resizing for short size in order to test

# Compute a permutation array
# perm = np.random.permutation(len(y))

# Use the permutation to shuffle X and y in the same way
# X_shuffled = X[perm]
# y_shuffled = y[perm]
# X_tru = X_shuffled[:1000].copy()
# y_tru = y_shuffled[:1000].copy()
# # get the feature names
# feature_names = vectorizer.get_feature_names()
# # print the feature names
# print(feature_names)

# print(X.shape)
# print(y.shape)

#checking unique value of X after feature extraction 
# len(np.unique(X))

"""Data scaling"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled =scaler.fit_transform(X)

"""##Balancing dataset by SMOTE



"""

###balancing dataset
from imblearn.over_sampling import SMOTE
sampler = SMOTE(random_state=0)
X_res, y_res = sampler.fit_resample(X_scaled, y)

#after oversampling's dataset shape 
print(X_res.shape)
print(y_res.shape)

#an extention of SMOTE that focus on continous feature. 
# from imblearn.over_sampling import SMOTEN
# sampler = SMOTEN(random_state=0)


"""##Nan's training dev

### Create train and test dataset
"""

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score,cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score,classification_report

X_train, X_test, y_train, y_test = train_test_split(X_res,y_res, test_size=0.2, random_state=2)

"""###Naive Bayes"""

from sklearn.naive_bayes import GaussianNB, MultinomialNB

# import warnings
# warnings.filterwarnings('ignore')
# param_grid = {'var_smoothing': [0.001, 0.01, 0.1, 1.0]}
# gnb = GaussianNB()

# gnb = GridSearchCV(gnb, param_grid, scoring='recall', cv = 4, verbose=1, n_jobs=-1)
# gnb.fit(X_train,y_train)

# params_optimal = gnb.best_params_

# print('Best Score (accuracy): %f'%gnb.best_score_)
# print('Optimal hyperparameter values: ', params_optimal)
# print('\n')

"""####Train the optimal Gaussian NB model"""

gaussianNB_clf = GaussianNB(var_smoothing=0.001)
gaussianNB_clf.fit(X_train,y_train)

pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
pickle.dump(gaussianNB_clf, open('model.pkl','wb'))
"""####Evaluate the optimal gaussian model on test data"""
# metrics_generator(gaussianNB_clf,X_test,y_test)
# model = pickle.load(open('model.pkl', 'rb'))
# model.predict(X_test)




