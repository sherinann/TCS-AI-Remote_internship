import sys
from sklearn.model_selection import train_test_split
import pandas as pd

def delete_unimportant_columns(data):
    del data['ID']
    del data['offerid']
    del data['merchant']
    return data

def decompose_datetime(data):
    for i in range(len(data)):
        part=data['datetime'][i].split(' ')
        time=part[1].split(':')
        hour=int(time[0])
        if hour<=12:
            data['datetime'][i]=1
        elif hour<18:
            data['datetime'][i] = 2
        else:
            data['datetime'][i] = 3
    return data

def format_deviceid(data):
    for i in range(len(data)):
        device=data['devid'][i]
        if device[0]=='M':
            data['devid'][i]=1
        elif  device[0]=='T':
            data['devid'][i]=2
        else:
            if device[0]=='D':
                data['devid'][i]=3
    return data

def format_browser(data):
    browser = {'Google Chrome': 1, 'Chrome': 1, 'Firefox': 2, 'Mozilla Firefox': 2, 'Mozilla': 2, 'Edge': 3}

    for i in range(len(data)):
        browser_opt = data['browserid'][i]
        data['browserid'][i] = browser.get(browser_opt)
    return data

if __name__ == '__main__':
    #train_file=sys.argv[1]
    #test_file=sys.argv[2]
    train_file='train.csv'
    test_file='test.csv'

    train_data=pd.read_csv('dataset/'+train_file)
    train_data=train_data.dropna(axis=0)
    target=train_data.ix[:,'click':]
    train_data=train_data.ix[:,:-1]
    labels=list(train_data)


    #new_train=pd.read_csv('dataset/new_train.csv')
    train_data=delete_unimportant_columns(train_data)
    train_data=decompose_datetime(train_data)
    train_data=format_deviceid(train_data)



    print(new_train)

    X_train, X_test, y_train, y_test = train_test_split(train_data, target,stratify=y, test_size=0.3)
    X_train.to_csv('dataset/new_train.csv', index=False, header=[i for i in labels[:]])
    X_test.to_csv('dataset/new_test.csv', index=False, header=None)
    y_train.to_csv('dataset/y_train.csv', index=False, header=['click'])
    y_test.to_csv('dataset/y_test.csv', index=False, header=None)
