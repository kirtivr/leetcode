class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n = n * 2
        if n == 0:
            return []

        parens = []
        
        def isValid(current):

            stk = []

            for ch in current:
                if ch == "(":
                    stk.append(ch)
                elif ch == ")":
                    if len(stk) == 0 or stk.pop() != "(":
                        return False
            
            return True if len(stk) == 0 else False

        def gen(num,curr):
#            print(num)
#            print(curr)
            if num == 0:
 #               print(curr)
                if isValid(curr):
                    parens.append(curr)
                return
            gen(num-1,curr + ")")
            gen(num-1,curr + "(")

        gen(n,"")
        return parens


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
        
