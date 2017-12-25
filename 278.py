# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def search(self, st, end):
        if st > end:
            return None
        
        mid = st + (end - st)/2

        if isBadVersion(mid):
            if mid > 0 and not isBadVersion(mid - 1):
                return mid
            else:
                return self.search(st, mid - 1)
        else:
            return self.search(mid + 1, end)

        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if isBadVersion(0):
            return 0


        return self.search(0, n-1)
