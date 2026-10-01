class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            minprice = min(minprice,prices[i])
            diff = prices[i]-minprice
            maxprofit = max(maxprofit,diff)
        return maxprofit