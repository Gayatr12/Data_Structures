# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:09:20 2020

@author: STSC
"""

def operation(operations):
    res = []
    ans = []
    for opr in operations: 
        if opr[0] == 0:
            res.append(opr[1]*opr[2])
        elif opr[0]==1:
            print(opr)
            if not res:
                
                ans.append(True)
            else:
                for i in range(0,len(res)):
                    
                    if res[i] > opr[1]*opr[2]:
                        ans.append(False)
                        break
                    if i ==len(res)-1 :
                        if res[i] > opr[1]*opr[2]:
                        
                            ans.append(True)
                        else:
                            ans.append(False)
                        
                        
                    
                        
                    
                        
        

    
    print(ans)
    
if __name__=='__main__': 
     operation([[1,22,20],[1,29,5],[1,18,18],[0,6,6],[0,30,4],[1,9,25],[1,28,12],[0,4,20],[0,17,7],[0,6,6],[0,4,10],[0,26,11],[1,26,15],[1,4,22]])
                        
        
        