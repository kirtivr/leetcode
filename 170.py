class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = []
        self.numbers = set()
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        index = hash(abs(number))%200000001
        self.numbers.add(number)
        
        if len(self.hashmap) > index:
            self.hashmap[index].append(number)
        else:
            diff = index - len(self.hashmap) + 1
            
            while diff > 0:
                self.hashmap.append([])
                diff -= 1
                
            self.hashmap[index].append(number)
            
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value == 1467164459:
            print(self.hashmap) 
            #        print(value)

        def evaluate(curr,diff,index,diff_index):
            if (curr == diff):
                egg = 0
                if len(self.hashmap[index]) >= 2:
                    for y in self.hashmap[index]:
                        if y == diff:
                            egg += 1
                if egg >= 2:
                    return True                          
            elif diff_index < len(self.hashmap) and len(self.hashmap[diff_index]) >= 1:
                
                for y in self.hashmap[diff_index]:
                    if y == diff:
                        return True 
                    
            return False
        
        for i in self.numbers:
            index = hash(abs(i))%200000001
            for curr in self.hashmap[index]:
                diff = value-curr        
                diff_index = hash(abs(diff))
                if evaluate(curr,diff,index,diff_index):
                    return True
                    
        return False
