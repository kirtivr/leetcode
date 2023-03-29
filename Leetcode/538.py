# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''

             7
  5                         9

3  6                     8   10                     

'''
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """


        def greaterTree(node, currentSum):
            if node == None:
                return 0

            rSum = greaterTree(node.right, currentSum)
            lSum = greaterTree(node.left, rSum + currentSum + node.val)

            node.val = currentSum + node.val + rSum
            return node.val+lSum+rSum

        return root
