class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        N = len(s)
        dp = {(i,i):True for i in range(N)}

        subs = N
        
        for i in range(N-1):
            c1 = s[i]
            c2 = s[i+1]

            if c1 == c2:
                dp[(i,i+1)] = True
                subs += 1
            else:
                dp[(i,i+1)] = False


        for i in range(3,N+1):
            for j in range(N-i+1):
                if (j,j+i-1) in dp:
                    continue
                elif dp[j+1,(i+j-2)] and s[j] == s[j+i-1]:
                    dp[(j,j+i-1)] = True
                    subs += 1
                else:
                    dp[(j,j+i-1)] = False

        #print(dp)
        return subs
if __name__ == '__main__':
    s = 'abababa'
    print(Solution().countSubstrings(s))
