#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return head
        first = None
        second = head

        while second != None:
            temp = second.next
            second.next = first
            first = second
            second = temp

        return first

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []

        ptr = head
        while ptr != None:
            temp.append(ptr.val)
            ptr = ptr.next

        head = self.reverseLinkedList(head)
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
    print(x.minPathSum(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
