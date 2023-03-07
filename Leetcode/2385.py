from typing import List, Optional, Tuple
import math
import ast
import pdb
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
    def __init__(self) -> None:
        self.maxTime = 0

    def traverse(self, root: Optional[TreeNode], start: int):
        if root == None:
            return (False, -1)

        if root.val == start:
            # Root is infected.
            # Return the amount of time it takes to reach the leaf node.
            lh = self.traverse(root.left, start)[1]
            rh = self.traverse(root.right, start)[1]
            self.maxTime = max(self.maxTime, 1 + max(lh, rh))
            #print(f'\n{root.val} found!, lh = {lh} rh = {rh}  max = {self.maxTime} out = {(True, 1 + max(lh, rh)  if lh > 0 or rh > 0 else 0)}')
            return (True, 0)

        (lf, lh) = self.traverse(root.left, start)
        (rf, rh) = self.traverse(root.right, start)

        if lf and rh >= 0:
            # It takes one minute to percolate up and then one minute to get to the right node.
            self.maxTime = max(self.maxTime, max(1, 1 + lh, 2 + lh + rh))
        elif rf and lh >= 0:
            self.maxTime = max(self.maxTime, max(1, 1 + lh, 2 + lh + rh))
        elif lf or rf:
            self.maxTime = max(self.maxTime, max(1, 1 + lh, 1 + rh))

        outh = 0
        if lf:
            outh = 1 + lh
        elif rf:
            outh = 1 + rh
        else:
            outh = 1 + max(lh, rh)

        out = (lf or rf, outh)
        #print(f'\ncurrent node = {root.val} lf = {lf} rf = {rf} lh = {lh} rh = {rh} max = {self.maxTime} out = {out}')
        return out
        
    def amountOfTime(self, input: List[int], start: int) -> int:
        root = self.CreateTree(input)
        self.traverse(root, start)
        return self.maxTime

    def CreateTree(self, input: List[int]) -> TreeNode:
        root = MakeBinaryTreeFromList(input)
        #PrintTree(root)
        return root

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2385_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        start = ast.literal_eval(f.readline())
        #print(edges)
        print(x.amountOfTime(n, start))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')