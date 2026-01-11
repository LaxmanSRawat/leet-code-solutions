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
        nodes = []
        nodes.append(root)
        childNodes = []
        currentLevel = []
        while(len(nodes) > 0 and nodes[0]):
            currentNode = nodes.pop(0)
            currentLevel.append(currentNode.val)
            if currentNode.left:
                childNodes.append(currentNode.left)
            if currentNode.right:
                childNodes.append(currentNode.right)
            if len(nodes) == 0 and len(childNodes) >= 0:
                nodes,childNodes = childNodes,[]
                result.append(currentLevel)
                currentLevel = []
        return result

bt = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15),TreeNode(7)))
print(Solution().levelOrder(bt))

                
        