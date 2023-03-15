#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Element(object):
    def __init__(self, key: int, val: int, prev, next):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        #print(f'get key = {key} head = {self.head} tail = {self.tail} cache = {self.cache}')
        if key in self.cache:
            el = self.cache[key]
            # Remove from DLL
            if el.prev:
                el.prev.next = el.next
                # If el was tail, el.prev is tail now
                self.tail = el.prev
            # Move element to front of the list
            old_head = self.head
            el.next = old_head
            old_head.prev = el
            self.head = el
            #print(f'done getting key = {key} head = {self.head} tail = {self.tail} cache = {self.cache}')

            return el.value
        return -1

    def put(self, key: int, value: int) -> None:
        #print(f'put key = {key} value = {value}')
        #print(f'head = {self.head} tail = {self.tail} cache = {self.cache} capacity = {self.capacity} cache size = {len(self.cache)}')
        if len(self.cache) == self.capacity and self.tail != None:
            #Evict LRU element.
            print(f'Evicting {self.tail.key}')
            del self.cache[self.tail.key]
            self.tail = self.tail.prev
            self.tail.next = None

        el = Element(key, value, None, self.head)
        if self.head is not None:
            self.head.prev = el
        self.head = el
        self.cache[key] = el
        if len(self.cache) == 1:
            self.tail = el
        
if __name__ == '__main__':
    lRUCache = LRUCache(2);
    lRUCache.put(1, 1); # cache is {1=1}
    lRUCache.put(2, 2); # cache is {1=1, 2=2}
    print(lRUCache.get(1));    # return 1
    lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2));    # returns -1 (not found)
    lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1));    # return -1 (not found)
    print(lRUCache.get(3));    # return 3
    print(lRUCache.get(4));    # return 4
#    x = Solution()
#    start = time.time()
#    print(x.minPathSum(grid))
#    end = time.time()
#    elapsed = end - start
#    print (f'time elapsed = {elapsed}')

# Adversarial input:
#  ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
