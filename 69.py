class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(0,x):

            if i*i == x:
                return i

            elif i*i > x:
                return i-1

            
            
