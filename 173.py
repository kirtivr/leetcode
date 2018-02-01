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
        self.stk = [root]
        curr = root
        
        while curr != None:
            self.stk.append(curr.val)
            
            while curr.left != None:
                self.stk.append(curr.val)
                curr = curr.left

            if curr.right != None:
                curr = curr.right
            else:
                curr = self.stk.pop()
        
            print(self.stk)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk) > 0 

    def next(self):
        """
        :rtype: int
        """
        
        return self.stk.pop() if self.hasNext() else None
        
