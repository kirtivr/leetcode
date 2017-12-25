class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        count = [[1 for j in range(n)] for i in range(m)]
        print(count)
        
        for i in range(m):
            for j in range(n):
                count[i][j] = count[i-1][j] + count[i][j-1]

        return count[m-1][n-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(3,3))
