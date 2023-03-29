# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        slowp = head
        fastp = head
        cycle = False
        while fastp != None and fastp.next != None:
            fastp = fastp.next.next
            slowp = slowp.next

            if fastp == slowp:
                cycle = True
                break
                
        while slowp != None and head != slowp:
            head = head.next
            slowp = slowp.next
        
        return head if cycle else None
