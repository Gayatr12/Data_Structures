# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:20:25 2020

@author: STSC
"""

#LinkedList

# creating LinkedList and printing

class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        
    def printlink(self,head):
        temp = head
        while (temp):
            print(temp.data,"--->", end =" ")
            temp = temp.next
            
        print("None")
        
     # reverse the linklist
    def reverse(self,head):
        temp = head
        prev = None
        
        while(temp):
            Nxt =temp.next
            temp.next =prev
            prev = temp
            temp = Nxt
        
        return prev
    
   
    # check if linklist is has cycle
    def checkCycle(self, head):
        slow = head
        fast = head
            
        while (fast.next !=None):
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False
    
        
        
                
                 
    
    
# 
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    llist.head.next = second;
    second.next = third
    
    print("LinkedList:")
    llist.printlink(llist.head)
    
    rev_list = llist.reverse(llist.head)
    print("Reverse LinkList:")
    llist.printlink(rev_list)
    
    if llist.checkCycle(llist.head):
        print("Linklist contain Cycle")
    else:
        print("Linklist does not contain Cycle")
    
    
    
    
        
    
    
         
    