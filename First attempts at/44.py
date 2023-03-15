import pdb
import time
from functools import lru_cache

class FirstSolution:
    def nextNonAsteriskIndex(self, p: str, i: int):
        for x in range(i, len(p)):
            if p[x] != "*":
                return x
        return len(p)
    
    def charactersMatch(self, c: str, o: str) -> bool:
        if c == o or c == "?" or o == "?":
            return True
        return False

    def isMatch(self, s: str, p: str) -> bool:
        s_i = 0
        p_i = 0
        while s_i < len(s) and p_i < len(p):
            if self.charactersMatch(s[s_i], p[p_i]):
                p_i += 1
                s_i += 1
                continue
            if p[p_i] != "*":
                return False
            #pdb.set_trace()

            # If we have an asterisk, match as many characters as possible until we have
            # s[i] == character after asterisk. In that case it is optional to increment
            # p_i and start matching again.
            # If it doesn't workout, we backtrack and try the next instance of "character after asterisk"
            # in s.
            p_i = self.nextNonAsteriskIndex(p, p_i)
            # Asterisks consumed all characters.
            if p_i == len(p):
                return True
            # Find all instances of p[p_i] in s.
            # If we have a match starting from any of those instances, return True.
            instances = []
            for c_i in range(s_i, len(s)):
                if self.charactersMatch(s[c_i], p[p_i]):
                    if self.isMatch(s[c_i:], p[p_i:]):
                        return True
            break

        if s_i == len(s):
            while p_i != len(p) and p[p_i] == "*":
                p_i += 1
            if p_i == len(p):
                return True

        return False

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):  # Reach full pattern
                return i == len(s)

            if i < len(s) and (s[i] == p[j] or p[j] == '?'):  # Match Single character
                return dfs(i + 1, j + 1)
            
            if p[j] == '*':
                return dfs(i, j + 1) or i < len(s) and dfs(i + 1, j)  # Match zero or one or more character
            
            return False

        return dfs(0, 0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Note there is the extra first row and extra first column.
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        # Handle the case where s is empty
        dp[0][0] = True
        i = 1
        while i <= len(p) and p[i-1] == '*':
            dp[0][i] = True
            i += 1
        while i <= len(p):
            dp[0][i] = False
            i += 1

        # Handle the case where p is empty
        for j in range(1, len(s) + 1):
            dp[j][0] = False

        for i in range (1, len(s) + 1):
            for j in range (1, len(p) + 1):
                # If characters match AND the substrings s[:i-2], p[:j-2] match,
                # dp[i][j] is True.
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = True if dp[i-1][j-1] else False
                # If p[i-1][j-1] is asterisk, we match
                # 1. No characters from "s", so dp[i][j] = dp[i-1][j-1] if dp[i-1][j] is True.
                # 2. One character from "s", so dp[i][j] = dp[i][j-1] if dp[i][j-1] is True.
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
#        for row in dp:
#            print(str(row))
        return dp[len(s)][len(p)]
                
            
if __name__ == '__main__':
    x = FirstSolution()
    #s = "aa"
    #p = "*"
    #s = "aa"
    #p = "*x"
    #s = "adceb"
    #p = "*a*b"
    #s = "abefcdgiescdfimde"
    #p = "ab*cd?i*de"
    #s = "mississippi"
    #p = "m??*ss*?i*pi"    
    #s = "leetcode"
    #p = "*e*t?d*"
    #s = "c"
    #p = "*?*"
    s = "bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa"
    p = "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****"
    #p = "*aa*bbb*aa*a*bb*ab*bbba*a*babaab*b*aa*a*"
    #s = ""
    #p = "******"
    start = time.time()
    print(x.isMatch(s, p))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
