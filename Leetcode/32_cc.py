class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = 0
        N = len(s)
        
        stk = []
        #test = False
        for k in range(N):
            ch = s[k]
            #print(stk)
            if ch == "(":
                stk.append(k)
            elif ch == ")":
                if len(stk) != 0:
                    if s[stk[-1]] == "(":
                        longest = max(longest, k - stk[-1] + 1)
                        stk.pop()
                        if len(stk) == 0:
                            longest = max(longest, k+1)
                    else:
                        stk.append(k)
                else:
                    stk.append(k)

        if len(stk) == 0:
            return N
        
        #print(stk)

        a = N
        b = 0

        while len(stk) > 0:
            b = stk.pop()
            longest = max(longest, a-b-1)
            a = b
            
        return longest

if __name__ == '__main__':
    #s ="()(())()()())((()))())((())()(())((()()()()(()()()))))))(()))()(())()(((()()(((()()()(((())))((())(()((()())())()(()(()(((())()()))())((())()(((())()()))))()(((()()))()()))(((()))(((())))())())("
    #s = "(()))(((())))"
    #s = "())"
#    s = "(()()"
    print(Solution().longestValidParentheses(s))

