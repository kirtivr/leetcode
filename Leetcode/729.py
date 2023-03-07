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

    def __repr__(self) -> str:
        return f'start: {self.start} end: {self.end}'

class MyCalendar:
    def findParentNode(self, start, end):
        # We have disjoint intervals.
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

    def updateSegment(self, current, isLeft, start, end):
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

    def __init__(self):
        self.head = None

    def book(self, start: int, end: int) -> bool:
        (current, overlaps, isLeft) = self.findParentNode(start, end)

        if overlaps:
            return False
        else:
            self.updateSegment(current, isLeft, start, end)
            return True

if __name__ == '__main__':
    x = MyCalendar()
    start = time.time()
    with open('729_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #print(edges)
        cal = MyCalendar()
        for edge in edges[1:]:
            print(cal.book(edge[0], edge[1]))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')