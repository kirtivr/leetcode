class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        N = len(haystack)
        M = len(needle)


        for i in range(N):

            for j in range(M):
                if needle[j] != haystack[i+j]:
                    break
                if j == M:
                    return i

        return -1
