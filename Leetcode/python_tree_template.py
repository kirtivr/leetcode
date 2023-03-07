from typing import List, Optional, Tuple
import math
import pdb
import ast
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    head: Optional[TreeNode]

def PrintTree(root: Optional[TreeNode]):
    if root == None:
        print("", end = "")
        return

    print(f'({root.val}', end = " ")

    PrintTree(root.left)
    PrintTree(root.right)
    print(f')', end = " ")

def BSTTraverseLeft(popped: Optional[TreeNode], pq, tq):
    curr = popped
    # Minimum element is curr or curr.left.
    while curr.left != None:
        curr = curr.left
        # Add to print queue.
        pq.append(curr)
        #print(f'update after adding curr = {curr.idx} pq = {pq} tq = {tq}')

def BSTTraverseInOrder(bst: BST, traversal, chunk):
    #pdb.set_trace()
    #PrintTree(bst.head)
    index = 0

    # Iterative In Order Traversal.
    # Traverse left until no more elements.
    tq = [bst.head]
    pq = []
    while (len(tq) > 0 or len(pq) > 0):
        popped = None
        if len(tq) > 0:
            popped = tq.pop()
            if popped == None:
                return
            pq.append(popped)
            if popped.left != None:
                BSTTraverseLeft(popped, pq, tq)
        elif len(pq) > 0:
            popped = pq.pop()
            # Add to traversal.
            traversal[index] = popped.idx
            index += 1
            # Add the right element to tq.
            if popped.right:
                tq.append(popped.right)
    return

def BSTInsert(bst: BST, priority: int, index: int):
    to_insert = TreeNode(priority, index, None, None)
    if bst.head == None:
        bst.head = to_insert
        return

    def TraverseTreeAndAdd(curr: Optional[TreeNode], to_insert: Optional[TreeNode]):
        # Curr cannot be None.
        if curr == None:
            print('Invariant broken')
            return

        if curr.val < to_insert.val:
            if curr.right == None:
                curr.right = to_insert
                return
            TraverseTreeAndAdd(curr.right, to_insert)        
            return
        else:
            if curr.left == None:
                curr.left = to_insert
                return
            TraverseTreeAndAdd(curr.left, to_insert)        
            return

    TraverseTreeAndAdd(bst.head, to_insert)

def MakeBSTFromSortedList(input: List[int]):
    # Making the BST from a sorted list lets it be more balanced compared to a
    # random list.
    if not input:
        return None

    def recurseAndCreateTreeFromList(input: List[int], left, right):
        if left > right:
            return

        mid = left + (right - left)//2

        root = TreeNode(input[mid], None, None)

        root.left = recurseAndCreateTreeFromList(input, left, mid - 1)
        root.right = recurseAndCreateTreeFromList(input, mid + 1, right)

        return root

    return recurseAndCreateTreeFromList(input, 0, len(input) - 1)

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

def MakeBSTFromList(input: List[int]):
    pass

def BSTTraverseInOrder(bst: BST, traversal):
    index = 0

    def do_traverse(curr: Optional[TreeNode], traversal):
        global index
        if curr == None:
            return
        
        do_traverse(curr.left)
        do_traverse(curr.right)

        traversal[index] = curr.val
        index += 1

    return

def BSTInsert(bst: BST, el: int):
    to_insert = TreeNode(el, None, None)
    if bst.head == None:
        bst.head = to_insert
        return

    def TraverseTreeAndAdd(curr: Optional[TreeNode], to_insert: Optional[TreeNode]):
        # Curr cannot be None.
        if curr == None:
            print('Invariant broken')
            return

        if curr.val < to_insert.val:
            if curr.right == None:
                curr.right = to_insert
                return
            TraverseTreeAndAdd(curr.right, to_insert)        
            return
        else:
            if curr.left == None:
                curr.left = to_insert
                return
            TraverseTreeAndAdd(curr.left, to_insert)        
            return

    TraverseTreeAndAdd(bst.head, to_insert)

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
        pass

    def CreateTree(self, input: List[int]) -> TreeNode:
        root = MakeBinaryTreeFromList(input)
        #PrintTree(root)
        return root

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('test_case.text', 'r') as f:
        input = ast.literal_eval(f.readline())
        root = x.CreateTree(input)
        print(x.isBalanced(root))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')