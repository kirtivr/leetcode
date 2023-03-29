# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumFromNode(self, node, currentNum, currentSum):
        if node == None:
            return currentSum

        currentNum = currentNum * 10 + node.val
        
        if node.left == None and node.right == None:
            return currentSum + currentNum

        return self.sumFromNode(node.left, currentNum, currentSum) + self.sumFromNode(node.right, currentNum, currentSum)
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumFromNode(root, 0, 0)
