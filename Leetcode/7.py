class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        y = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
            
        while x > 0:
            last = x%10
            y = y*10 + last

        return y if not neg else return -y
