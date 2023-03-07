from typing import Optional
import pdb

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def PrintList(head: Optional[ListNode]):
    while head is not None:
        print(head.val)
        head = head.next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Lists of size one or two, they should not change.
        if head == None or head.next == None or head.next.next == None:
            return head
        
        slow_odd = head
        slow_even = head.next
        first_even = head.next

        while slow_odd is not None and slow_even is not None:
#            print(f'slow_odd = {slow_odd.val} slow_even = {slow_even.val}')
            fast_odd = slow_odd.next.next if slow_odd.next is not None else None
            fast_even = slow_even.next.next if slow_even.next is not None else None
#            print(f'fast_odd = {None if fast_odd == None else fast_odd.val} fast_even = {None if fast_even == None else fast_even.val}')

            if fast_odd is None:
                # Slow Odd -> Slow Even -> None
                # Slow Odd -> None
                slow_odd.next = first_even
                break
            if fast_even is None:
                # Slow Odd -> Slow Even -> None
                # Slow Even -> Fast Odd -> None
                if slow_even.next is not None:
                    # Fast odd is not None.
                    slow_odd.next = fast_odd
                    fast_odd.next = first_even
                    # Even still points to odd.
                    slow_even.next = None
#                    PrintList(head)
#                    PrintList(first_even)
                    break
                slow_odd.next = first_even
                break
#            print('----------------------')
#            print(f'fast_odd = {fast_odd.val} slow_odd = {slow_odd.val} fast_even = {fast_even.val} slow_even = {slow_even.val}')
#            PrintList(head)
#            print('----------------------')

            slow_odd.next = fast_odd
            slow_even.next = fast_even

            slow_odd = fast_odd
            slow_even = fast_even

        return head

                

if __name__ == '__main__':
    x = Solution()
    nodes = [ListNode(1), ListNode(2), ListNode(3)]# ListNode(4), ListNode(5)]
    head = nodes[0]
    for i in range(len(nodes) - 1, 0, -1):
        next = nodes[i]
        prev = nodes[i - 1]
        prev.next = next

    PrintList(x.oddEvenList(head))
