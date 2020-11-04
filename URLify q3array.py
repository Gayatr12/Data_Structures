# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:57:07 2020

@author: STSC
"""

#replace space with '%20

def rep(word):
    space_count = 0
    word = word.strip()
    truelength = len(word)
    
    for i in range(truelength-1):
        
        if word[i] ==' ':
            
            space_count +=1
        index = truelength + space_count*2
    
    word = list(word) 
    for f in range(truelength - 2, index - 2):
        word.append('0')
       
    for i in range(truelength-1,-1,-1):
        
        if word[i] ==' ':
            word[index-1] = "0"
            word[index-2] = "2"
            word[index-3] = "%"
            index -=3
        else:
            word[index-1] = word[i]
            index -=1
    return ''.join(word)

if __name__=='__main__': 
    
    ans =rep("Mr John Smith ")
    print(ans)

