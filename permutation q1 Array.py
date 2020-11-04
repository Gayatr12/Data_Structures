# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:48:48 2020

@author: STSC
"""

# Check if two string are permutation of each other

def per(s1,s2):
    if (len(s1) != len(s2)):
        return  False
    
    return sorted(s1) == sorted(s2)

if __name__=='__main__': 
    
    print(per("dog","god"))
    