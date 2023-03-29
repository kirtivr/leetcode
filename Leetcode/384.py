from random import *

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = len(nums)
        self.orig = list(nums)
        self.nums = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        used_nums = {}
        
        for i in range(self.N):
            idx = randint(0,self.N-1)
            while used_nums.get(self.orig[idx]) != None:
                    idx = randint(0,self.N-1)
                    
            used_nums[self.orig[idx]] = True
            self.nums[i],self.nums[idx] = self.nums[idx],self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)
