class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_price=prices[0]


        for price in prices:
            if price<min_price:
                min_price=price
            else:
                profit=price-min_price
                max_profit=max(profit,max_profit)   
        return max_profit         