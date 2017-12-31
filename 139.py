class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        N = len(s)
        ok = [False for i in range(N)]
        dp = {}
        
        def testBreak(bs,start):
            nonlocal N,ok
            #print(' incoming '+bs)
            if (start,N) in dp:
#                print('clash')
                return False
            
            for i in range(start,N,1):
                subs = s[start:i+1]
                #print(subs)
                if subs in wordDict:
                    ok[i] = True

            for i in range(start,N,1):
                if ok[i]:
                    # check if remaining is in dictionary
                    if s[i+1:] in wordDict:
                        return True
                    elif testBreak(s[i+1:],i+1):
                        return True

            dp[(start,N)] = True
            
            if ok[N-1]:
                return True
            return False
        
        return testBreak(s,0)


if __name__ == '__main__':
#    word = "aaaaaaa"
#    wdic =["aaaa","aaa"]
#     ["leet","code"]
    w = "leetcode"
    d = ["leet","code"]
    w = "abcd"
    d = ["a","abc","b","cd"]
    w = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(Solution().wordBreak(w,d))
