# -*- coding: utf-8 -*-
from collections import deque

"""
二分图定义：一个图的顶点可以分为两个集合X和Y，图中所有边一定是有一个顶点
属于X，另一个顶点属于Y。
这里用无向图（不知道为什么，test 二分图都是无向图）
并且是 Strongly Connected Graph。

"""

graph_true = {'A': ['B','D'],
              'B': ['A','C'],
              'C': ['D'],
              'D': ['A','C','E'],
              'E': ['D'] }


graph_f1 = {
    'A': ['B', 'C'],
    'B': [],
    'C': [],
    'D': ['B']
}
def isBipartite(graph = None, src = ''):
    # @param graph: a dictionary repesented digraph
    # @param src: the start vertex
    # @return boolean: whether the graph is bipartite
    if not src:
        return False

    queue = deque([src])
    colored = {}
    colored[src] = True
    
    while queue:
        cur = queue.popleft()
        color = not colored[cur]
        for v in graph[cur]:
            if v not in colored:
                colored[v] = color
                queue.append(v)
            else:
                if colored[v] != color:
                    return False
                
    if len(colored) < len(graph):
        return False                
    return True

print isBipartite(graph_true, 'A')
