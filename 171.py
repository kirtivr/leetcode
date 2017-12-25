class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        N = len(s)
        total = 0
        multiplicand = 1
        
        for i in range(N-1, -1, -1):
            ich = ord(s[i]) - ord('@')
            total = total + multiplicand * (ich)
            multiplicand = multiplicand*26

        return total

if __name__ == '__main__':
    print(Solution().titleToNumber("ABCDE"))
