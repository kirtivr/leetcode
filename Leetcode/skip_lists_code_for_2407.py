from typing import List, Optional, Tuple, Dict
import heapq
import pdb
import ast
import sys
from dataclasses import dataclass, field
from functools import cmp_to_key
import time

class ListNode:
    def __init__(self, val, idx):
        self.idx = idx
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return 'idx = ' + str(self.idx) + ' val = ' + str(self.val)

def AddAfter(node: ListNode, priority: int, idx: int):
    if node == None:
        return

    new_node = ListNode(priority, idx)
    next = node.next
    new_node.prev = node    
    new_node.next = next
    if next:
        next.prev = new_node

    node.next = new_node

def PrintList(head: Optional[ListNode]):
    while head is not None:
        print(f'idx = {head.idx} val = {head.val} next idx = {None if head.next == None else head.next.idx} prev idx = {None if head.prev == None else head.prev.idx}', end = "\n")
        head = head.next

# Transition from greater than to less than.
def FindClosestSkipListNodeBefore(sl, priority):
    #print('---------------------------')
    if sl[0].val < priority:
        return None

    def searchBinary(sl, left, right):
        nonlocal priority
        if left > right:
            return None

        mid = left + (right - left)//2

        # We found the right element when:
        # there is only one element in sl and this is the one.
        # or, mid.val <= priority < (mid + 1).val
        node = sl[mid]
        #print(f'cheking idx = {node.idx} val = {node.val} looking for val = {priority} left = {left} right = {right}')
        #if node == None:
        #    print(f'Line 48 Invariant violated')
        #    for i in range(len(sl)):
        #        print(f'i = {i} sl[i] = {sl[i]}')
        if (node.val > priority and mid + 1 >= right) or (node.val == priority):
            return mid
        
        if node.val >= priority and (mid + 1 <= right and sl[mid + 1].val <= priority):
            return mid

        elif node.val > priority:
            return searchBinary(sl, mid + 1, right)
        else:
            return searchBinary(sl, left, mid - 1)

    return searchBinary(sl, 0, len(sl) - 1)

def UpdateHead(ll, node):
    old_head = ll
    old_head.prev = node
    node.next = old_head
    return node

# Transition from greater than to less than.
def FindClosestLinkedListNodeBeforeStartingFrom(ll, priority):
    prev = ll
    while ll.next != None:
        if ll.next.val <= priority:
            return ll
        prev = ll
        ll = ll.next

    return prev

def UpdateSkipListAfterIdx(sl, sl_idx):
    # 0-----------------10------------------20
    # 0-------new-------9-------------------19
    # Something was added after sl_idx and before sl_idx + 1.
    # Update all consequent pointers to point to the previous element.
    print(f'old list = {sl} i = {sl_idx}')
    for i in range(sl_idx + 1, len(sl)):
        sl[i] = sl[i].prev
    #print(f'new list = {sl}')

def MoveSkipListOneIndexForward(sl):
    sl.append(None)
    prev = sl[0]
    for i in range(1, len(sl)):
        temp = sl[i]
        sl[i] = prev
        prev = temp


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        lis = [1 for i in range(len(nums))]
        sl = []
        ll = None
        #print(nums)
        for i in range(0, len(nums)):
            #print(f'lis = {lis}')
            curr = ll
            #PrintList(ll)
            for j in range(0, i):
                index = curr.idx
                diff = nums[i] - nums[index]
                #print(f'i = {i} j = {j} nums[i] = {nums[i]} lis[j] = {curr.val} k = {k} diff = {diff}')
                if diff > 0 and diff <= k:
                    lis[i] = max(lis[i], lis[index] + 1)
                    break
                curr = curr.next

            # Insert to linked list after a binary search.
            if len(sl) == 0 or ll == None:
                # Seed the skip list with one element to begin with.
                node = ListNode(lis[i], i)
                ll = node
                sl.append(node)
            else:
                sl_idx = FindClosestSkipListNodeBefore(sl, lis[i])
                #print(f'sl_idx = {sl_idx}')
                if sl_idx == None:
                    #if ll.val < lis[i]:
                    #    print(f"Invariant violated ll.val = {ll.val} lis[{i}] = {lis[i]} skip list = {sl}")
                    # The current element is the smallest element.
                    MoveSkipListOneIndexForward(sl)
                    node = ListNode(lis[i], i)
                    sl[0] = node
                    ll = UpdateHead(ll, node)
                    #print(f'After adding to head new sl = {sl}')
                else:                    
                    sl_node = sl[sl_idx]
                    #print(f'sl_idx = {sl_idx} sl_node = ( {sl_node} ) sl ={sl}')
                    ll_node = FindClosestLinkedListNodeBeforeStartingFrom(sl_node, lis[i])
                    AddAfter(ll_node, lis[i], i)
                    #PrintList(ll)
                    UpdateSkipListAfterIdx(sl, sl_idx)

            if i != 0 and i % 512 == 0:
                # Add a new skip list element, which will be the tail of the linked list.
                if len(sl) > 0:
                    sl_node = sl[-1]
                    curr = sl_node
                    #print(f'going to append to skip list {sl}')
                    while curr != None and curr.next != None:
                        curr = curr.next
                    sl.append(curr)
                    #print(f'appended new skip list is {sl}')
            #print('\n')
        #print(lis)
        max_lis = max(x for x in lis)
        return max_lis

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2407_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        k = ast.literal_eval(f.readline())
        #print(n)
        #print(edges)
        print(x.lengthOfLIS(n, k))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')