# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverseTree(node,array = []):
    if node:
        if len(array) == 0:
            array.append(node.val)
    else:
        return array
    if node.left:
        array.append(node.left.val)
    if node.right:
        array.append(node.right.val)
    array = traverseTree(node.left, array)
    array = traverseTree(node.right, array)
    return array

def printTree(node):
    print(traverseTree(node, []))

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return invertTree1(root)        

def invertTree1(root):
    if (root and (root.left or root.right)):
        dummy = root.left
        root.left = root.right
        root.right = dummy
        invertTree1(root.left)
        invertTree1(root.right)
    return root
    
bt1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),TreeNode(7, TreeNode(6),TreeNode(9)))
bt2 = TreeNode(2, TreeNode(1),TreeNode(3))
printTree(bt1)

solution_obj = Solution()
printTree(solution_obj.invertTree(bt1))

printTree(bt2)
printTree(solution_obj.invertTree(bt2))

printTree(None)
printTree(solution_obj.invertTree(None))