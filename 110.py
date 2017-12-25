# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):

        if root == None:
            return 0

        elif root.left == None and root.right == None:
            return 1

        else:
            return max(1+ self.getHeight(root.left), 1+ self.getHeight(root.right))
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True

        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)

        if abs(leftH - rightH) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
