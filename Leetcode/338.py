class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        def getSetBits(n):
            n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
            n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
            n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
            n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
            n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
            n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32) # This last & isn't strictly necessary.
            return n

        if num <= 4:
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num == 2:
                return 2
            if num == 3:
                return 4
            if num == 4:
                return 5
            
        ctr = 0
        dp = [0,1,1,2,1]
        start = 5

        for i in range(start,num+1):
            dp.append(0)

            if i%4 == 0 and (i&(i-1)):
                dp[i] = dp[i-4]+1
            elif i%4 == 0:
                dp[i] = 1
        
        for i in range(start,num+1):
            fourIdx = i//4 * 4
            addend = dp[fourIdx]

            if i%4 == 1:
                dp[i] = addend+1
            elif i%4 == 2:
                dp[i] = addend+1
            elif i%4 == 3:
                dp[i] = addend+2

        return dp

if __name__ == '__main__':
    print(Solution().countBits(15))
