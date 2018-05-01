import sys
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from Assignment_set_2.Assignment1.classifier import classifiers
from sklearn.ensemble import ExtraTreesClassifier
from matplotlib import pyplot


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
        data.rename(columns={'datetime':'time'})
    print(list(data))
    return data

def format_deviceid(data):
    for i in range(len(data)):
        device=data.iloc[i]['devid']
        if device[0]=='M':
            data.at[i,'devid']=1
        elif  device[0]=='T':
            data.at[i,'devid']=2
        else:
            if device[0]=='D':
                data.at[i,'devid']=3
    return data

def format_browser(data):
    browser = {'Google Chrome': 1, 'Chrome': 1, 'Firefox': 2, 'Mozilla Firefox': 2, 'Mozilla': 2, 'Edge': 3,
               'Safari':4,'Explorer':5,'InternetExplorer':5,'Internet Explorer':5,'IE':5,'Opera':6}

    for i in range(len(data)):
        browser_opt = data.iloc[i]['browserid']
        data.at[i,'browserid'] = browser.get(browser_opt)
    return data

def format_countrycode(data):
    one_hot=pd.get_dummies(data['countrycode'])
    #print(one_hot)
    del data['countrycode']
    data=data.join(one_hot)
    print(data)
    countrycode={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
    #for i in range(len(data)):
    #    country_opt = data.iloc[i]['countrycode']
    #    data.at[i, 'countrycode'] = countrycode.get(country_opt)
    return data

def one_hot_encoding(data,label):
    one_hot=pd.get_dummies(data[label])
    del data[label]
    data=data.join(one_hot)
    return data

def format_columns(data):
    data = format_browser(data)
    #data = format_countrycode(data)
    #data = format_deviceid(data)
    data=decompose_datetime(data)
    return data

def feature_selection(data,target):
    labels = list(data)
    model = ExtraTreesClassifier()
    model.fit(data, target)
    print(labels)
    features = model.feature_importances_
    print(features)

    for i in range(len(labels)):
        if features[i] < 0.09:
            del data[labels[i]]
    return data


def preprocess(dataset_address):
    train_data=pd.read_csv(dataset_address,index_col=None)
    train_data = train_data.dropna(axis=0)
    train_data = train_data.reset_index(drop=True)
    target = train_data.ix[:, 'click':]
    train_data = train_data.ix[:, :-1]
    del train_data['ID']

    train_data=format_columns(train_data)
    categorical_data={'devid','browserid','date','time','countrycode'}
    for item in categorical_data:
        train_data=one_hot_encoding(train_data,item)

    print(train_data)

    train_data=feature_selection(train_data,target)

    #print(train_data)

    X_train, X_test, y_train, y_test = train_test_split(train_data, target,stratify=target, test_size=0.3)
    Xtrain, Xvalidate, ytrain, yvalidate = train_test_split(X_train, y_train, test_size=0.2)
    clr=classifiers()
    clr.svm(Xtrain,ytrain,Xvalidate,yvalidate)
    clr.naive_bayes(Xtrain,ytrain,Xvalidate,yvalidate)
    clr.decision_tree(Xtrain,ytrain,Xvalidate,yvalidate)