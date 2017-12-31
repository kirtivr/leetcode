# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        inorder = []
        
        traverse(root,inorder)

        def traverse(root,l):

            if root == None:
                return

            traverse(root.left)
            l.append(root.val)
            traverse(root.right)


        return inorder
