# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        orderDict = self.orderNodes(root, {}, 0, 0)
        # flatten
        levels = orderDict.keys()
        levels = sorted(levels)

        build = []
        for level in levels:
            line = orderDict[level]
            # order line by depth
            line = sorted(line, key=lambda x:x[1])
            lineVals = [x for (x,y) in line]
            build.append(lineVals)
            
        return build

    def orderNodes(self, root, order, level, depth):

        if root == None:
            return order

        if level in order:
            order[level].append((root.val, depth))
        else:
            order[level] = [(root.val, depth)]

        order = self.orderNodes(root.left, order, level - 1, depth + 1)
        order = self.orderNodes(root.right, order, level + 1, depth + 1)
        
        return order
