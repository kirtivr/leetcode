# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isSame(l,r):
            if l == None and r == None:
                return True
            elif l == None or r == None:
                return False
        
            return l.val == r.val and isSame(l.left,r.right) and isSame(l.right,r.left)

        if root == None:
            return True

        return isSame(root.left,root.right)
