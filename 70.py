class Solution(object):
    def tryClimb(self, n, steps):

        if n in steps:
            return steps[n]

        return steps[n-1]+steps[n-2]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        steps = {}
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2

        for i in range(2,n+1):
            steps[i] = self.tryClimb(i,steps)

        return steps[n]
