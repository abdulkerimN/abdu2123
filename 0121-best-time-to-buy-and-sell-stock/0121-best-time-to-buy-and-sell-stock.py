class Solution:
    def maxProfit(self, prices):
        # Initialize variables
        min_price = float('inf')  # To track the minimum price seen so far
        max_profit = 0  # To track the maximum profit
        
        # Iterate through each price in the list
        for price in prices:
            # Update the minimum price if we find a lower price
            if price < min_price:
                min_price = price
            # Calculate the potential profit if we sold at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
      