class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n > 0 and n <= 3:
            return True
        elif n <= 0:
            return False
        elif n == 4:
            return False
        else:
            return True 
