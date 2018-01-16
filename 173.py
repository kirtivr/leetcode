# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        parent = root
        curr = parent

        
        while curr != None:
            while curr != None:
                self.stk.append(curr)
                curr = curr.left
        print(self.stk)
    def hasNext(self):
        """
        :rtype: bool
        """
        

    def next(self):
        """
        :rtype: int
        """
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
