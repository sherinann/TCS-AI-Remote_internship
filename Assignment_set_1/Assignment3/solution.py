import numpy as np
import random
import sys

#1. Create a function which creates an n×n array with (i,j)-entry equal to i+j.
def array_i_j(n):
    array1=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            array1[i][j]=i+j
    print(array1)

#2. Create a numpy array which contains odd numbers below 20. Arrange it to a 2x5 matrix. Compute the log of each element.
def array_odd():
    array1=np.array([])
    for i in range(20):
        if i%2!=0:
            array1=np.append(array1,i)
    matrix1=[[0 for i in range(5)] for j in range(2)]
    i=-1
    j=0
    for k in array1:
        if j==0:
            i=i+1
        matrix1[i][j]=k
        j=(j+1)%5
    print(np.log(matrix1))

#3. Create a function which creates an n×n random array. Subtract the average of each row of the matrix
def array_rand_avg(n):
    matrix1 = [[random.randint(0,10) for i in range(n)] for j in range(n)]
    print(matrix1)
    for i in range(n):
        sum=0
        for j in range(n):
            sum=matrix1[i][j]+sum
        avg=sum/n
        for j in range(n):
            matrix1[i][j]=matrix1[i][j]-avg
    print(matrix1)


#4. Create a function which creates an n×n random array. Write a program to find the nearest value from a given value in the array.
#will check which element in the matrix is near to item given by the user
def array_rand_near(n,item):
    matrix1 = [[random.randint(0, 100) for i in range(n)] for j in range(n)]
    print(matrix1)
    small=sys.maxsize
    val=sys.maxsize
    for i in range(n):
        for j in range(n):
            no=abs(item-matrix1[i][j])
            if no<small:
                small=no
                val=matrix1[i][j]
    print(val)


#5. Write a function to check if two random arrays are equal or not.
def array_rand_equal(n):
    matrix1 = [[random.randint(0, 100) for i in range(n)] for j in range(n)]
    matrix2 = [[random.randint(0, 100) for i in range(n)] for j in range(n)]
    print(matrix1)
    print(matrix2)
    for i in range(n):
        for j in range(n):
           if matrix1[i][j]!=matrix2[i][j]:
               return 'no'
    return 'yes'

#6. Create a function to get the n largest values of an array.
def nlargest(n,array1):
    array1=sorted(array1,reverse=True)
    for i in range(n):
        print(array1[i])

