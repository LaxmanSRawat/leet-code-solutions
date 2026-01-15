'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100'''

'''Intuition: We can use Depth-First Search (DFS) to traverse the tree. At each node, we calculate the maximum depth of its left and right subtrees and return the greater of the two depths plus one (to account for the current node). If we reach a null node, we return a depth of zero.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                return max(dfs(node.left)+1,dfs(node.right)+1)
            else:
                return 0
        return dfs(root)
        