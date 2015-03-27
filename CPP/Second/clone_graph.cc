#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node == nullptr)
            return nullptr;
        unordered_map<const UndirectedGraphNode*, UndirectedGraphNode*> graph;
        queue<const UndirectedGraphNode*> q;
        q.push(node);
        graph[node] = new UndirectedGraphNode(node->label);
        while(!q.empty()) {
            const UndirectedGraphNode* curr = q.front();
            q.pop();
            for (auto nb: curr->neighbors) {
                if (graph.find(nb) == graph.end()) {
                    UndirectedGraphNode* copy = new UndirectedGraphNode(nb->label);
                    graph[nb] = copy;
                    graph[curr]->neighbors.push_back(copy);
                    q.push(nb);
                } else {
                    graph[curr]->neighbors.push_back(graph[nb]);
                }
            }
        }
        return graph[node];
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
