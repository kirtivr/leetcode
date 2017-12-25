class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        table = {}

        T = len(t)
        S = len(s)
        
        for i in range(T):
            table[t[i]] = 1 if t[i] not in table else table[t[i]] + 1

        prev = None
        window = None
        oldT = dict(table)
        
        for i in range(S):
            if table.get(s[i],None):
                table[s[i]] -= 1
                if table[s[i]] == 0:
                    table.pop(s[i])
                    
                if prev == None:
                    prev = i
                print(table)

            if len(table) == 0 and (window == None or window[1] - window[0] + 1 > i+1 - prev):
                window = (prev,i+1)
                table = dict(oldT)
                table[s[i]] -= 1
                if table[s[i]] == 0:
                    table.pop(s[i])
                prev = i
                print(table)

        return s[window[0]:window[1]] if window else ""


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    S = "acbbaca"
    T = "aba"
    S = "cabefgecdaecf"
    T = "cae"
    S = "bdab"
    T = "ab"
    S = "aaflslflsldkalskaaa"
    T = "aaa"
    print(Solution().minWindow(S,T))
            
                
                
            
                 
