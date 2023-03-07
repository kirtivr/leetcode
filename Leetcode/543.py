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
    def diameterAndHeight(self, head: Optional[TreeNode]):
        if head == None:
            return (0, 0)
        
        (ld, lh) = self.diameterAndHeight(head.left)
        (rd, rh) = self.diameterAndHeight(head.right)
        print(f'diameter at {head.left.val if head.left else None} = {ld} height = {lh}')
        print(f'diameter at {head.right.val if head.right else None} = {rd} height = {rh}')
        dia = max(ld, rd)
        dia = max(dia, lh + rh)
        return (dia, 1 + max(lh, rh))

    def diameterOfBinaryTree(self, head: Optional[TreeNode]):
        # For each node, return its diameter which is the height sum of
        # the left subtree and the right subtree.
        return self.diameterAndHeight(head)[0]

    def CreateTree(self, input: List[int]) -> TreeNode:
        root = MakeBinaryTreeFromList(input)
        PrintTree(root)
        return root

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    #input = [1,2,2,3,3,None, None,4,4]
    input = [1,2]#,3,4,5]
    root = x.CreateTree(input)
    print(f'\n{x.diameterOfBinaryTree(root)}')
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')