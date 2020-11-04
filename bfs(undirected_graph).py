# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:22:55 2020

@author: STSC
"""

# Breadth First Search Implementation // undirected Graph


from queue import Queue


       

adj_list = {
"A" : ["B", "D"],
"B" : ["A", "C"],
"C" : ["B"],
"D" : ["A", "E", "F"],
"E" : ["D", "F", "G"],
"F" : ["D", "E", "H"],
"G" : ["E", "H"],
"H" : ["G", "F"]
}
visited = {}
level ={}
bfs_output = []
parent ={}
queue =Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1
    
s ="A"
level[s]= 0
visited[s] =True
queue.put(s)

while not queue.empty():
    u =queue.get()
    bfs_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            queue.put(v)
            visited[v]=True
            parent[v]= u
            level[v]=level[u]+1
print(bfs_output)
 
#to find part from source node to given node  
node ="G"
path= [] 
while node is not None:
    path.append(node)
    node = parent[node] 

path.reverse()
print("path from source node to given node is" , path)    
            
        
        
 