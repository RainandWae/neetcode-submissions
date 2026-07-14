# buy low sell high
# cant go back in time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        # set minimum buy if we must buy at first price
        minBuy = prices[0]

        for i in prices:
            # get maximum profit
            maxProf = max(maxProf, i - minBuy)
            
            # get the lowest price possible
            minBuy = min(minBuy, i)
        return maxProf