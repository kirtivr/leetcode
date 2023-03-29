class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = ''
        stk = []
        
        for ch in s:
            if ch == ']':
                interior = ''
                while len(stk) > 0:
                    top = stk.pop()
                    if top == '[':
                        repeatStr = ''

                        while len(stk) > 0:
                            top = stk.pop()
                            if not ('0' <= top  <= '9' ):
                                stk.append(top)
                                break
                            repeatStr = top + repeatStr

                        repeat = int(repeatStr)
                        repeatable = interior
                        interior = ''
                        for i in range(repeat):
                            interior = interior + repeatable
                        break # out of while
                    else:
                        interior = top + interior
                stk.append(interior)
            else:
                stk.append(ch)
            #print(stk)
            
        while(len(stk) > 0):
            final = stk.pop() + final

        return final

if __name__ == '__main__':
    #s = "2[abc]3[cd]ef"
    s = "3[a2[c]]"
    print(Solution().decodeString(s))
