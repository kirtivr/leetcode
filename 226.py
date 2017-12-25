# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or (root.left == None and root.right == None):
            return root

        elif root.left == None or root.right == None:
            if root.right != None:
                root.left = self.invertTree(root.right)
                root.right = None
            
            elif root.left != None:
                root.right = self.invertTree(root.left)
                root.left = None
            
        else:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp


        return root
