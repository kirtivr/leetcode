# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
'''
-1
	 n: 8
	 r: 4
newh set
8
	 n: 7
	 r: -3
7
	 n: -3
-3
	 n: 4
4
	 r: -1
****
-1
	 n: 8
	 r: 4
8
	 n: 7
	 r: -3
7
	 n: -3
-3
	 n: 4
4
	 r: 8
'''
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        current = head
        prev = None
        newH = None
        
        while current != None:
            print(current.label)
            node = RandomListNode(current.label)

            if prev != None:
                prev.next = node
            else:
                newH = node

            node.random = current
            
            temp = current.next
            current.next = node

            current = temp
            prev = node
        print('****')
        
        current = newH

        while True:
            print(current.label)
            orand = current.random.random
            orig = current.random
            
            if orand == None:
                current.random = None   
            else:
                current.random = orand.next

            if current.next != None:
                onext = current.next.random
                orig.next = onext
                current = current.next
            else:
                break
            
        return newH

        
            
