class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >=0 :
                    dp[i] = min(dp[i],1+dp[i-coin])
        print(dp)
        return dp[amount] if dp[amount] != amount+1 else -1 
                
