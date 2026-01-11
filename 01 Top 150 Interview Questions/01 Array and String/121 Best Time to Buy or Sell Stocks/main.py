'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104'''

'''intuition: To solve this problem, we can iterate through the list of prices while keeping track of the minimum price encountered so far. For each price, we calculate the potential profit by subtracting the minimum price from the current price. We update the maximum profit if the calculated profit is greater than the current maximum profit. This approach ensures that we only make one pass through the list, resulting in a time complexity of O(n) and a space complexity of O(1).'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -float(inf)
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
            else:
                min_price = prices[i]
        
        if max_profit > 0:
            return max_profit
        return 0
        