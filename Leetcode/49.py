class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        table = []
        N = len(strs)

        for i in range(N):
            table.append([0 for j in range(26)])

        hashtable = {}
        
        for i in range(N):
            string = strs[i]
            for ch in string:
                idx = (ord(ch)-ord('a'))
                table[i][idx] += 1

            temp = [str(x) for x in table[i]]
            strhash = ''.join(temp)
            
            if strhash in hashtable:
                hashtable[strhash].append(string)
            else:
                hashtable[strhash] = [string]

        out = []
        
        for key,value in hashtable.items():
            out.append(value)

        return out


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

