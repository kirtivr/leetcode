from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class IntervalNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.parent = None
        self.count = 1

    def __repr__(self) -> str:
        return f'start: {self.start} end: {self.end}'

class MyCalendarTwo:
    def findParentNode(self, start, end):
        # Based on the start time, figure out which node in the interval tree we need to
        # add the new node to.
        current = self.head
        while current != None:
            # Traverse left subtree.
            if end <= current.start:
                # We can add the node to the left tree here.
                if current.left == None:
                    return (current, False, True)
                else:
                    current = current.left
            # Traverse right subtree.
            elif start >= current.end:
                # We can add the node to the right tree here.
                if current.right == None:
                    return (current, False, False)
                else:
                    current = current.right
            else:
                return (current, True, None)

        return (None, None, None)

    def AddDisjointNode(self, current, isLeft, start, end):
        # There are a few pre-conditions we need to clarify before we write the code here
        # 1. Given an incoming range (start, end], can the range intersect with more than
        #    one node in the interval tree?
        #    Yes. First traverse the entire tree and find intersections with nodes of the tree.
        #    Then add those intersections to the tree as well.
        new_node = IntervalNode(start, end)
        if self.head == None:
            self.head = (new_node)
            return

        # Is it the left or right subtree?
        new_node.parent = current
        if isLeft:
            current.left = new_node
        else:
            current.right = new_node

        return

    def isIntersecting(self, node, start, end):
        ns = node.start
        ne = node.end

        if (start <= ns and end > ns) or (start > ns and ne > start):
            return True
        return False
            
    def intersectAndUpdateNode(self, node, start, end):
        if node == None:
            return (None, None, None)

        ns = node.start
        ne = node.end

        li = None
        ov = None
        ri = None

        # Left intersection.
        if start <= ns and end > ns:
            # Intersection starts from 'ns' and ends at the min of end and ne.
            ov = (ns, min(ne, end))
            li = (start, ns)
            ri = (min(ne, end), max(ne, end))

            node.end = ov[1]
            node.count += 1

        # Right intersection.
        elif start > ns and ne > start:
            ov = (start, min(ne, end))
            li = (ns, start)
            ri = (min(ne, end), max(ne, end))

            node.start = ov[0]
            node.end = ov[1]
            node.count += 1

        return (li, ov, ri)

    def findIntersectionsWithTree(self, start, end):
        if self.head == None:
            return (False, [])

        intersections = []
        q = [self.head]

        while len(q) > 0:
            curr = q.pop(0)
            if curr.count >= 2 and self.isIntersecting(curr, start, end):
                return (True, [])
            (left_nonoverlapping, overlapping, right_nonoverlapping) = self.intersectAndUpdateNode(curr, start, end)
            if left_nonoverlapping:
                intersections.append(left_nonoverlapping)
            if right_nonoverlapping:
                intersections.append(right_nonoverlapping)

            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

        return (False, intersections)
    
    def updateSegment(self, intersections):
        for i in intersections:
            (current, overlaps, isLeft) = self.findParentNode(i[0], i[1])
            self.AddDisjointNode(current, isLeft, i[0], i[1])

    def __init__(self):
        self.head = None

    def book(self, start: int, end: int) -> bool:
        (triple_booked, intersections) = self.findIntersectionsWithTree(start, end)

        if triple_booked:
            #print('triple booked')
            return False
        else:
            if intersections:
                #print(f'intersections = {intersections}')
                self.updateSegment(intersections)
            else:
                #print(f'adding {intersections}')
                self.updateSegment([(start, end)])
            return True

if __name__ == '__main__':
    start = time.time()
    with open('731_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #print(edges)
        cal = MyCalendarTwo()
        for edge in edges[1:]:
            print(cal.book(edge[0], edge[1]))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')