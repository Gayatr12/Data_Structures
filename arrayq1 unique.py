# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:35:45 2020

@author: STSC
"""

# is unique 
# with extra space
# def unique(str):
#     dic = {}
    
#     for c in str:
#         if c in dic:
#             return False
#         else:
#             dic[c] = 1
#     return True

#without extra space

def unique(str):
    for i in range(len(str)-1):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False
    return True
        



if __name__ =="__main__":
    ans =unique("asfjsa")
    print(ans)