class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        table = {}
        longest = 0
        
        def divide(current, i, j):
            nonlocal longest
            print(' i = '+str(i)+' j= '+str(j))
            if i > j:
                return
            elif i == j:
                table[i,j] = False
                return
            elif j - i + 1 == 2:
                table[i,j] = (current[i] == "(" and current[j] == ")")
            else:
                mid = i + (j-i)//2
                divide(current, i, mid)
                divide(current, mid+1, j)

                if (j-i+1)%2 != 0:
                    table[i,j] = False
                    return
                
                if (i+1,j-1) in table:
                    print('op')
                
                if (i+1,j-1) in table and table[i+1,j-1] and current[i] == "(" and current[j] == ")":
                    table[i,j] = True
                else:
                    table[i,j] = isValid(current[i:j+1])

            if table[i,j]:
                longest = max(longest, j-i+1)
                
        def isValid(current):
            stk = []

            for k in range(len(current)):
                ch = current[k]
                
                if ch == "(":
                    stk.append(ch)
                elif ch == ")":
                    if len(stk) == 0 or stk.pop() != "(":
                        return False
            
            return len(stk) == 0

        divide(s,0,len(s)-1)
        print(table)
        return longest
    
'''
        N = len(s)
        
        for i in range(len(s)):
            for j in range(len(s)-1,i,-1):
                if (i - j + 1)%2 != 0:
                    continue

                curr = s[i:j+1]
#                print(" i = "+str(i)+" j = "+str(j))
#                print(curr)
                if (i,j) in table:
                    print('opt2')
                    longest = max(longest,len(curr))
                elif isValid(curr,i,j):
                    longest = max(longest,len(curr))
        #print(table)
'''

        
if __name__ == '__main__':
#    s ="()(())()()())((()))())((())()(())((()()()()(()()()))))))(()))()(())()(((()()(((()()()(((())))((())(()((()())())()(()(()(((())()()))())((())()(((())()()))))()(((()()))()()))(((()))(((())))())())("
#    s = "(()))(((())))"
    s = "())"
    print(Solution().longestValidParentheses(s))

