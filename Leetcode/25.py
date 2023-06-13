from python_linked_list_template import *

class Solution:
    def Length(self, head: Optional[ListNode]):
        out = 0
        while head is not None:
            out += 1
            head = head.next
        return out

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 1:
            return head

        N = self.Length(head)

        # Approach:
        #   Say size = k
        #   x -- (x -- x) -- x -- x -- x
        #   
        #   from i to i + k the pointers are reversed.
        #   i - 1 points to what was previously i + k.
        #   i + k points to what was previously i + k + 1.

        # We need to store pointers to i - 1 and i + k + 1 and make sure i - 1 points to the right element and i + k + 1 is still pointed to.
        m1_pointer = None        
        iterations = N // k
        first = None
        last = None
        hh = head

        for it in range(iterations):
            # Reverse K groups in chunks of size k.
            #print(f'iteration = {it}\n')
            
            # Move head 'steps' steps to the right
            for steps in range(k - 1, 0, -1):
                first = head
                prev = None

                # Move first from location 0 to location steps.
                for j in range(steps):
                    second = first.next
                    #print(f'\nprev pointer = {prev}')
                    #print(f'iter = {it} steps = {steps} j = {j} first = {first} second = {first.next}')
                    first.next = second.next
                    
                    second.next = first
                    #print(f'iter = {it} steps = {steps} j = {j} first = {first} first.next = {first.next} second = {second} second.next = {second.next}')
                    
                    # We always start from the head, so we are storing the new head here.
                    if j == 0:
                        head = second
                    if j == k - 2:
                        #print(f'updating last to {first}')
                        last = first

                    # Link the previous element to second (only if j >= 1).
                    if prev:
                        prev.next = second
                    prev = second

                #print(f'New head = {head} head.next = {head.next} last = {last}')                    
                #PrintList(head)
            if m1_pointer is not None:
                m1_pointer.next = second
            m1_pointer = last

            if it == 0: # Other iterations do not affect the head pointer.
                hh = head
            #PrintList(hh)

            m1_pointer = last
            head = last.next
        return hh

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('25_tc.text', 'r') as f:        
        edges = ast.literal_eval(f.readline())
        k = ast.literal_eval(f.readline())
        nodes = MakeNodes(edges)
        PrintList(nodes)
        x.reverseKGroup(nodes, k)
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')