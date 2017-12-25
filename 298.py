# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        left = self.longestConsecutive(root.left)
        right = self.longestConsecutive(root.right)

        if root.left and root.left.val == root.val + 1:
            left = left + 1

        if root.right and root.right.val == root.val + 1:
            right = right + 1

        return max(1,left,right)
