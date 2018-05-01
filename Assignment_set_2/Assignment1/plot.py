import matplotlib.pyplot as plt
import pandas as pd
import Assignment_set_2.Assignment1.preprocessing as pre
def plott():
    train_data=pd.read_csv('Assignment_set_2/Assignment1/dataset/train.csv')
    #df=pd.DataFrame(train_data['offerid'],train_data['click'])
    train_data = train_data.dropna(axis=0)
    train_data=pre.format_browser(train_data)
    plt.scatter(train_data['browserid'],train_data['click'])
    plt.show()