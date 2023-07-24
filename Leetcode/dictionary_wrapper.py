from typing import List, Optional, Tuple, Dict

class Dictionary:
    def __init__(self, label:str = None):
        self.label = label
        self.min = float("inf")
        self.min_chars = set()
        self.max = -float("inf")
        self.max_chars = set()
        self.container = {}
    
    def __copy__(self, other):
        # Do shallow copy if possible.
        if not self.container:
            self.container = other.container.copy()
            self.min = other.min
            self.min_chars = set(other.min_chars)
            self.max = other.max
            self.max_chars = set(other.max_chars)
            self.label = other.label
            return

        for key, value in other.container.items():
            if key not in self.container:
                self.container[key] = value
            else:
                self.container[key] += value
        
        (self.min, self.min_chars) = self.findMinimum()
        (self.max, self.max_chars) = self.findMaximum()

    def findMinimum(self):
        minv = float("inf")
        minarr = set()

        for key, value in self.container.items():
            if value < minv:
                minv = value
                minarr = {key}
            elif value == minv:
                minarr.add(key)

        return (minv, minarr)
    
    def findMaximum(self):
        maxv = -float("inf")
        maxarr = set()

        for key, value in self.container.items():
            if value < maxv:
                maxv = value
                maxarr = {key}
            elif value == maxv:
                maxarr.add(key)

        return (maxv, maxarr)

    def getMinMax(self):
        return [[self.min, self.min_chars], [self.max, self.max_chars]]

    def setMinAndMaxWithUpdatedKey(self, x):
        #print(f'label = {self.label} self.min_chars = {self.min_chars}')
        # x may not be present in container, remove it from min and max.
        if x not in self.container:
            if x in self.min_chars:
                self.min_chars.remove(x)
            if x in self.max_chars:
                self.max_chars.remove(x)
            if len(self.min_chars) == 0:
                self.min = float("inf")
            if len(self.max_chars) == 0:
                self.max = -float("inf")
            return

        if self.container[x] < self.min:
            self.min = self.container[x]
            self.min_chars = set()
            self.min_chars.add(x)
        elif self.container[x] == self.min:
            self.min_chars.add(x)

        if self.container[x] > self.max:
            self.max = self.container[x]
            self.max_chars = set()
            self.max_chars.add(x)
        elif self.container[x] == self.max:
            self.max_chars.add(x)

        if self.container[x] > self.min and x in self.min_chars:
            self.min_chars.remove(x)
            if len(self.min_chars) == 0:
                (self.min, self.min_chars) = self.findMinimum()

        if self.container[x] < self.max and x in self.max_chars:
            self.max_chars.remove(x)
            if len(self.max_chars) == 0:
                (self.max, self.max_chars) = self.findMaximum()

    def add(self, key, value):
        if key not in self.container:
            self.container[key] = value
        else:
            self.container[key] += value

        self.setMinAndMaxWithUpdatedKey(key)

    def remove(self, x):
        if x not in self.container:
            return
        else:
            self.container[x] -= 1

        if self.container[x] == 0:
            del self.container[x]

        self.setMinAndMaxWithUpdatedKey(x)

    def __str__(self):
        return str(self.container)
    
    def __repr__(self):
        out = str(self.label) + ':' + str(self.container) if self.label is not None else str(self.container)
        return f'{out if self.label is not None else str(self.container)}'