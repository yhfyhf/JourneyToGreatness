# -*- coding: utf-8 -*-
"""
Topological Sort
Given a set of partil order, get the possible total orders

Solution:
1. select the vertexes have no precursor (in degree as 0) and output them
2. delete the vetex and the edge end with this vetex
3. repeat 1 and 2 until graph is empty

http://blog.csdn.net/littlethunder/article/details/24113193
http://www.cnblogs.com/Bob-FD/archive/2012/10/23/2736132.html
http://www.geeksforgeeks.org/topological-sorting/
"""
class TopologicalSort():
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges

    def indegree0(self):
        if len(self.vertex) == 0:
            return None

        # 存储入度为0的节点
        vertex_copy = self.vertex[:]

        # remove edges which indegree are not 0
        # 只有在最开始的点，才不会是边中的终点
        for i in self.edges:
            if i[1] in vertex_copy:
                vertex_copy.remove(i[1])

        # 如果有环，在某一步计算indgree0的时候，所有的边都会消掉。
        if len(vertex_copy) == 0:
            return -1

        # 去掉入度为0的节点所在边们
        for t in vertex_copy:
            for i in xrange(len(self.edges)):
                if t in self.edges[i]:
                    self.edges[i] = 'X' # to delete

        self.edges = [x for x in self.edges if x != 'X']

        # different set vertex - vertex_copy
        # 去掉入度为0节点
        vertex_copy_set = set(vertex_copy)
        self.vertex = [x for x in self.vertex if x not in vertex_copy_set]
        return vertex_copy

    def topoSort(self):
        res = []
        while True:
            nodes = self.indegree0()

            # finished
            if nodes is None:
                break
            if nodes == -1:
                print 'Circle founded'
                return
            res.extend(nodes)
        return res



def topo2(v, e):
    stack = []
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for edge in e:
                if edge[1] == node:
                    dfs(edge[0])
            stack.append(node)
        return

    for node in v:
        dfs(node)
    while stack:
        print stack.pop()

def test2():
    v=['a', 'b', 'c', 'd', 'e', 'f', 'k']
    e=[('k', 'f'), ('k', 'a'), ('f', 'd'), ('a','b'),('a','d'),('b','c'),('d','c'),('d','e')]

    t = TopologicalSort(v, e)
    print t.topoSort()
    print '=================================='
    topo2(v, e)

if __name__ == '__main__':
    print 'test2',
    test2()
