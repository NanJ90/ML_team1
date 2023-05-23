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

url = 'https://raw.githubusercontent.com/NanJ90/ML_team1/main/inputs.csv'
df1 = pd.read_csv(url)
df1['category'] = pd.Categorical(df1['category'])
#convert multi-labels to binary 0:malicious 1:normal
df1['labels'] = [0 if el == 'normal' else 1 for el in df1['category']]
X = df1['input']
y = df1['labels']
#functions
def feature_extrac_skl(X):
  vectorizer = CountVectorizer(min_df = 2, max_df = 0.8, stop_words = stopwords.words('english'))
  X = vectorizer.fit_transform(X.values.astype('U')).toarray()
  return X
def standadize(X):
  scaler = StandardScaler()
  X_scaled =scaler.fit_transform(X)
  return X_scaled
def metrics_generator(model, X_test, y_test):
  y_test_predicted = model.predict(X_test)

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

#feature extraction
vectorizer = CountVectorizer(min_df = 2, max_df = 0.8, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(X.values.astype('U')).toarray()
X_scaled = standadize(X)

#balancing dataset
from imblearn.over_sampling import SMOTE
sampler = SMOTE(random_state=0)
X_res, y_res = sampler.fit_resample(X_scaled, y)

###balancing dataset
from imblearn.over_sampling import SMOTE
sampler = SMOTE(random_state=0)
X_res, y_res = sampler.fit_resample(X_scaled, y)

#choose randome sample cause our dimentionality is large
#Compute a permutation array
perm = np.random.permutation(len(y))

#Use the permutation to shuffle X and y in the same way
X_shuffled = X_res[perm]
y_shuffled = y_res[perm]
X_tru = X_shuffled[:1000].copy()
y_tru = y_shuffled[:1000].copy()

# Assuming your NumPy array is called 'data'
values, counts = np.unique(y_tru, return_counts=True)

# Print the count of each unique value
for value, count in zip(values, counts):
    print(f'{value}: {count}')

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score,cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score,classification_report

#portion of X and y
X_train, X_test, y_train, y_test = train_test_split(X_shuffled,y_shuffled, test_size=0.2, random_state=2)

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_train)

# Perform t-SNE
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_train)

# Visualize the transformed data
plt.figure(figsize=(10, 5))
# PCA plot with colors
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_train)  # Use y_train as color labels
plt.title('PCA')

# t-SNE plot with colors
plt.subplot(1, 2, 2)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_train)  # Use y_train as color labels
plt.title('t-SNE')

plt.tight_layout()
plt.show()