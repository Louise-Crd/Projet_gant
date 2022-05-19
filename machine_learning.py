# 1. Importing libraries

import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# 2. Loading Iris data

path = 'base-de-donneesv3.csv'  # path of the dataset
col_name = ['doigt_1', 'doigt_2', 'doigt_3', 'doigt_4', 'doigt_5', 'class']  # creates the list of column name
dataset = pd.read_csv(path, names=col_name)  # pandas read_csv() is used for reading the csv file

# 3. Summarize the Dataset

dataset.shape
dataset.head()  # displaying the first 5 records of our dataset
dataset.info()  # prints information about a DataFrame (index dtype, columns, non-null values, memory usage)
dataset.describe()  # to view some basic statistical details of a DataFrame or a series of numeric values
dataset['class'].value_counts()  # checks the number of rows that belongs to each class

# 4. Data visualization

#Violin plot
sns.violinplot(y='class', x='doigt_1', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='doigt_2', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='doigt_3', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='doigt_4', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='doigt_5', data=dataset, inner='quartile')
plt.show()
# Pair plot
sns.pairplot(dataset, hue='class', markers='+')
plt.show()
# Heatmap
plt.figure(figsize=(7,5))
sns.heatmap(dataset.corr(), annot=True, cmap='cubehelix_r')
plt.show()


# 5. Model Building- part 1

# 5.1 Splitting the dataset
'''
X is having all the dependent variables.
Y is having an independent variable (here in this case ‘class’ is an independent variable).
'''
X = dataset.drop(['class'], axis=1)
y = dataset['class']
print(f'X shape: {X.shape} | y shape: {y.shape} ')

# 5.2 Train Test split
'''
Splitting our dataset into train and test using train_test_split(), what we are doing here is taking 80% of 
data to train our model, and 20% that we will hold back as a validation dataset
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# 5.3 Model Creation
'''
We don’t know which algorithms would be best for this problem.
Let’s check each algorithm in loop and print its accuracy, so that we can select our best algorithm
'''
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC(gamma='auto')))
# evaluate each model in turn
results = []
model_names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    model_names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# 6. Model Building- part 2

model = SVC(gamma='auto')
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy_score(y_test, prediction)
classification_report(y_test, prediction)
print(f'Test Accuracy: {accuracy_score(y_test, prediction)}')
print(f'Classification Report: \n {classification_report(y_test, prediction)}')