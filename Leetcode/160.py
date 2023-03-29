# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        m = 0
        n = 0

        if headA == None or headB == None:
            return None

        ap = headA

        while ap:
            ap = ap.next
            m += 1
            
        bp = headB

        while bp:
            bp = bp.next
            n += 1


        diff = max(m,n) - min(m,n)

        if m > n:
            while diff > 0:
                headB = headB.next
        else:
            while diff > 0:
                headA = headA.next


        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
