# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        start = head
        ahead = head

        if head == None:
            return head
        
        temp = head
        N = 0

        while temp != None:
            temp = temp.next
            N += 1

        k = k%N
        
        for i in range(k):
            ahead = ahead.next
        
        if ahead == None:
            return head
        
        while ahead.next != None:
            ahead = ahead.next
            start = start.next

        if ahead != None:
            ahead.next = head
            head = start.next
            start.next = None
            
        return head
