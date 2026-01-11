# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None or checkHeight(root):
            return True
        return False 

def checkHeight(root):
    if root:
        left_height = checkHeight(root.left)
        right_height = checkHeight(root.right)
        # print(root.val, left_height,right_height)
        if(((not left_height) and (root.left)) or ((not right_height) and (root.right))):
            # print("here", left_height, not root.left, right_height, not root.right)
            return False
        if (left_height - right_height <-1 or left_height-right_height >1):
            return False
        if left_height > right_height:
            return left_height +1
        return right_height +1
    return 0

bt = TreeNode(3,TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7)))

solObj = Solution()
# print(solObj.isBalanced(bt))

bt = TreeNode(1,TreeNode(2, TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))
print(solObj.isBalanced(bt))


        
