from typing import List, Optional, Tuple, Dict

class Dictionary:
    def __init__(self):
        self.min = float("inf")
        self.min_chars = set()
        self.max = -float("inf")
        self.max_chars = set()
        self.container = {}
    
    def __copy__(self, other):
        for key, value in other.container.items():
            self.addMultiple(key, value)
            self.setMinAndMaxWithUpdatedKey(key)

    def __deepcopy__(self, other):
        self.__copy__(other)

    def setMinAndMaxWithUpdatedKey(self, x):
        # x may not be present in container, remove it from min and max.
        if x not in self.container:
            if x in self.min_chars:
                self.min_chars.remove(x)
            if x in self.max_chars:
                self.max_chars.remove(x)
            if len(self.min_chars) == 0:
                self.min = 0
            if len(self.max_chars) == 0:
                self.max = 0
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
        if self.container[x] < self.max and x in self.max_chars:
            self.max_chars.remove(x)
        
    def addMultiple(self, key, value):
        if key not in self.container:
            self.container[key] = value
        else:
            self.container[key] += value

        self.setMinAndMaxWithUpdatedKey(key)

    def add(self, x):
        if x not in self.container:
            self.container[x] = 1
        else:
            self.container[x] += 1

        self.setMinAndMaxWithUpdatedKey(x)

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
