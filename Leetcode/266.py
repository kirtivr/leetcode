class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


        N = len(s)
        sd = {}

        for i in range(N):
            sd[s[i]] = 1 if s[i] not in sd else sd[s[i]] + 1 

        print(sd)

        tol =  2 if N%2 == 1 else 1
        
        for i in range(N):
            if sd[s[i]]%2 != 0:
                tol -= 1
            if tol == 0:
                return False

        return True
    
if __name__ == '__main__':
    s = "aab"
    print(Solution().canPermutePalindrome(s))
