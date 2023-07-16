from typing import List, Optional, Tuple, Dict

class Dictionary:
    def __init__(self):
        self.container = {}
        self.min = float("inf")
        self.max = -float("inf")
    
    def __copy__(self, other):
        for key, value in other.container.items():
            self.addMultiple(key, value)

    def __deepcopy__(self, other):
        self.__copy__(other)

    def addMultiple(self, key, value):
        if key not in self.container:
            self.container[key] = value
        else:
            self.container[key] += value

        self.min = min(self.min, self.container[key])
        self.max = max(self.max, self.container[key])

    def add(self, x):
        if x not in self.container:
            self.container[x] = 1
        else:
            self.container[x] += 1

        self.min = min(self.min, self.container[x])
        self.max = max(self.max, self.container[x])

    def remove(self, x):
        if x not in self.container:
            return
        else:
            self.container[x] -= 1

        self.min = min(self.min, self.container[x])

    def __str__(self):
        return str(self.container)
