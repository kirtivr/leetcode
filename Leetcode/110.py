from typing import List, Optional, Tuple
import math
import pdb
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def PrintTree(root: Optional[TreeNode]):
    if root == None:
        print("", end = "")
        return

    print(f'({root.val}', end = " ")

    PrintTree(root.left)
    PrintTree(root.right)
    print(f')', end = " ")

def MakeBinaryTreeFromList(input: List[int]):
    if not input:
        return None
    root = None
    current = None
    # If element at "i" is root, element at "i + 1" is left
    # and element at "i + 2" is right.
    i = 0
    queue = [TreeNode(input[0], None, None)]
    while queue:
        parent = queue.pop(0)
        if parent.val == None:
            continue
        if root == None:
            root = parent
        if i * 2 + 1 < len(input) and input[i * 2 + 1] is not None:
            new_node = TreeNode(input[i * 2 + 1], None, None)
            queue.append(new_node)
            parent.left = new_node
        if i * 2 + 2 < len(input) and input[i * 2 + 2] is not None:
            new_node = TreeNode(input[i * 2 + 2], None, None)
            queue.append(new_node)
            parent.right = new_node
        i += 1
    return root

def Height(head: Optional[TreeNode]):
    if head == None:
        return 0

    return max(1 + Height(head.left), 1 + Height(head.right))

def CountNodes(head: Optional[TreeNode]):
    if head == None:
        return 0

    return 1 + CountNodes(head.left) + CountNodes(head.right)

class Solution:
    def CheckBalanced(self, head: Optional[TreeNode]):
        if head == None:
            return (True, 0)

        (left_balanced, left_height) = self.CheckBalanced(head.left)
        (right_balanced, right_height) = self.CheckBalanced(head.right)
        balanced = abs(left_height - right_height) <= 1
        return (left_balanced and right_balanced and balanced, max(1 + left_height, 1 + right_height))

    def isBalanced(self, head: Optional[TreeNode]):
        return self.CheckBalanced(head)[0]

    def CreateTree(self, input: List[int]) -> TreeNode:
        root = MakeBinaryTreeFromList(input)
        PrintTree(root)
        return root

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    input = [1,2,2,3,3,None, None,4,4]
    #input = [1,2,3,4,5,6,None,8]
    root = x.CreateTree(input)
    print(x.isBalanced(root))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')