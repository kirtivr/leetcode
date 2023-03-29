# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splice(self, l1, l2):
        head = l2
        tail = None
        while l2 != None and l1 != None and l1.val >= l2.val:
            l2 = l2.next
        tail = l2
        return (head,tail)
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        l1ptr = None
        l2ptr = None
        head = None
        prev = None 

        if l1.val <= l2.val:
            head = l1
            l1ptr = l1
            l2ptr = l2
        else:
            head = l2
            l1ptr = l2
            l2ptr = l1

        prev = None
        
        while l1ptr != None and l2ptr != None:
            temp = None

            if l1ptr.val >= l2ptr.val:
                sphead,sptail = self.splice(l1ptr,l2ptr)

                if prev == None:
                    nextPtr = l1ptr.next
                    prev = l1ptr
                    while sphead != sptail:
                        prev.next = sphead
                        prev = prev.next
                        sphead = sphead.next

                    prev.next = nextPtr
                    l1ptr = nextPtr
                    l2ptr = sptail  
                else:
                    while sphead != sptail:
                        prev.next = sphead
                        prev = prev.next
                        sphead = sphead.next
                
                    prev.next = l1ptr
                    prev = prev.next
                    l1ptr = l1ptr.next
                    l2ptr = sptail
                
            elif l1ptr.val < l2ptr.val:
                prev = l1ptr
                l1ptr = l1ptr.next

        while l1ptr != None:
            prev.next = l1ptr
            prev = prev.next
            l1ptr = l1ptr.next

        while l2ptr != None:
            prev.next = l2ptr
            prev = prev.next
            l2ptr = l2ptr.next

        return head
