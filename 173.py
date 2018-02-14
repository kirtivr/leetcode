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
        
        while curr and len(self.stk) > 0:
            while curr.left != None:
                curr = curr.left
                self.stk.append(curr)
            
            print(curr.val)
            
            if curr.right != None:
                self.stk.append(curr.right)
                curr = curr.right
            else:
                curr = self.stk.pop()
            #for i in range(len(self.stk)):
            #    print(self.stk[i].val)
        
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
        
