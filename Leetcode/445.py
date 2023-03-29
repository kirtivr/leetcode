# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
class Solution(object):
    def addZeros(self,l,numZeros):
        head = l
        
        while numZeros > 0:
            lnew = ListNode(0)
            lnew.next = head
            numZeros = numZeros - 1
            head = lnew

        return head
    
    def getListLength(self, l):
        sz = 0

        while l!= None:
            sz = sz + 1
            l = l.next
        return sz

    def addLists(self, l1, l2):
        # first reverse list l1
        prev = None
        head = l1
        
        while head != None:
            head2 = head.next
            head.next = prev
            prev = head
            head = head2

        l1 = head

        # next reverse list l2
        prev = None
        head = l2
        
        while head != None:
            head2 = head.next
            head.next = prev
            prev = head
            head = head2

        l2 = head

        carry = 0
        while l1 != None:
            l1.val = carry + (l1.val + l2.val)%10
            carry = (l1.val + l2.val) - 9 if (l1.val + l2.val) > 9 else 0

        return l1

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        extra = self.getListLength(l1) - self.getListLength(l2)
        larger,smaller = l1,l2 if extra >=0 else l2,l1

        extra = abs(extra)

        # add extra zeros to the beginning of smaller

        self.addZeros(smaller, extra)

        suml = self.addLists(smaller,larger,self.getListLength(smaller))

        
        return suml 
