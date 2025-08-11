from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        max_height, max_dia = self.maxDiameter(root)
        
        return max_dia
    

    def maxDiameter(self,root):
        
        if not root.left and not root.right:
            return 0,0
        
        left_height,right_height,left_max_dia,right_max_dia = 0,0,0,0

        if root.left:
            left_height,left_max_dia = self.maxDiameter(root.left)
            left_height+=1
        
        if root.right:
            right_height, right_max_dia = self.maxDiameter(root.right)
            right_height+=1
        
        return max(left_height,right_height), max(left_max_dia,right_max_dia,left_height+right_height)

# bin_tree = TreeNode(1,TreeNode(2, TreeNode(4, TreeNode(6, TreeNode(10)), TreeNode(7)),TreeNode(5, TreeNode(8, TreeNode(11), TreeNode(12, TreeNode(13))), TreeNode(9))),TreeNode(3))
bin_tree = TreeNode(1,TreeNode(2, TreeNode(4, TreeNode(5), TreeNode(6))),TreeNode(3))
# bin_tree = TreeNode(1,TreeNode(2))
print(Solution().diameterOfBinaryTree(bin_tree))
            
        
        