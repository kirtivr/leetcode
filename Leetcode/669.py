# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeSubtree(self, root: Optional[TreeNode]):
        if root == None:
          return
        if root.left == None and root.right == None:
          return
        self.removeSubtree(root.left)
        root.left = None
        self.removeSubtree(root.right)
        root.right = None
    def findElementInTree(self, root: Optional[TreeNode], low: int, high: int):
      if root == None:
        return root
      if root.val >= low and root.val <= high:
        return root
      if root.val < low:
        return self.findElementInTree(root.right, low, high)
      return self.findElementInTree(root.left, low, high)
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
      # invariant: parent is in the tree
      def trimBSTWithGivenParent(node: Optional[TreeNode], parent: Optional[TreeNode]):
        if node == None:
          return node
        if node.val >= low and node.val <= high:
          trimBSTWithGivenParent(node.left, node)
          trimBSTWithGivenParent(node.right, node)
          return root
        if node.val < low:
          self.removeSubtree(node.left)
          node.left = None
          parent.left = self.trimBST(node.right, low, high)
        elif node.val > high:
          self.removeSubtree(node.right)
          node.right = None
          parent.right = self.trimBST(node.left, low, high)
      node = self.findElementInTree(root, low, high)
      if node == None:
        return None
      trimBSTWithGivenParent(node.left, node)
      trimBSTWithGivenParent(node.right, node)
      return node
