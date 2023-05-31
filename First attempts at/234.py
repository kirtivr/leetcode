#!/usr/bin/env python
import time
import pdb
import sys
sys.path.append('../')
import copy
from typing import List, TypedDict, Optional
from Leetcode.python_linked_list_template import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]):
        if head == None or head.next == None:
            return head


        first = head
        prev = head
        current = head.next
        
        # New node comes to the first of the list.
        while current != None:
            temp = current.next
            prev.next = temp
            current.next = first

            first = current
            current = temp

        prev.next = None

        return first
            
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        
        ptr = head
        while ptr != None:
            temp.append(ptr.val)
            ptr = ptr.next
        #PrintList(head)
        #print()
        head = self.reverseLinkedList(head)
        #PrintList(head)
        ptr = head
        i = 0
        while ptr != None:
            if ptr.val != temp[i]:
                return False
            ptr = ptr.next
            i += 1

        return True

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    grid = [1,2,3,1]
    nodes = MakeNodes(grid)
    print(x.isPalindrome(nodes))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
