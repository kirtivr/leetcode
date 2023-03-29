class Solution:

    def processString(self, s):
        N = len(s)
        new_str = []
        i = 0
        
        while i < N:
            c = s[i]

            if c == "*":
                j = i+1
                while j<N and (s[j] == c):
                    j += 1
                
                new_str.append("*")

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
                elif j < P and i < T:
                    first_match = p[j] in {s[i], '?'}

                    if p[j] == '*':
                        ans = dp(i, j+1) or dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                else:
                    if i == T and P - j == 1:
                        ans = p[j] == "*"
                    else:
                        ans = False
                memo[i, j] = ans
                
            return memo[i, j]

        print(memo)
        return dp(0,0)

    def isMatch(self, s, p):
        p = self.processString(p)
        print(p)
        return self.isMatchRecursive(s,p)


if __name__ == '__main__':
#    s = "aaaaaaaaaaaaab"
 #   p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
#    s = "aabcbcbcaccbcaabc"
#    p = ".*a*aa*.*b*.c*.*a*"
    s = "aa"
    p = "a*"
    #s = "aa"
    #p = "*"
#    s = "zacabz"
#    p = "*a?b*"
    print(Solution().isMatch(s,p))
