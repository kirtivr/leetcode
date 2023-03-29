class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        P = len(p)
        S = len(s)
        tb = {}

        print(s)
        
        for i in range(P):
            if p[i] not in tb:
                tb[p[i]] = 1
            else:
                tb[p[i]] = tb[p[i]]+1

        out = []
        ctr = P
        
        for i in range(S):
            if i >= P:
                if s[i-P] in tb:
                    if tb[s[i-P]] >= 0:
                        ctr += 1
                    tb[s[i-P]] = tb[s[i-P]]+1
                        
            if s[i] in tb:
                if tb[s[i]] > 0:
                    ctr -= 1
                tb[s[i]] -= 1
                
            if ctr <= 0:
                out.append(i-P+1)

            #print('tb = '+str(tb) + ' ctr = '+str(ctr))
        return out
        
if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    s = "baa"
    p = "aa"
    print(Solution().findAnagrams(s,p))
