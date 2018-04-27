from sklearn.model_selection import train_test_split
#from .dataset import *
import pandas as pd

train_data=pd.read_csv('dataset/train.csv')

#print(train_data)
y=train_data.columns[-1]

X_train, X_test, y_train, y_test = train_test_split(train_data, y,stratify=y, test_size=0.25)

print('ya')



#Extract features that are relevant for classification

#Identify the target variable.
#Do all the necessary pre-processing steps like One-hot encoding, Treating missing values, Standardization, converting categorical to numerical data, etc. wherever necessary.

#Handle any class imbalance, if required.
#Split the data into 80:20 for train and validation.
#Apply different classifiers and check validation accuracy.
#Calculate the cross-validation score, precision, recall and also display the confusion matrix.
#Evaluate the accuracy on test set#.
