class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minNow = 1 << 30
        maxProfit = 0
        
        for i in range(len(prices)):
            price = prices[i]
            if price - minNow > maxProfit:
                maxProfit = price - minNow
            if price < minNow:
                minNow = price

        return maxProfit


if __name__ == '__main__':
#    l = [7, 1, 5, 3, 6, 4]
    l = [7,6,4,3,1]
    print(Solution().maxProfit(l))
