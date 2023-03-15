from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class IntervalNode:
    def __init__(self, start, end, count=1):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.parent = None
        self.count = count

    def __repr__(self) -> str:
        out = ''
        if self.end < 50:
            out = f'start: {self.start} end: {self.end} count: {self.count}'
        return out

def PrintTree(root: Optional[IntervalNode]):
    if root == None:
        print("", end = "")
        return

    print(f'(({root})', end = " ")

    PrintTree(root.left)
    PrintTree(root.right)
    print(f')', end = " ")


'''
Philosophy: Lay down markers every time a range starts. Remove the marker when the range ends.
Iterate through the map (up to 1000 entries) to find any range with equal to 3 markers.
Remove the just added range.
C++ ordered map allows this to be done easily.

class SimpleSolution:
  
    map<int, int> mp;
    
    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        
        // increment the value of start 
        
        mp[start]++;
        
        // decrement the value of end
        
        mp[end]--;
        
        // traverse over map, if at any any moment we get count > 2, then we have found a triple booking
        
        int count = 0;
        
        for(auto x : mp)
        {
            count += x.second;
            
            if(count > 2)
                break;
        }
        
        // remove the inserted interval from map
        
        if(count > 2)
        {
            mp[start]--;
            
            mp[end]++;
            
            return false;
        }
        
        return true;
    }
'''

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

    def AddDisjointNode(self, current, isLeft, new_node):
        # There are a few pre-conditions we need to clarify before we write the code here
        # 1. Given an incoming range (start, end], can the range intersect with more than
        #    one node in the interval tree?
        #    Yes. First traverse the entire tree and find intersections with nodes of the tree.
        #    Then add those intersections to the tree as well.
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

        # Left intersection. Note we are ignoring the outlying parts of the incoming element.
        if start <= ns and end > ns:
            # Intersection starts from 'ns' and ends at the min of end and ne.
            ov = (ns, min(ne, end))
            li = None
            if ne > end:
                ri = (end, ne, node.count) # Belongs to node.

            if ri and ri[0] == ri[1]:
                ri = None
            #print(f'node {node} (start, end) = {(start, end)}changed to have end {ov[1]}')
            if ov[0] == ov[1]:
                ov = None
            node.end = ov[1]
            node.count += 1

        # Right intersection.
        elif start > ns and ne > start:
            ov = (start, min(ne, end))
            li = (ns, start, node.count) # Belongs to node
            if ne > end:
                ri = (end, ne, node.count) # Belongs to node.

            if li[0] == li[1]:
                li = None
            if ri and ri[0] == ri[1]:
                ri = None
            if ov[0] == ov[1]:
                ov = None
            #print(f'node {node} changed to have start {ov[0]} and end {ov[1]}')
            node.start = ov[0]
            node.end = ov[1]
            node.count += 1


        return (li, ov, ri)

    def subtractOverlappingsFromRangeAndAddToIntersections(self, start, end, overlappings, intersections):
        overlappings.sort()
        #print(f'incoming intersections = {intersections}')
        st = start
        idx = 0
        while st < end and idx < len(overlappings):
            if st < overlappings[idx][0]:
                # We have a range.
                intersections.append((st, overlappings[idx][0], 1))
            st = overlappings[idx][1]
            idx += 1

        if st < end:
            intersections.append((st, end, 1))
        #print(f'outgoing intersections = {intersections}')

    def findIntersectionsWithTree(self, start, end):
        #print(f'input start = {start} end = {end}')
        if self.head == None:
            return ([], False)
        
        q = [self.head]
        intersections = []
        overlappings = []
        while len(q) > 0:
            curr = q.pop(0)
            (left_nonoverlapping, overlapping, right_nonoverlapping) = self.intersectAndUpdateNode(curr, start, end)
            if left_nonoverlapping:
                    #print(f'left non overlapping = {left_nonoverlapping}')
                    intersections.append(left_nonoverlapping)

            if right_nonoverlapping:
                #print(f'right non overlapping = {right_nonoverlapping}')
                intersections.append(right_nonoverlapping)

            if overlapping:
                overlappings.append(overlapping)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

        #PrintTree(self.head)
        self.subtractOverlappingsFromRangeAndAddToIntersections(start, end, overlappings, intersections)

        return (intersections, True if overlappings else False)
    
    def updateSegment(self, intersections):
        #print(intersections)
        for i in intersections:
            #print()
            #print(f'adding node {i}')
            (current, overlaps, isLeft) = self.findParentNode(i[0], i[1])
            #print(f'parent node is {current} isLeft = {isLeft}')
            self.AddDisjointNode(current, isLeft, IntervalNode(i[0], i[1], i[2]))

    def __init__(self):
        self.head = None

    def book(self, start: int, end: int) -> bool:
        (intersections, overlapped) = self.findIntersectionsWithTree(start, end)

        if intersections:
            #print(f'intersections = {intersections}')
            self.updateSegment(intersections)
        elif not overlapped:
            #print(f'adding {intersections}')
            self.updateSegment([(start, end, 1)])

        q = [self.head]
        out = 0
        while len(q) > 0:
            curr = q.pop(0)
            out = max(out, curr.count)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

        return out

if __name__ == '__main__':
    start = time.time()
    #expected = [None,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]
    expected = [None,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,False]
    expected = [None, 1, 1, 2, 3, 3, 3]
    expected = [None,1,1,1,2,2,3,3,3,3,3,3,4,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,8,9,9,9,9,9,10]
    with open('732_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #edges = edges[:18]
        #print(edges)
        cal = MyCalendarTwo()
        idx = 1
        count = 0
        print(f'size of test cases = {len(edges)}')
        fn = IntervalNode(18, 35)
        for edge in edges[1:]:
            res = cal.book(edge[0], edge[1])
            if cal.isIntersecting(fn, edge[0], edge[1]):
                count += 1
                #print(f'{edge} count = {count}')
            if edge[0] == 6 and edge[1] == 23:
                break
            if res != expected[idx]:
                print(f'failed test case number {idx} {edge} expected: {expected[idx]} answer: {res}')
            idx += 1
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')