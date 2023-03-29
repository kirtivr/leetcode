# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None:
            return True
        
        tail = head
        count = 1

        while tail.next != None:
            tail = tail.next
            count += 1
        
        m = count//2 if count%2 == 0 else count//2 + 1

        midPtr = head
        while m > 0:
            midPtr = midPtr.next
            m -= 1

        rev = midPtr
        mid = midPtr
        #print(midPtr.val)

        prev = None
        
        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        
        while head and tail:
            if head.val == tail.val:
                head = head.next
                tail = tail.next
            else:
                return False
            
        return True

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    x = head.next
    x.next = ListNode(3)
    x = x.next
    x.next = ListNode(4)
    x = x.next
    x.next = ListNode(3)
    x = x.next
    x.next = ListNode(2)
    x = x.next
    tail = ListNode(1)
    x.next = tail
    tail.next = None
    print(Solution().isPalindrome(head))
