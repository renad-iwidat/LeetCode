class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #initially set to infinity, any stock price will be lower
        lowest_price_so_far = float('inf')

         # start with zero profit
        best_profit = 0                    
        
        # Iterate through each stock price
        for current_price in prices:
            # Update the lowest price 
            if current_price < lowest_price_so_far:
                lowest_price_so_far = current_price
            # Calculate the potential profit 
            potential_profit = current_price - lowest_price_so_far
            
            if potential_profit > best_profit:
                best_profit = potential_profit
                
        return best_profit