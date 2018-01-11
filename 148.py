# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def getLength(node):
            count = 0
            x = node
            
            while x:
                count += 1
                x = x.next
            return count
        
        def sortedMerge(a,b):
            ap = a
            bp = b
            np = None
            head = None

            while ap != None and bp != None:
                if ap.val <= bp.val:
                    if np == None:
                        np = ap
                        head = np
                    else:
                        np.next = ap
                        np = np.next
                    ap = ap.next
                    
                else:
                    if np == None:
                        np = bp
                        head = np
                    else:
                        np.next = bp
                        np = np.next
                    bp = bp.next
                    
                    print('np .. '+str(np.val))
            while ap != None and np:
                np.next = ap
                np = np.next
                ap = ap.next

            while bp != None:
                np.next = bp
                np = np.next
                bp = bp.next

            return head
            
        def sort(head):
            count = getLength(head)
            if count == 0:
                return None
            elif count == 1:
                return head
            
            print(' c - '+str(count)+' head is '+str(head.val))
            
            y = head
            ast = y
            
            for i in range(count//2 - 1):
                y = y.next

            bst = y.next
            y.next = None

            temp = bst
            blen = count - count//2 - 1

            for i in range(blen):
                temp = temp.next

            temp.next = None
            
            a = sort(ast)
            b = sort(bst)
                
            if a == None and b:
                return b
            elif b == None and a:
                return a
                
            c = sortedMerge(a,b)
            return c
              
        return sort(head)

if __name__ == '__main__':
    nums = [1,5,2,4,15,10,5,20,3,2]
    head = None
    hptr = None
    
    for num in nums:
        if head == None:
            head = ListNode(num)
            hptr = head
        else:
            head.next = ListNode(num)
            head = head.next

    x = (Solution().sortList(hptr))

    while x != None:
        print(x.val)
        x = x.next
