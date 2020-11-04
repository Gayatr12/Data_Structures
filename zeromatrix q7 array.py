# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:39:32 2020

@author: STSC
"""

# zero matrix
def zero(A):
    n = len(A)
    m =len(A[0])
    
    first_col =-1
    first_row = -1
    
    for i in range(n):
        for j in range(m):
            if A[i][j] ==0 and i ==0:
                first_row = 1
            if A[i][j] ==0 and j ==0:
                first_col = 1
            if A[i][j] ==0:
                A[i][0] = A[0][j] = 0
                
    for i in range(1,n):
        if A[i][0] == 0:
            for j in range(1,m):
                A[i][j] = 0
                
    for i in range(1,m):
        if A[0][i] == 0:
            for j in range(1,n):
                A[j][i] = 0
    
    if first_row == 1:
        for i in range(1,m):
            A[0][i] =0
    
    if first_col ==1:
        for i in range(1,n):
            A[i][0] = 0
    
    print(A)
    
if __name__ == '__main__':
    zero([[0,1,2,0],[5,3,7,8],[3,6,8,1]])
    
                           

