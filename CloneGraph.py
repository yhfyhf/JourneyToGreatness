# Learn from x-zh
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = collections.deque()
        
        queue.append(node)
        #graph is a node.val to real node map
        graph = dict()
        #graph[node.label] = UndirectedGraphNode(node.label)

        while queue:
            n = queue.popleft()
            if n.label not in graph:
                graph[n.label] = UndirectedGraphNode(n.label)
                for nb in n.neighbors:
                    # for each real node, we assigin int to neighbor
                    graph[n.label].neighbors.append(nb.label)
                    queue.append(nb)

        # for each real node
        for n in graph.values():
            for k, v in enumerate(n.neighbors):
                # replace int back to read node
                n.neighbors[k] = graph[v]
        return graph[node.label]

    def cloneGraph1(self, node):
        '''
        dfs to visit each node
        A dict to mark visited nodes
        '''
        def dfs(node, map):
            # @param node, a undirected graph node
            # @param map, a dict
            # @return a undirected graph node
            if node in map:
                return map[node]
            else:
                res = UndirectedGraphNode(node.label)
                map[node] = res
                for nb in node.neighbors:
                    res.neighbors.append(dfs(nb, map))
                return res
        
        if not node:
            return None
        return dfs(node, {})


    def cloneGraph2(self, node):
        '''
        bfs to visit each node
        A dict to mark visited nodes
        key as original graph, value as copied graph
        '''
        if not node:
            return None
        queue = collections.deque()
        graph = {}
        queue.append(node)
        new_node = UndirectedGraphNode(node.label)
        graph[node] = new_node
        while queue:
            curr = queue.popleft()
            for nb in curr.neighbors:
                if nb not in graph:
                    copy = UndirectedGraphNode(nb.label)
                    graph[curr].neighbors.append(copy)
                    graph[nb] = copy
                    queue.append(nb)
                else:
                    # from directed graph to undirected graph
                    graph[curr].neighbors.append(graph[nb])
        return new_node
    
    def cloneGraph3(self, node):
        '''
        bfs to visit each node
        a dict, key as original node, val as copyied graph
        a queue, store visit sequence 
        '''
        if not node:
            return None
        mirror = {}
        queue = collections.deque()
        queue.append(node)
        new_node = UndirectedGraphNode(node.label)
        while queue:
            curr = queue.popleft()
            for nb in curr.neighbors:
                if nb not in mirror:
                    nb_copy = UndirectedGraphNode(nb.label)
                    mirror[nb] = nb_copy
                    mirror[curr].neighbors.append(nb_copy)
                    queue.append(nb)
                else:
                    mirror[curr].neighbors.append(mirror[nb])
        return new_node


    def cloneGraph4(self, node):
        '''
        dfs to visit each node
        a dict, key as original node, val as copyied graph
        a queue, store visit sequence 
        '''
        if not node:
            return None
        mirror = {}
        def dfs(node, mirror):
            if node in mirror:
                return mirror[node]
            copy = UndirectedGraphNode(node.label)
            mirror[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor, mirror))
            return copy
                
        dfs(node, mirror)
        return mirror[node]
         
if __name__ == '__main__':
    
