class Solution:
    def coinChange(self, coins, amount):
        minCoins = {0:0}
        
        for i in range(1,amount+1):
            minCoins[i] = -1
            for currentCoin in coins:
                if i >= currentCoin and (i-currentCoin) in minCoins:
                    if minCoins[i-currentCoin] == -1:
                        continue
                    if minCoins[i] == -1 or minCoins[i-currentCoin] + 1 < minCoins[i]:
                        minCoins[i] = minCoins[i-currentCoin]+1
        
        return minCoins[amount]

print(Solution().coinChange([2,3,5],1))
print(Solution().coinChange([2,3,5],2))
print(Solution().coinChange([2,3,5],3))
print(Solution().coinChange([2,3,5],4))
print(Solution().coinChange([2,3,5],5))
print(Solution().coinChange([2,3,5],6))
print(Solution().coinChange([2,3,5],7))
print(Solution().coinChange([2,3,5],8))
print(Solution().coinChange([2,3,5],9))
print(Solution().coinChange([2,3,5],10))
print(Solution().coinChange([2,3,5],11))
print(Solution().coinChange([2,3,5],12))
print(Solution().coinChange([2,3,5],13))
                        