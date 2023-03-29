# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        currlevel = 0
        return self.findInTree(root, k, currlevel)[0]

    def findInTree(self, root, k, index):
        if root == None:
            return (index, False)
        
        (index,found) = self.findInTree(root.left, k, index)[0]

        if found == True:
            return (index, True)
        
        index = index + 1

        if index == k:
            return (root.val, True)
        
        (index, found) = self.findInTree(root.right, k, index)

        if found == True:
            return (index, True)

        return (index, False)
