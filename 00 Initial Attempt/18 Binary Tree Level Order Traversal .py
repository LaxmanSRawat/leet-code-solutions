from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        nodes = deque()
        nodes.append(root)
        while(nodes):
            currentLevel = []

            for _ in range(0,len(nodes)):
                currentNode = nodes.pop()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    nodes.append(currentNode.left)
                if currentNode.right:
                    nodes.append(currentNode.right)
            result.append(currentLevel)
        return result

bt = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15),TreeNode(7)))
print(Solution().levelOrder(bt))

                
        