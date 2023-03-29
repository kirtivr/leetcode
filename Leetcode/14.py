class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        N = len(strs)

        if N == 0:
            return 0
        
        minLen = float("inf")
        
        for i in range(N):
            minLen = min(len(strs[i]),minLen)

        pref = 0
        
        for j in range(1,minLen,1):
            t = strs[0][:j]
            isPrefix = True
            
            for i in range(1,N,1):
                s = strs[i][:j]
                if s != t:
                    isPrefix = False
                    break

            if isPrefix:
                pref = j

        return pref


if __name__ == '__main__':
    strs = ["ars","arsenal"]
    print(Solution().longestCommonPrefix(strs))
