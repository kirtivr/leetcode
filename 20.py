class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stk = []


        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stk.append(ch)
            else:
                popped = stk.pop()

                if ch == ']':
                    if popped == '[':
                        continue
                    else:
                        return False
                elif ch == ')':
                    if popped == '(':
                        continue
                    else:
                        return False
                elif ch == '}':
                    if popped == '{':
                        continue
                    else:
                        return False

        return True
