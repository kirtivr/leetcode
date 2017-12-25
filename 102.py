# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root, level, out):
        if root == None:
            return

        self.traverse(root.left, level + 1, out)
        
        while len(out) < level:
            out.append([])
        
        out[level - 1].append(root.val)

        self.traverse(root.right, level + 1, out)
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        out = []
        self.traverse(root, 1, out)

        return out
