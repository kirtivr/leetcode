from typing import List, Optional, Tuple
import pdb
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def PrintList(head: Optional[ListNode]):
    while head is not None:
        print(head.val, end = " ")
        head = head.next

def MakeNodes(input: List[int]):
    head = None
    current = None
    for i in range(len(input)):
        new_node = ListNode(input[i], None)
        if head == None:
            head = new_node
            current = new_node
            continue
        current.next = new_node
        current = new_node
    return head

def AddAfter(node: Optional[ListNode], to_add: int):
    if node == None:
        return

    next = node.next
    new_node = ListNode(to_add, next)
    node.next = new_node

def Length(head: Optional[ListNode]):
    out = 0
    while head is not None:
        out += 1
        head = head.next
    return out

def ElementAt(head: Optional[ListNode], idx: int):
    out = 0
    while head is not None:
        out += 1
        if idx == out:
            return head
        head = head.next
    return None

class Solution:
    def partitionAndSort(self, head: Optional[ListNode]):
        pass                

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    nodes = MakeNodes([1, 2, 3, 4, 5])
    PrintList(nodes)
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')
