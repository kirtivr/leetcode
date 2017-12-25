class Solution:

    def processString(self, s):
        N = len(s)
        new_str = []
        i = 0
        
        while i < N:
            c = s[i]

            if c == "*":
                repeat = s[i-1]
                j = i+1
                while j<N and (s[j] == repeat):
                    if j+1 < N and s[j+1] == "*":
                        j += 2
                    else:
                        break
    
                new_str.pop()
                new_str.append(repeat + "*")

                if j > i+1:
                    i = j
                else:
                    i += 1                
            else:
                new_str.append(c)
                i += 1
                
        return "".join(new_str)

    def isMatchRecursive(self, s, p):
        memo = {}
        P = len(p)
        T = len(s)

        def dp(i, j):

            if (i, j) not in memo:
                if j == P:
                    ans = i == T
                else:
                    first_match = i < T and p[j] in {s[i], '.'}

                    if j+1 < P and p[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
                
            return memo[i, j]

        print(memo)
        return dp(0,0)

    def isMatch(self, s, p):
        p = self.processString(p)
        return self.isMatchRecursive(s,p)


if __name__ == '__main__':
#    s = "aaaaaaaaaaaaab"
 #   p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
#    s = "aabcbcbcaccbcaabc"
#    p = ".*a*aa*.*b*.c*.*a*"
    s = "aa"
    p = "a*"
    
    print(Solution().isMatch(s,p))
