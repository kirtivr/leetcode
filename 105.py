# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        N = len(preorder)

        if N == 0:
            return None
        table = {}
        for i in range(N):
            table[preorder[i]] = i

        r = TreeNode(preorder[0])

        left = []
        right = []
        
        for i in range(N):
            if inorder[i] == r.val:
                left = inorder[0:i]
                right = inorder[i+1:]
                break

        def construct(root, left, right):
            nonlocal table
            if len(left) == len(right) == 0:
                return

            leftIdx = None
            rightIdx = None
            leftMin = None
            rightMin = None
            
            for i in range(len(left)):
                node = left[i]
                if leftIdx == None or table[node] < leftMin:
                    leftIdx = i
                    leftMin = table[node]
                    
            for i in range(len(right)):
                node = right[i]
                if rightIdx == None or table[node] < rightMin:
                    rightIdx = i
                    rightMin = table[node]
                    
            #print(' left idx = '+str(leftIdx)+' rightIdx = '+str(rightIdx))
            
            if leftIdx != None:
                root.left = TreeNode(left[leftIdx])
                newLeft = left[0:leftIdx]
                newRight = left[leftIdx+1:]
                #print('left of root = '+str(root.val)+' is '+str(root.left.val))
                construct(root.left, newLeft, newRight)

            if rightIdx != None:
                root.right = TreeNode(right[rightIdx])
                newLeft = right[0:rightIdx]
                newRight = right[rightIdx+1:]
                #print('righft of root = '+str(root.val)+' is '+str(root.right.val))
                construct(root.right, newLeft, newRight)

        
        #print(left)
        #print(right)
        construct(r,left,right)
        return r
            
