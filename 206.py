# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr != None:
            if curr.next == None:
                head = curr

            nexte = curr.next
            curr.next = prev
            prev = curr
            curr = nexte
                
        return head
