# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:26:20 2020

@author: STSC
"""

# String rotation
def strrotate(S1, S2):
    if len(S1) != len(S2):return False
    S = S1+S1
    
    if S.count(S2) >0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(strrotate("water","terwe"))