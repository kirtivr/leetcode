class Solution(object):
    def getXOR(self, num):
        n = 1

        while n < num:
            n = n*2

        return ~(~n + 1)
    
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        print(self.getXOR(num))
        return(num^self.getXOR(num))
        
if __name__ == '__main__':
    Solution().findComplement(5)
        
        
