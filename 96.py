class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        table = {0:0,1:1,2:2}
        
        def countTrees(n):
            nonlocal table
            
            if n in table:
                return table[n]
            
            count = 0
            
            for i in range(n):
                l = i
                r = n - i - 1
                print(' l = '+str(l)+' r = '+str(r))
                left = max(countTrees(l),1)
                right = max(countTrees(r),1)
                print(' left = '+str(left) + ' right = '+str(right))
                count = count + ( left * right )

            table[n] = count
            return count
        
        return countTrees(n)


if __name__ == '__main__':
    n = 4
    print(Solution().numTrees(n))
