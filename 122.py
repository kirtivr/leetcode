class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0
        
        maxProfit = 0
        grads = []
        
        for i in range(len(prices)-1):
            price = prices[i]
            prevN = prices[i+1]
            grads.append(price - prevN)

        toAdd = -1 if grads[-1] > 0 else 1
        grads.append(toAdd)
        if toAdd > 0:
            grads.append(-1)

        buyIndex = -1
        sellIndex = -1

        bought = False
        print(grads)

        i = 0
        while i < len(grads):
            grad = grads[i]
            
            if (grad > 0) and bought:
                # sell
                sellIndex = i
                maxProfit = maxProfit + prices[sellIndex] - prices[buyIndex]
                bought = False
                print('sold! at idx = '+str(i))
                    
            if (grad < 0) and not bought:
                # buy
                buyIndex = i
                print('bought! at index '+str(i))
                bought = True
            i = i + 1
            
        return maxProfit

if __name__ == '__main__':
    #l = [7, 1, 5, 3, 6, 4]
#    l = [7,6,4,3,1]
#    l = [1,2]
#    l = [2,2,5]
#    l = [1,2,4]
    print(Solution().maxProfit(l))
