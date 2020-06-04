#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).

class Solution:
    # def cloneGraph(self, node: 'Node') -> 'Node':
    # def cloneGraph(self, node):
    
    #     if not node:
    #         return

    #     head = copy_graph = Node(node.val)
    #     node = node.neighbors
    #     copy_graph = copy_graph.neighbors
    #     while(node):
    #         copy_graph = Node(node.val)
    #         node = node.neighbors
    #         copy_graph = copy_graph.neighbors

    #     copy_graph = None


    #     return head

    # def cloneGraph(self, node: 'Node') -> 'Node':
    def cloneGraph(self, node):
        if not node:
            return

        graph_dict = {}
        ans = self.dfs(node, graph_dict)
        print(graph_dict)

        return ans
        
    def dfs(self, node, graph_dict):
        if not node:
            return

        copy_graph = Node(node.val, [])
        graph_dict[node] = copy_graph
        for nei in node.neighbors:
            if nei in graph_dict:
                copy_graph.neighbors.append(graph_dict[nei])
            else:
                copy_graph.neighbors.append(self.dfs(nei, graph_dict))

        

            

        

# @lc code=end

