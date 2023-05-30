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

    def __repr__(self):
        return f'{self.key}'

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def print_cache(self):
        curr = self.head
        while curr != None:
            print(f'{curr}', end = " ")            
            curr = curr.next
            if curr is not None:
                print('->', end = " ")
        print()
        
    def print_cache_reverse(self):
        print('reverse print')
        curr = self.tail
        while curr != None:
            print(f'{curr}', end = " ")            
            curr = curr.prev
            if curr is not None:
                print('->', end = " ")
        print()

    def get(self, key: int) -> int:
        print()
        self.print_cache()
        self.print_cache_reverse()
        print(f'get key = {key} head = {self.head} tail = {self.tail} cache = {self.cache}')
        if key in self.cache:
            el = self.cache[key]
            
            if self.head is not None and self.head.key != key:
                # el will move. So set the pointers of el's previous and next elements accordingly.
                preceding = el.prev
                if el.prev:
                    el.prev.next = el.next

                if el.next:
                    el.next.prev = el.prev

                # Move element to front of the list
                old_head = self.head
                el.prev = None
                el.next = old_head
                old_head.prev = el
                self.head = el
                #print(f'done getting key = {key} head = {self.head} tail = {self.tail} cache = {self.cache}')

                # Element is now head. If el was tail, el.prev is tail now
                if self.tail is not None and self.tail.key == el.key and preceding is not None:
                    self.tail = preceding
                    self.tail.next = None

            return el.value
        return -1

    def put(self, key: int, value: int) -> None:
        print()
        self.print_cache()
        self.print_cache_reverse()
        print(f'put key = {key} head = {self.head} tail = {self.tail} cache = {self.cache}')

        el = None
        new_tail = None
        if key not in self.cache and len(self.cache) == self.capacity and self.tail != None:
            #Evict LRU element.
            print(f'Evicting {self.tail.key}')
            del self.cache[self.tail.key]
            new_tail = self.tail.prev

        if key in self.cache:            
            el = self.cache[key]
            el.value = value
        else:
            el = Element(key, value, None, None)
            
        
        if self.head is not None and self.head.key != key:
            print(f'updating head from {self.head} to {el}')
            if key in self.cache:
                # el will move. So set the pointers of el's previous and next elements accordingly.
                preceding = el.prev
                if el.prev:
                    el.prev.next = el.next

                if el.next:
                    el.next.prev = el.prev
                    
                # Element is now head. If el was tail, el.prev is tail now
                if self.tail is not None and self.tail.key == el.key and preceding is not None:
                    new_tail = preceding

            el.next = self.head
            self.head.prev = el

        self.head = el
        self.head.prev = None
        self.cache[key] = el

        if len(self.cache) == 1:
            self.tail = el    
        elif len(self.cache) == 2:
            self.tail = el.next
        elif new_tail:
            #Remove evicted element from cache.
            self.tail = new_tail

        self.tail.next = None

if __name__ == '__main__':
    lRUCache = LRUCache(2);
    #lRUCache.put(1, 1); # cache is {1=1}
    #lRUCache.put(2, 2); # cache is {1=1, 2=2}
    #print(lRUCache.get(1));    # return 1
    #lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    #print(lRUCache.get(2));    # returns -1 (not found)
    #lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    #print(lRUCache.get(1));    # return -1 (not found)
    #print(lRUCache.get(3));    # return 3
    #print(lRUCache.get(4));    # return 4

    print(lRUCache.get(2))
    lRUCache.put(2, 1); # cache is {1=1}
    #print(lRUCache.get(1))
    lRUCache.put(1, 1); # cache is {1=1, 2=2}
    lRUCache.put(2, 3); # cache is {1=1, 2=2}
    lRUCache.put(4, 1); # cache is {1=1, 2=2}
    #print(lRUCache.get(1))
    #print(lRUCache.get(2))

    #print(lRUCache.get(1));    # return 1
    #lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    #print(lRUCache.get(2));    # returns -1 (not found)
    #lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    #print(lRUCache.get(1));    # return -1 (not found)
    #print(lRUCache.get(3));    # return 3
    #print(lRUCache.get(4));    # return 4

#    x = Solution()
#    start = time.time()
#    print(x.minPathSum(grid))
#    end = time.time()
#    elapsed = end - start
#    print (f'time elapsed = {elapsed}')
# Adversarial input:
#  ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
