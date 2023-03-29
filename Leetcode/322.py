class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        N = len(coins)
        dp = {}

        for i in range(N):
            dp[coins[i]] = 1
        
        def countCoins(current):
            nonlocal dp
            if current == 0:
                return 0
            elif current in dp:
                return dp[current]

            minC = None
            for i in range(N):
                if current - coins[i] > 0:
                    res = countCoins(current - coins[i])
                    dp[current - coins[i]] = res                    
                    if res == -1:
                        continue
                    elif minC == None:
                        minC = 1+res
                    elif 1+res < minC:
                        minC = min(minC,1+res)
                        
            if minC == None:
                dp[current] = -1
                return -1

            #print('for '+str(current)+' result is ..'+str(minC))
            
            dp[current] = minC
            #print(dp)
            return minC

        #print(dp)
        return countCoins(amount)

if __name__ == '__main__':
    c = [186,419,83,408]
    a = 6249
    c = [1, 2, 5]
    a = 11
    print(Solution().coinChange(c,a))
