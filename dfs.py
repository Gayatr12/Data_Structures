# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:46:46 2020

@author: STSC
"""
# for directed Graph


class Graph:
    
    def __init__(self, v):
        self.m_v =v
        self.m_adj =[[] for i in range(v)]
    
    def addEdge(self,u,v):
        self.m_adj[u].append(u)
        
        
#using recursion
    def Dfs_re(self,i,visited):
        visited[i] =True
        print(i)
        for u in self.m_adj[i]:
            if not visited[u]:
                Dfs_rec(u,visited)
                
# using Iteration
    def Dfs_it(self,i,visted):
        s =[]
        s.append(i)
        print(s)
        visted[i] =True
        while len(s)> 0:
            u = s[-1]
            s.pop()
            print(u)
            for v in self.m_adj[u]:
                if not visted[v]:
	                s.append(v)
	                visted[v] = True
            
                            
    def Dfs(self):
        
        visited = [False]*self.m_v
      
        for i in range(self.m_v):
            if not visited[i]:
                self.Dfs_it(i,visited)
            
G = Graph(5)
G.addEdge(0,1)
G.addEdge(0,3)
G.addEdge(1,2)
G.addEdge(3,2)
G.addEdge(3,4)
G.Dfs()


