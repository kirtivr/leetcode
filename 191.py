class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        
        while n > 0:
            n = n & n-1
            x += 1

        return x
