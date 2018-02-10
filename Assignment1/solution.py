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
ax1 = iris.plot(kind='scatter', x=features[0], y=features[1], color='r')
ax2 = iris.plot(kind='scatter', x=features[0], y=features[2], color='g')
ax3 = iris.plot(kind='scatter', x=features[0], y=features[3], color='g')
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

