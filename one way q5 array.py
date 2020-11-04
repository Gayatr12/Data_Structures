# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:52:23 2020

@author: STSC
"""

# one way

def oneway(S,T):
    if len(S) == len(T):
        return oneedit(S,T)
    if len(S) == len(T)+1:
        return oneinsert(S,T)
    if len(S) +1 == len(T):
        return oneinsert(T,S)
    
    
def oneedit(S,T):
    replace = False
    for i in range(len(S)):
        if S[i] != T[i]:
            if replace :
                return False
            else:
                replace = True
    return True

def oneinsert(S,T):
    index1 =0 
    index2 = 0
    
    while(index1 <len(S) and index2 < len(T)):
        if S[index1] != T[index2] :
            if index1 !=index2:
                return False
            index1 +=1
        else:
            index1 +=1
            index2+=1
    return True
    
if __name__ == "__main__":
    print(oneway("pale","pal"))

            
            