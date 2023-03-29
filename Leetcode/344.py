class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        N = len(s)
        chars =list(s)
        
        for i in range(N//2):
            chars[i],chars[N-i-1] = chars[N-i-1],chars[i]

        return (''.join(chars))

if __name__ == '__main__':
    s = 'hello'
    print(Solution().reverseString(s))
