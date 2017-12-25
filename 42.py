import sys
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        table = {}
        dummy = 0
        N = len(height)
        maxLeft = [ 0  for i in range(N) ]
        maxRight = [ 0 for i in range(N) ]
        total = 0

        for i, ht in enumerate(height):
            if i != 0:
                maxLeft[i] = max(maxLeft[i-1],height[i-1])

        for i in range(N-1, -1, -1):
            if i != N-1:
                maxRight[i] = max(maxRight[i+1],height[i+1])
                                  
        for i, ht in enumerate(height):
            contribution = max(0, max(0, min(maxLeft[i],maxRight[i])) - ht)
            total = total + contribution
            
        return total
if __name__ == '__main__':
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(heights))
