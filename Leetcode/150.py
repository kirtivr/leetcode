class Solution(object):
    def isOperator(self,op):
        operators = ["+","-","*","^","/"]
        
        return op in operators

    def performOp(self,op,opd1,opd2):
        if op == "+":
            return int(opd1) + int(opd2)
        elif op == "-":
            return int(opd1) - int(opd2)
        elif op == "*":
            return int(opd1) * int(opd2)
        elif op == "^":
            return int(opd1) ^ int(opd2)
        else:
            return int(opd1) / int(opd2)
        
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        N = len(tokens)

        if N == 1:
            return tokens[0]

        stk = []

        for tk in tokens:

            if not self.isOperator(tk):
                stk.append(tk)
            else:
                opd2 = stk.pop()
                opd1 = stk.pop()

                ret = self.performOp(tk, opd1, opd2)
                print(str(opd1)+str(tk)+str(opd2))
                stk.append(ret)

        ret = stk.pop()
        return ret
    
if __name__ == '__main__':
#    rpn = ["2", "1", "+", "3", "*"]
    rpn = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(rpn))
