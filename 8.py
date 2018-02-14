class Solution(object):
    def myAtoi(self, inp):
        """
        :type str: str
        :rtype: int
        """

        inpl = list(inp.strip())
        inv = False
        
        out = 0

        if len(inpl) == 0 or not (inpl[0].isdigit() or inpl[0] == '+' or inpl[0] == '-'):
            return 0

        i = 0
        
        if inpl[0] == '-':
            inv = True
            i = 1
        elif inp[0] == '+':
            i = 1
            
        N = len(inpl)
        
        while i < N and inpl[i].isdigit(): 
            out = out * 10 + ord(inp[i]) - ord('0')

        return out
        
