# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:45:30 2020

@author: STSC
"""

#palindrome permutation

def paliper(string):
    if len(string) == 0 or len(string) ==1:
        return True
    dic ={}
    string = string.lower()
    for c in string:
        if c != ' ':
            if c in dic:
                dic[c]+=1
            else:
                dic[c] =1
   
        
    isodd = False
    for keys in dic:
        if dic[keys] %2 !=0:
            if isodd:
                return False
            else:
                isodd = True
    return True

if __name__ == '__main__':
    print(paliper('T'))