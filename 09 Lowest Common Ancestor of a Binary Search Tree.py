# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

def printTree(root):
    array = []
    if root:
        array = [root.val]
        array = traverseTree(root,array)
    return array

def traverseTree(root,array):
    if(root.left or root.right):
        if root.left:
            array.append(root.left.val)
        else:
            array.append('null')
        if root.right:
            array.append(root.right.val)
        else:
            array.append('null')
        if root.left:
            array = traverseTree(root.left,array)
        if root.right:
            array = traverseTree(root.right,array)
    return array


    

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p<q:
            lca = getLowestCommonAncestor(root,p,q)
        else:
            lca =getLowestCommonAncestor(root,q,p)
        return lca
    
def getLowestCommonAncestor(root,smallerInt,biggerInt):    
        if (root.val > smallerInt and root.val < biggerInt) or root.val == smallerInt or root.val == biggerInt:
            return root.val
        if (root.val < smallerInt):
            return getLowestCommonAncestor(root.right,smallerInt,biggerInt)
        else:
            return getLowestCommonAncestor(root.left,smallerInt,biggerInt)

bt = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4,TreeNode(3),TreeNode(5))), TreeNode(8,TreeNode(7),TreeNode(9)))
printTree(bt)

solObj = Solution()
print(solObj.lowestCommonAncestor(bt,2,8))
print(solObj.lowestCommonAncestor(bt,2,4))

bt = TreeNode(3, TreeNode(1))
print(solObj.lowestCommonAncestor(bt,3,1))

        