class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        N = len(s)
        M = len(t)
        
        diff = abs(N - M)
        
        if diff > 1:
            return False
        
        if diff == 1:
            if N > M:
                for i in range(N):
                    if s[:i] + s[i+1:] == t:
                        return True
                    
                return False
            else:
                for i in range(N):
                    if t[:i] + t[i+1:] == s:
                        return True
                        
        for i in range(N):
            if s[i] != t[i]:
                diff += 1
                
        return diff == 1
