# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def __init__(self):
        self.levels = {0:[]}
    # @param root, a tree link node
    # @return nothing
    def doConnect(self,root,level):
        if root == None:
            return None

        leftMost = None
        if level in self.levels:
            leftMost = self.levels[level][-1]
            leftMost.next = root
            self.levels[level].append(root)
        else:
            self.levels[level] = [root]
            
        self.doConnect(root.left, level + 1)
        self.doConnect(root.right, level + 1)

        return root
    
    def connect(self, root):
        
        root = self.doConnect(root)
