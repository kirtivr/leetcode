# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


        if root == None:
            return None

        if root.left == None and root.right == None:
            return None
        
        #if root.left == None:
        #    return self.lowestCommonAncestor(root.right,p,q)
        #elif root.right == None:
         #   return self.lowestCommonAncestor(root.left,p,q)

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        elif root.val >= p.val and root.val >= q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
