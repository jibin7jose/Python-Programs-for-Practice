# Python Program to Add Two Matrices.

A = [[1,3,5],
     [7,9,11],
     [13,15,17]]

B = [[2,4,6],
     [8,10,12],
     [14,16,18]]

Result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j] = A[i][j] + B[i][j]

for r in Result:
    print(r)
    