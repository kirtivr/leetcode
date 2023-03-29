class Solution:
   def minWindow(self, s, t):
        need, missing = {}, len(t)
        for i in t:
            if i in need:
                need[i]+=1
            else:
                need[i]=1
        i = I = J = 0
        for j, c in enumerate(s,1):
            if c in need:
                missing-= need[c]>0
                need[c]-=1
            if not missing:
                while i<j and (s[i] not in need or need[s[i]]<0):
                    if s[i] in need:
                        need[s[i]] +=1
                    i+=1
                if not J or j-i<J-I:
                    I, J = i, j
        return s[I:J]
    
if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    S = "acbbaca"
    T = "aba"
    S = "cabefgecdaecf"
    T = "cae"
    S = "bdab"
    T = "ab"
#    S = "aaflslflsldkalskaaa"
#    T = "aaa"
    S = "ab"
    T = "a"
    print(Solution().minWindow(S,T))

