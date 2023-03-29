class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxSubstr = 0
        win_i = 0
        win_j = 0
        distinct = 0
        dict_ele = {}
        
        for i,c in enumerate(s):
            win_j = i
            if s[i] in dict_ele and dict_ele[s[i]] > 0:
                dict_ele[s[i]] = dict_ele[s[i]] + 1
            else:
                dict_ele[s[i]] = 1
                distinct = distinct + 1

            if distinct <= k and win_j - win_i + 1 > maxSubstr:
                print('max s[i] is '+s[i])
                maxSubstr = win_j - win_i + 1
            
            # remove left side till distinct <= k
            while distinct > k and win_j > win_i:
                ch = s[win_i]
                dict_ele[ch] = dict_ele[ch] - 1

                if (dict_ele[ch] == 0):
                   distinct = distinct - 1
                win_i = win_i + 1

  #          print(s[i]+' ' +str(distinct))
   #         print(str(dict_ele))
        return maxSubstr

if __name__ == '__main__':
    #s = 'eceba'
#    s = 'aba'
    s = 'aa'
    k = 0
    print(Solution().lengthOfLongestSubstringKDistinct(s,k))
