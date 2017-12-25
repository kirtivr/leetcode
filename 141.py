# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        slowp = head
        fastp = head

        while fastp != None and fastp.next != None:
            fastp = fastp.next.next
            slowp = slowp.next

            if fastp == slowp:
                return True

        return False
            
