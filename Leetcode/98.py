# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def compareBST(root):
            if root == None:
                return (True,None,None)

            if root.left == None and root.right == None:
                return (True,root.val,root.val)

            (lv, ll,lr) = self.isValidBST(root.left)
            (lv, rl, rr) = self.isValidBST(root.right)

            ll = min(ll,rl,root.val,lr)
            lr = max(lr,ll,rl,rr,root.val)
            
            lv = (root.val > ll) and (root.val < lr) 

            return (lv,ll,lr)

        
        return compareBST(root)[0]
