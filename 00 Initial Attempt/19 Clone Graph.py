
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
def print_graph(node):
    if not node:
        print("Graph is empty.")
        return

    visited = set()

    def dfs(n):
        if n in visited:
            return
        visited.add(n)

        # Print current node and its neighbors
        neighbor_vals = [neighbor.val for neighbor in n.neighbors]
        print(f"Node {n.val}: Neighbors -> {neighbor_vals}")

        # Continue DFS for each neighbor
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        hash = {}

        if not node:
            return node
        
        rootNode = Node(node.val,[])
        hash[node.val] = rootNode

        rootNode  = self.handleNode(node,rootNode,hash)

        return rootNode
  
    def handleNode(self,node,copiedNode,hash):
        for neighboringNode in node.neighbors:
            if neighboringNode.val not in hash:
                copiedNeighbor = Node(neighboringNode.val,[])
                hash[neighboringNode.val] = copiedNeighbor
                copiedNode.neighbors.append(copiedNeighbor)
                copiedNeighbor = self.handleNode(neighboringNode,copiedNeighbor,hash)
            else:
                copiedNode.neighbors.append(hash[neighboringNode.val])
            
        return copiedNode
    
n1 = Node(1,[])
n2 = Node(2,[])
n3 = Node(3,[])
n4 = Node(4,[])

n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n1)
n2.neighbors.append(n3)
n3.neighbors.append(n2)
n3.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n3)

# print_graph(n1)
n5 = Node(5,[])

print_graph(Solution().cloneGraph(n5))