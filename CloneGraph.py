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