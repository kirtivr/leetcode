class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        subs = [[-1 for j in range(len(word2))] for i in range(len(word1))]
        print(subs)
        def getMinSubstrings(w1,w2,i,j):
            nonlocal subs

            print(' w1 = '+w1+' w2 = '+w2)
            print(' i= ' + str(i) + ' j= '+str(j))
            
            N = len(w1)
            M = len(w2)

            if i >= len(word1) or j >= len(word2):
                return max(N,M)
                                
            if N == 0 or M == 0:
                subs[i][j] = max(N,M)

            if N == 1 and M == 1:
                if w1 == w2:
                    subs[i][j] = 0
                else:
                    subs[i][j] = 1

            if subs[i][j] != -1:
                return subs[i][j]
            
            delw1 = 1 + getMinSubstrings(w1[1:],w2[:],i+1,j)
            addw1 = 1 + getMinSubstrings(w1[:],w2[1:],i,j+1)
            replacew1 = getMinSubstrings(w1[1:],w2[1:],i+1,j+1) + (0 if w1[0] == w2[0] else 1)

            print('del = '+str(delw1))
            print('add = '+str(addw1))
            print(' replace = '+str(replacew1))
            
            subs[i][j] = min(delw1,addw1,replacew1)
            return subs[i][j]

        return  getMinSubstrings(word1,word2,0,0)
                                                        
if __name__ == '__main__':
#    s1 = "prosperity"
#    s2 = "properties"
#    s1 = "ass"
#    s2 = 'asked'
    s1 = "a"
    s2 = "a"
    print(Solution().minDistance(s1,s2))
