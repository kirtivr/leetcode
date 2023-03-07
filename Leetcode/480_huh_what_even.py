from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time
import random

class HeapElement:
    def __init__(self, idx: int, left, right, parent):
        self.idx = idx
        self.left = left
        self.right = right
        self.parent = parent
        self.in_max_heap = True

    def __str__(self) -> str:
        print(f'idx = {self.idx}')

class HeapSupportingLookup:
    def __init__(self, nums, index_lookup):
        self.head = None
        self.size = 0
        self.nums = nums
        self.index_lookup = index_lookup

    def __len__(self):
        return self.size

    def peep(self):
        return self.head

    def percolateup(self, item: HeapElement) -> HeapElement:
        # If item is larger than its parent, exchange values and
        # percolate the item up.
        if item.parent is not None and self.nums[item.idx] > self.nums[item.parent.idx]:
            idx = item.idx
            item.idx = item.parent.idx
            item.parent.idx = idx
            self.index_lookup[item.idx] = item
            self.index_lookup[item.parent.idx] = item.parent
            return self.percolateup(item.parent)
        # Item is the head.
        elif item.parent is None:
            self.head = item
            return item

    def percolatedown(self, item: HeapElement):
        if item.left is not None and self.nums[item.left.idx] > self.nums[item.idx] and (
            item.right is None or self.nums[item.left.idx] >= self.nums[item.right.idx]):
                print(f'comparing with {self.nums[item.left.idx]}')
                idx = item.idx
                item.idx = item.left.idx
                item.left.idx = idx
                self.index_lookup[item.idx] = item
                self.index_lookup[item.left.idx] = item.left
                return self.percolatedown(item.left)
        elif item.right is not None and self.nums[item.right.idx] > self.nums[item.idx]:
                print(f'comparing with {self.nums[item.right.idx]}')
                idx = item.idx
                item.idx = item.right.idx
                item.right.idx = idx
                self.index_lookup[item.idx] = item
                self.index_lookup[item.right.idx] = item.right
                return self.percolatedown(item.right)
        elif item.left is not None and item.right is not None:
            #pass
            print("float(inf) is not minimum. Unexpected!")

        # Cannot be percolated further.
        print(f'to be removed item on maxheap? {item.in_max_heap} with index {item.idx} and value {self.nums[item.idx]} has left = {item.left} right = {item.right}')
        return item

    def heappush(self, item: HeapElement):
        self.size += 1
        if self.head is None:
            self.head = item
            return

        # Add to the least spot until we reach a leaf node. Then percolate up.
        choices = [0, 1]
        curr = self.head
        #pdb.set_trace()
        while curr is not None:
            if curr.left is None:
                item.parent = curr
                curr.left = item
                break
            elif curr.right is None:
                item.parent = curr
                curr.right = item
                break
            else:
                # Choose left or right element.
                choice = random.choice(choices)
                if choice == 0:
                    curr = curr.left
                else:
                    curr = curr.right

        # We added the element to a free leaf. Now percolate up.
        self.percolateup(item)

    def removeandretainheap(self, item: HeapElement):
        self.size -= 1
        old_idx = item.idx
        old_val = self.nums[item.idx]

        self.nums[old_idx] = -float("inf")
        print(f'removing element {self.nums[item.idx]} from heap with head {self.nums[self.head.idx]}')
        item_to_remove = self.percolatedown(item)
        self.nums[old_idx] = old_val
        print(f'removing element {self.nums[item.idx]} from heap with head {self.nums[self.head.idx]}')
        if (item_to_remove.left is None and item_to_remove.right is None):
            # Leaf node. Is this the left child or the right child.
            # Is this the head?
            if item_to_remove.parent is not None:
                #print(f'leaf node with parent {self.nums[item_to_remove.parent.idx]}')
                if item_to_remove.parent.left == item_to_remove:
                    #print('here1')
                    item_to_remove.parent.left = None
                    item_to_remove.parent = None
                elif item_to_remove.parent.right == item_to_remove:
                    #print('here2')
                    item_to_remove.parent.right = None
                    item_to_remove.parent = None
            if (item_to_remove.parent is None) or (self.head is not None and self.head == item_to_remove):
                #print('setting head to None')
                self.head = None
            return item_to_remove
        else:
            # Not a leaf node. This is unexpected.
            print('Unexpected!')

    def heappop(self):
        # The new head is the larger of the two child nodes of the head.
        to_return = self.removeandretainheap(self.head)
        if self.head:
            self.head.parent = None
        return to_return

    def levelTraverse(self, node: Optional[HeapElement], level: int, traversal: List[List[int]]):
        if node is None:
            return
        #print(f'traversal = {traversal} level = {level} node = {node.val}')
        if len(traversal) < level:
            traversal.append([self.nums[node.idx]])
        else:
            traversal[level - 1].append(self.nums[node.idx])

        self.levelTraverse(node.left, level + 1, traversal)
        self.levelTraverse(node.right, level + 1, traversal)

    def levelOrder(self, root: Optional[HeapElement]) -> List[List[int]]:
        traversal = []
        self.levelTraverse(root, 1, traversal)
        return traversal

    def __str__(self) -> str:
        tr = (self.levelOrder(self.head))
        return (str(tr) if tr else '')

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        index_to_node = {idx: HeapElement(idx, None, None, None) for idx, val in enumerate(nums)}
        max_heap = HeapSupportingLookup(nums, index_to_node)
        min_heap = HeapSupportingLookup(nums, index_to_node)        
        res = []
        idx = 0
        while idx < len(nums):
            print(f'\npushing {nums[idx]}')
            node = index_to_node[idx]
            # If current idx >= k, we need to pop the earliest element
            # from one of the heaps before pushing.
            element_to_remove = None
            if idx >= k:
                # May be negative if it is in the min heap.
                element_to_remove = index_to_node[idx - k]
                if element_to_remove.in_max_heap:
                    # It is in the max heap.
                    if len(max_heap) >= 1 and nums[element_to_remove.idx] <= nums[max_heap.peep().idx]:
                       print(f'removing oldest element {nums[element_to_remove.idx]} from max heap')
                       max_heap.removeandretainheap(element_to_remove)
                    else:
                        pass
                        #print('Unexpected - element to remove not on the max heap')
                else:
                    print(f'removing oldest {-nums[element_to_remove.idx]} from min heap')
                    min_heap.removeandretainheap(element_to_remove)

            print(f'after removal max heap = {max_heap} size = {len(max_heap)}')
            print(f'min heap = {min_heap} size = {len(min_heap)}')

            if len(max_heap) == 0 and len(min_heap) == 0:
                max_heap.heappush(node)
            # Insert where it fits.
            elif len(max_heap) > 0 and nums[max_heap.peep().idx] >= nums[node.idx]:
                node.in_max_heap = True
                max_heap.heappush(node)
            else:
                node.in_max_heap = False
                nums[node.idx] = -nums[node.idx]
                min_heap.heappush(node)

            # Rebalance.
            odd = (len(max_heap) + len(min_heap)) % 2 != 0
            if (not odd and len(max_heap) != len(min_heap)) or (odd and abs(len(max_heap) - len(min_heap)) > 1):
              if len(max_heap) > len(min_heap):
                #print('popping max heap')
                popped = max_heap.heappop()
                popped.in_max_heap = False
                nums[popped.idx] = -nums[popped.idx]
                min_heap.heappush(popped)
              else:
                #print('popping min heap')
                popped = min_heap.heappop()
                # NEGATE values to get the real value from the minheap.
                nums[popped.idx] = -nums[popped.idx]
                popped.in_max_heap = True
                max_heap.heappush(popped)
            if idx >= k - 1:
                if not odd and k == 1:
                    if len(max_heap) >= 0:
                        res.append(nums[max_heap.peep().idx])
                    else:
                        res.append(nums[min_heap.peep().idx])
                elif not odd:
                    mh = nums[max_heap.peep().idx]
                    mnh = -nums[min_heap.peep().idx]
                    res.append((mh + mnh) / 2)
                else:
                    if len(max_heap) > len(min_heap):
                        mh = nums[max_heap.peep().idx]
                        #print(f'appending {mh}')
                        res.append(mh)
                    else:
                        mnh = -nums[min_heap.peep().idx]
                        #print(f'appending {mnh}')
                        res.append(mnh)
            idx += 1
            print(f'\n after adding abd rebalancing max heap = {max_heap} size = {len(max_heap)}')
            print(f'min heap = {min_heap} size = {len(min_heap)}')
        return res

    def medianSlidingWindow2(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        out = []
        idx = 0

        while idx < len(nums):
            if idx == 0:
                # Initially add to max heap.
                max_heap.append(nums[idx])
            else:
                # A new element has come in, figure out which 
                pass

            if len(max_heap) + len(min_heap) == k:
                # We are ready for an output.
                mxh_o = max_heap[0]
                mnh_o = min_heap[0]
                if len(max_heap) == len(min_heap):
                    out.append((mxh_o + mnh_o) //2)
                # Pop an element from the larger heap.
                elif len(max_heap) > len(min_heap):
                    out.append(mxh_o)
                else:
                    out.append(mnh_o)

if __name__ == '__main__':
    s = Solution()
    start = time.time()
    with open('480_tc.text', 'r') as f:
        arr = ast.literal_eval(f.readline())
        #print(n)
        k = ast.literal_eval(f.readline())
        #print(edges)
        print(s.medianSlidingWindow(arr, k))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')