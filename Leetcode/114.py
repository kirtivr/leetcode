# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        def recurse(root):
            if root == None:
                return None

            if root.left == None and root.right == None:
                return root

            lflat = self.flatten(root.left)
            rflat = self.flatten(root.right)

    
            if lflat:
                print(lflat.val)
                root.right = lflat
        
            while lflat.right != None:
                print(lflat.val)
                lflat = lflat.right

                lflat.right = rflat
            else:
                root.right = rflat
            
            root.left = None

            return root
    
        return
