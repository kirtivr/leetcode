# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        slowPtr = None
        fastPtr = head
        temp = None
        
        for i in range(n-1):
            fastPtr = fastPtr.next

        while fastPtr != None and fastPtr.next != None:
            fastPtr = fastPtr.next
            if slowPtr == None:
                slowPtr = head
                temp = slowPtr
            else:
                slowPtr = slowPtr.next
        
        if slowPtr != None:
            print(slowPtr.val)
            
        if slowPtr != None:
            if slowPtr.next != None:
                slowPtr.next = slowPtr.next.next
        elif head != None:
            slowPtr = head.next
            temp = slowPtr
        
        return temp
