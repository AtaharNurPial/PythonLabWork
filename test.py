import numpy as np


'''
1D array indexing
a = np.arange(10)**3
print(a)

print(a[-4:])
print(a[::-1])

a [:6:2] = 6969
a[4::3] = 6969

#iterating 1D array
for element in a:
    print(element**(1/3))
'''
'''
2D array 
indexing = a[row,column]
b = np.array([[0,1,2,3],
              [10,11,12,13],
              [20,21,22,23],
              [30,31,32,33],
              [40,41,42,43]])

print(b[4,1])
print(f"Prints column1: {b[:,1]}")
print(f"Prints column3: {b[:,3]}")

print(f"Prints row3: {b[3,:]}")

print(f"Prints column0and1: {b[:,:2]}")
print(f"Prints column1and2: {b[:,1:3]}")

print(b[:2, 2])  #prints first 2 rows in the third column of b

iterating 2D array

for row in b:
    for col in row:
        print(col, end= " ")
'''
'''
#specific row and column value indexing

a = np.array([[1,2,3],
              [6,9,7],
              [56,69,42]])
#if i want to print 2(0,1),7(1,2),69(2,1)  => a[(all_row),(all_col)]
print(a[(0,1,2),(1,2,1)])
'''

'''
# accessing an array(a) by another array(b) //also called mutating

a = np.array([[0,1,2],
              [5,6,7], 
              [3,4,8]])
b = np.array([2,1,0])
print(a[np.arange(3),b])  #access the a array using np.arange(3) as row and b[] as col 



#boolean indexing

a = np.array([[0,1,2],
              [5,6,7], 
              [3,4,8]])
print(a[a>2])   #returns a 1D array that meets the condition
'''

# change array shape

a = np.floor(10* np.random.random((3,4)))
print(a)
# print(type(a[2,1]))

print(a.ravel()) #ravel() converts any dimension array to 1D array
print(a.reshape(4,3))  #reshape the array into desired dimension if number of elements are sequal i.e 3*4 ==4*3
