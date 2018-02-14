# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''

Example:
Given 1->2->3->4->5->6->7->8->NULL,
return 1->3->5->7->2->4->6->8->NULL. 

'''

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None or head.next.next == None:
            return head

        odd = head
        even = head.next

        while odd and even and odd.next and even.next:
            print(even.val)
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even
        even.next = None
        return head
            
