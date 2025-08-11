# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkValidBST(node,min_val,max_val):
            
            if node == None:
                return True

            if min_val < node.val < max_val:
                return checkValidBST(node.left, min_val,node.val) and checkValidBST(node.right,node.val,max_val)
            else:
                return False
           
        
        return checkValidBST(root,float("-inf"),float("inf"))

# bt = TreeNode(2,TreeNode(1),TreeNode(3))
# bt = TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3), TreeNode(6)))
bt = TreeNode(5,TreeNode(4),TreeNode(6,TreeNode(3), TreeNode(7)))

print(Solution().isValidBST(bt))


        
