class Solution:
    
    def searchTree(self, root, node, k):
        if root == None:
            return False

        if root.val == k and root != node:
            return True
        elif root.val > k:
            return self.searchTree(root.left,node,k)
        else:
            return self.searchTree(root.right,node,k)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        if root == None:
            return False
        
        def searchTwo(node, k):
            diff = k - node.val
            return self.searchTree(root, node, diff) or searchTwo(node.left, k) or searchTwo(node.right, k)

        
        return searchTwo(root,k)
