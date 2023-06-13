# Definition for singly-linked list.
from python_linked_list_template import *


import heapq

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2(object):
    def __init__(self):
        self.heap = []

    def addToHeap(self, l):
        while l != None:
            heapq.heappush(self.heap,l.val)
            l = l.next
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        total = 0
        indices = []
        head = None
        
        for l in lists:
            self.addToHeap(l)

        prev = None
        while len(self.heap) > 0:
            if head == None:
                headval = heapq.heappop(self.heap)
                head = ListNode(headval)
                prev = head
            else:
                newVal = heapq.heappop(self.heap)
                newNode = ListNode(newVal)
                prev.next = newNode
                prev = newNode
        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(10)
    l2 = ListNode(3)

    l = [l1,l2]
    head = Solution().mergeKLists(l)

    while head != None:
        print(head.val)
        head = head.next
