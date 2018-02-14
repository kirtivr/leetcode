class Solution:
    def computeArea(self, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        x5 = max(A,E)
        y5 = max(B,F)
        x6 = min(C,G)
        y6 = min(D,H)

        if x5 >= x6 or y5 >= y6:
            return abs(x2-x1)*abs(y2-y1) + abs(x4-x3)*abs(y4-y3)

        else:
            return abs(x2-x1)*abs(y2-y1) + abs(x4-x3)*abs(y4-y3) - abs(x6-x5)*abs(y6-y5)
        
