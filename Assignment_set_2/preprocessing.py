import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

from Assignment_set_2.classifier import classifiers


def decompose_datetime(data):
    data['date']=" "
    for i in range(len(data)):
        datetime=data.iloc[i]['datetime'].split(' ')
        ymd=datetime[0].split('-')
        date=int(ymd[2])
        if date<=14:
            data.at[i, 'date'] = 'month_first_half'
        else:
            data.at[i, 'date'] = 'month_second_half'
        time=datetime[1].split(':')
        hour=int(time[0])

        if hour<=12:
            data.at[i, 'datetime'] = 'morning'
        elif hour<18:
            data.at[i, 'datetime'] = 'afternoon'
        else:
            data.at[i,'datetime']='evening'
        #data.rename(columns={'datetime':'time'})
    #print(list(data))
    return data

def format_browser(data):
    firefox={'Mozilla Firefox', 'Mozilla'}
    explorer={'InternetExplorer','Internet Explorer','IE'}
    for i in range(len(data)):
        if data.at[i,'browserid']=='Google Chrome':
            data.at[i, 'browserid']='Chrome'
        elif  data.at[i,'browserid'] in firefox:
            data.at[i, 'browserid'] = 'Firefox'
        else:
            if data.at[i,'browserid'] in explorer:
                data.at[i, 'browserid'] = 'Explorer'
    return data



def one_hot_encoding(data,label):
    one_hot=pd.get_dummies(data[label])
    del data[label]
    data=data.join(one_hot)
    return data

def format_columns(data):
    data = format_browser(data)
    data=decompose_datetime(data)
    return data

def feature_selection(data,target):
    labels = list(data)
    model = ExtraTreesClassifier()
    model.fit(data, target)
    print(labels)
    feature_importance = model.feature_importances_
    print('feature importance')
    print(feature_importance)

    for i in range(len(labels)):
        if feature_importance[i] < 0.09:
            del data[labels[i]]
    return data


def preprocess(dataset_address):
    #delete rows with missing values, get target data, delete ID column
    train_data=pd.read_csv(dataset_address,index_col=None)
    train_data = train_data.dropna(axis=0)
    train_data = train_data.reset_index(drop=True)
    target = train_data.ix[:, 'click':]
    train_data = train_data.ix[:, :-1]
    del train_data['ID']

    #format other columns
    train_data=format_columns(train_data)
    categorical_data={'devid','browserid','date','datetime','countrycode'}
    #one hot encoding
    for item in categorical_data:
        train_data=one_hot_encoding(train_data,item)

    #select relevant features
    train_data=feature_selection(train_data,target)

    print('selected features:')
    print(list(train_data))
    #divide into train and test dataset
    X_train, X_test, y_train, y_test = train_test_split(train_data, target,stratify=target, test_size=0.3)
    X_test.to_csv('dataset/X_test.csv')
    y_test.to_csv('dataset/y_test.csv')

    #divide into train and validation dataset
    Xtrain, Xvalidate, ytrain, yvalidate = train_test_split(X_train, y_train, test_size=0.2)

    flag=1
    label=list(train_data)
    #apply different classifiers on validation data
    print('Validation data results')
    clr=classifiers()
    clr.naive_bayes(Xtrain, ytrain, Xvalidate, yvalidate,flag,label)
    clr.svm(Xtrain,ytrain,Xvalidate,yvalidate,flag,label)
    clr.decision_tree(Xtrain,ytrain,Xvalidate,yvalidate,flag,label)
    flag=0
    #apply classifiers on test data
    print('Test data results')
    clr.naive_bayes(Xtrain,ytrain,X_test,y_test,flag,label)
    clr.svm(Xtrain, ytrain, X_test, y_test,flag,label)
    clr.decision_tree(Xtrain, ytrain, X_test, y_test,flag,label)
