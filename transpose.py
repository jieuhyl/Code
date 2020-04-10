# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:50:35 2019

@author: Jie.Hu
"""
# square matrix
X = [[1,2,3],
     [4,5,6],
     [7,8,9]]

trans_X = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        trans_X[j][i] = X[i][j]

trans_X   

[[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]



# rectangular
X = [[1,2],[3,4],[5,6]]

trans_X = [[0,0,0],
           [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        trans_X[j][i] = X[i][j]

trans_X        
         
[[X[j][i] for j in range(len(X))] for i in range(len(X[0]))] 



X = [[1,2],[3,4],[5,6]]
for i in range(len(X)):
    for j in range(len(X[0])):
        trans_X[j][i] = X[i][j]
trans_X
[i[::-1] for i in trans_X]

import numpy as np
np.transpose(X)

# final version
A = [[1,2],[3,4],[5,6]]

trans_A = [[0,0,0],
           [0,0,0]]
#transpose
for i in range(len(A)):
    for j in range(len(A[0])):
        trans_A[j][i] = A[i][j]
#reverse col
[i[::-1] for i in trans_A]
#reverse row
trans_A[::-1]

#method 2
[[X[j][i] for j in range(len(A))] for i in range(len(A[0]))]

[[X[i][j] for i in range(len(A))] for j in range(len(A[0]))]

# practise
A = [[1,2],[3,4],[5,6]]

trans_A = [[0,0,0],
           [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        trans_A[j][i] = A[i][j]

trans_A

[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]        

[i[::-1] for i in trans_A]

trans_A[::-1]

[trans_A[i] if i%2==0 else trans_A[i][::-1] for i in range(len(trans_A))]

