class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def compareBST(root,minVal, maxVal):
            if root == None:
                return True

            if root.val >= maxVal or root.val <= minVal:
                return False

            return compareBST(root.left,minVal,root.val) and compareBST(root.right,root.val,maxVal)

        return compareBST(root,-float("inf"), float("inf"))
