# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:03:49 2020

@author: STSC
"""

def compress(chars):
        
        
        chars = list(chars)
        if len(chars) == 1:
            return 1
        count, j, prev = 1, 0, chars[0]
        chars.append(chr(34))
        
        for i in range(1, len(chars)):
            print(i)
            if prev == chars[i]:
                count+=1
            else:
                
                comp_str = prev + str(count) if count > 1 else prev
                chars[j:j+count] = comp_str
                prev, j, count = chars[i], j+len(comp_str), 1
                
        return ''.join(chars)
    

if __name__ == '__main__':
    print(compress("aabbcdcxcdddd"))