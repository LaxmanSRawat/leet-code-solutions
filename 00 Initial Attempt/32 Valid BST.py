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
        def checkValidBST(node,check_greater_than_array,check_lesser_than_array):
            
            if node == None:
                print("current node val ", "None")
                return True

            print("current node val ", node.val)

            for i in check_greater_than_array:
                print("left check", i, node.val)
                if i <= node.val:
                    return False
            for i in check_lesser_than_array:
                print("right check", i, node.val)
                if i >= node.val:
                    return False

            
            check_greater_than_array.append(node.val)
            left_result = checkValidBST(node.left,check_greater_than_array,check_lesser_than_array)
            check_greater_than_array.pop()

            check_lesser_than_array.append(node.val)
            right_result = checkValidBST(node.right,check_greater_than_array,check_lesser_than_array)
            check_lesser_than_array.pop()
            

            return left_result and right_result
        
        return checkValidBST(root,[],[])

# bt = TreeNode(2,TreeNode(1),TreeNode(3))
# bt = TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3), TreeNode(6)))
bt = TreeNode(5,TreeNode(4),TreeNode(6,TreeNode(3), TreeNode(7)))

print(Solution().isValidBST(bt))


        
