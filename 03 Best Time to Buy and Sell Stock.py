class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        lowest_price = prices[0]
        highest_price = None

        last_max_profit = 0
        for i in range(1,len(prices)):
            print(last_max_profit)
            if prices[i] < lowest_price:
                print("here1 ",prices[i],lowest_price,highest_price)
                if highest_price != None:
                    if highest_price - lowest_price > last_max_profit:
                        last_max_profit = highest_price - lowest_price
                lowest_price = prices[i]
                highest_price = None
                print("here2 ",prices[i],lowest_price,highest_price)
            if prices[i]>lowest_price:
                print("here3 ",prices[i],lowest_price,highest_price)
                if highest_price == None or highest_price < prices[i]:
                    highest_price = prices[i]
                print("here4 ",prices[i],lowest_price,highest_price)
        if highest_price:
            if highest_price - lowest_price > last_max_profit:
                return highest_price - lowest_price
            else:
                return last_max_profit
        return last_max_profit

solution_obj = Solution()
# print("first",solution_obj.maxProfit([7,1,5,3,6,4]))
# print("second",solution_obj.maxProfit([7,6,4,3,1]))
# print("third",solution_obj.maxProfit([2,4,1]))
print("fourth",solution_obj.maxProfit([4,11,2,7,1]))
