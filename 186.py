class Solution(object):
    def reverse(self, i, j, s):
        while 0 <= i < j < len(s):
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """

        if len(s) == 0:
            return s
        
        s.append(" ")
        start = 0
        for i, v in enumerate(s):
            if v == " ":
            	self.reverse(start, i - 1, s)
            	start = i + 1
        s.pop()
        self.reverse(0, len(s) - 1, s)

if __name__ == '__main__':
    inp = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(Solution().reverseWords(inp))
