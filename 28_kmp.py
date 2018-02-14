class Solution:
    def partial(self, needle):
        ret = [0]

        for i in range(1,len(needle)):
            j = ret[i-1]
            while j > 0 and needle[j] != needle[i]:
                j = ret[j-1]
            ret.append(j + 1 if needle[j] == needle[i] else j)

        return ret
        
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        partial, ret, j = self.partial(needle), [], 0

        for i in range(len(haystack)):
            
        
