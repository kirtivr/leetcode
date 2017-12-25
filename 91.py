class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        
        n = len(s)

        numW = [0 for i in range(n + 1)]
        numW[n] = 1
        numW[n-1] = 0 if s[n-1] == '0' else 1

        for i in range(n-2,-1,-1):
            if s[i] == '0':
                continue

            numW[i] = numW[i+1] + numW[i+2] if int(s[i:i+2]) <= 26 else num[i+1]
#        print(numW)
        return numW[0]
        

if __name__ == "__main__":
    #s = "1237612"
    s = "12120"
    print(Solution().numDecodings(s))
