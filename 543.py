# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxD = 0
        
        def getDiameter(root):
            nonlocal maxD
            
            if root == None:
                return 0
            elif root.left == None and root.right == None:
                return 1
            else:
                leftD = getDiameter(root.left)
                rightD = getDiameter(root.right)
                
                maxD = max(leftD+rightD,maxD)

                return 1+max(leftD,rightD)

        getDiameter(root)
        
        return maxD

        
