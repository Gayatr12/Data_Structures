# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:57:01 2020

@author: STSC
"""
# rotate matrix 

def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(i+1, m):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
    for i in range(n):
        swaprow(matrix[i])
        
    print(matrix)
    
def swaprow(A):
    l = len(A)
    i =0
    j =l-1
    while(i < j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i+=1
        j -=1
    
if __name__ == '__main__':
    rotate([[1,2,3],[4,5,6],[7,8,9]])
    
            
    