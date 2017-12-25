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
                
        return new_str
        
    def isMatchRecursive(self, s, p, i, j):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        N = len(s)
        M = len(p)

        while i<N and j<M:
            t = s[i]
            v = p[j]

            if len(t) == 1 and len(v) == 1:
                if t != v and t != "." and v != ".":
                    return False
                else:
                    i += 1
                    j += 1
            else:
                if len(t) == 2 and len(v) == 1:
                    
                    ch = t[0]

                    if ch != '.' and ch != v and v != ".":
                        # dont match
                        i += 1
                    else:
                        # match or dont match
                        match = self.isMatchRecursive(s[i:],p[j+1:],0,0)
                        dontmatch = self.isMatchRecursive(s[i+1:],p[j:],0,0)

                        return match or dontmatch
                        
                elif len(v) == 2 and len(t) == 1:
                    # match or dont match
                    
                    ch = v[0]
                    if ch != '.' and ch != t and t != ".":
                        j += 1
                    else:
                        # match or dont match
                        match = self.isMatchRecursive(s[i+1:], p[j:],0,0)
                        dontmatch = self.isMatchRecursive(s[i:],p[j+1:],0,0)

                        return match or dontmatch
                elif len(v) == 2 and len(2) == 2:
                    match1 = self.isMatchRecursive(s[i+1:],p[j:],0,0)
                    match2 = self.isMatchRecursive(s[i+1:],p[j+1:],0,0)
                    match3 = self.isMatchRecursive(s[i:],p[j+1:],0,0)

                    if match1 or match2 or match3:
                        return True
                    i += 1
                    j += 1
        while i < N:
            if len(s[i]) == 2:
                i += 1
            else:
                break
        while j < M:
            if len(p[j]) == 2:
                j += 1
            else:
                break
            
        N = N - i
        M = M - j

        if N == 0 and M == 0:
            return True
        else:
            return False
        

    def isMatch(self, s, p):
        s = self.processString(s)
        p = self.processString(p)
        print(s)
        print(p)
        return self.isMatchRecursive(s,p,0,0)


if __name__ == '__main__':
#    s = "aaaaaaaaaaaaab"
 #   p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
    s = "aabcbcbcaccbcaabc"
    p = ".*a*aa*.*b*.c*.*a*"
    print(Solution().isMatch(s,p))
