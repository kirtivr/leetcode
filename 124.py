# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        def findSum(root):
            if root == None:
                return [(None,False)]

            if root.left == None and root.right == None:
                return [(root.val,False)]

            lpaths = findSum(root.left)
            if root.left:
                print(' for '+str(root.left.val)+ ' got '+str(leftSum) +' internal = '+str(il))
            rpaths = findSum(root.right)
            
            if root.right:
                print(' for '+str(root.right.val)+ ' got '+str(rightSum) +' internal = '+str(ir))
                
            if leftSum == None:
                if ir:
                    if root.val > rightSum:
                        return (root.val,False)
                    else:
                        return (rightSum,True)

                if rightSum > root.val and rightSum > root.val + rightSum:
                    return (rightSum,True)
                else:
                    return (max(root.val,root.val+rightSum),False)
            elif rightSum == None:
                if il:
                    if root.val > leftSum:
                        return (root.val,False)
                    else:
                        return (leftSum,True)
                
                if leftSum > root.val and leftSum > root.val + leftSum:
                    return (leftSum,True)
                else:
                    return (max(root.val,root.val+leftSum),False)
            else:
                if il and not ir:
                    if root.val > leftSum or root.val + rightSum > leftSum:
                        return (max(root.val,root.val+rightSum),False)
                    else:
                        return (leftSum,True)
                elif ir and not il:
                    if root.val > rightSum or root.val + leftSum > rightSum:
                        return (max(root.val,root.val+leftSum),False)
                    else:
                        return (rightSum,True)
                elif ir and il:
                    if root.val > leftSum and root.val > rightSum:
                        return (root.val,False)
                    else:
                        return (max(leftSum,rightSum),True)
                else:
                    if leftSum > root.val and leftSum > leftSum + root.val and leftSum > root.val + rightSum:
                        return (leftSum,True)
                    elif rightSum > root.val and rightSum > root.val + rightSum and rightSum > root.val + leftSum:
                        return (rightSum,True)
                    
                    imax = max(root.val,root.val+leftSum,root.val+rightSum)
                    if root.val + leftSum + rightSum > imax:
                        return [(root.val + leftSum + rightSum, True),(imax,False)]
                    else:
                        return [(imax,False)]

        return findSum(root)[0]
