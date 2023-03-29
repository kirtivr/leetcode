class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        S = len(s)
        T = len(t)

        sd = {}

        for i in range(S):
            sd[s[i]] = 1 if s[i] not in sd else sd[s[i]] + 1 

        for j in range(T):
            if t[j] not in sd:
                return False

            sd[j] = sd[j] - 1

        for i in range(S):
            if sd[i] != 0:
                return False

        return True
        
