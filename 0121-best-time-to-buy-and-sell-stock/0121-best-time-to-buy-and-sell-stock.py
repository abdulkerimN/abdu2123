
class Solution:
    def maxProfit(self, prices):
        minimum_price = prices[0]
        maximum_profit = 0

        for current_price in prices:
            profit = current_price - minimum_price

            if profit > maximum_profit:
                maximum_profit = profit

            if current_price < minimum_price:
                minimum_price = current_price

        return maximum_profit
