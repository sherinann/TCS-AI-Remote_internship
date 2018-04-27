import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#1. load dataset
iris=pd.read_csv('iris.csv')

#2. Create a list named headers with all the column header names in the given order.
headers= list(iris)

#3. Using the slice operation on headers, extract the column names with index 1 to 4 onto a list called features
features=list(headers[1:5])
print('features:',features)

#4. Display the first five records of iris
print(iris.head(n=5))

#5. Make a scatterplot of the Iris features.
colors = np.where(iris['Species']=='Iris-setosa','r','-')
colors[iris['Species']=='Iris-virginica'] = 'y'
colors[iris['Species']=='Iris-versicolor'] = 'b'
for i in range(len(features)):
    for j in range(i+1,len(features)):
        iris.plot.scatter(x=features[i],y=features[j],c=colors)
plt.show()

#6. What is the range of ‘SepalLengthCm’ in the dataset?
#  What is the second largest value of ‘SepalLengthCm’ in the dataset?
print( 'range of SepalLengthCm:',iris['SepalLengthCm'].max()- iris['SepalLengthCm'].min())
k=list(iris['SepalWidthCm'].nlargest(2))
print('second largest value in SepalLengthCm:',k[1])

#7. Find the mean of all the values in SepalWidthCm using numpy
print('mean:',np.mean(iris['SepalWidthCm']))

#8. Identify  ‘SepalLengthCm’  values less than 5. Create a new column named ‘Length’ , categorise each entry as ‘Small’ or ‘Large’, if less than 5.
length=[]
for i in iris['SepalLengthCm']:
    if i<5:
        length.append('Small')
    else:
        length.append('Large')
iris[iris.shape[0]]=length
print(iris)

#9. Group dataFrame by the "Species" column. Make a histogram of the same.
plt.hist(iris['Species'])
plt.show()

#10 .Find the deviation of length for ‘SepalLengthCm’ from the average
print('standard deviation:',iris['SepalLengthCm'].std())

#11 . Find correlation between columns and display columns with more than 70% percent correlation (either positive or negative).
for i in range(len(features)):
    for j in range(i+1,len(features)):
        val=iris[features[i]].corr(iris[features[j]])
        if abs(val)>0.7:
            print( 'correlation of ', features[i], features[j],':', val)

#12. Impute missing values if present using mean of the dataset.
for i in range(len(features)):
    iris[features[i]].fillna((iris[features[i]].mean()), inplace=True)

#13. Save the current dataFrame out to a new csv file.
iris.to_csv('new_iris.csv', index=False, header=None)