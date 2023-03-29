class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        M = len(word1)
        N = len(word2)
        
        subs = [[0 for j in range(N+1)] for i in range(M+1)]

        for i in range(M+1):
            subs[i][0] = i
            
        for j in range(N+1):
            subs[0][j] = j

        for i in range(1,M+1):
            for j in range(1,N+1):
                
                if word1[i-1] == word2[j-1]:
                    subs[i][j] = subs[i-1][j-1]
                else:
                    subs[i][j] = min(1+subs[i-1][j],1+subs[i][j-1],1+subs[i-1][j-1])
        return subs[M][N]
    
if __name__ == '__main__':
    s1 = "prosperity"
    s2 = "properties"
#    s1 = "ass"
#    s2 = 'asked'
    #s1 = "a"
    #s2 = "a"
    print(Solution().minDistance(s1,s2))
