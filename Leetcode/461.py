class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        xored = x^y
        
        def countSetBits(x):

            count = 0

            while x!=0:
                x = x & (x-1)
                count += 1
                
            return count

        return countSetBits(xored)

if __name__ == '__main__':
    print(Solution().hammingDistance(1,4))
