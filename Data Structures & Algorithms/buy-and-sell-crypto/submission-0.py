class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l = 0
       less = prices[0]
       profit = 0
       while l < len(prices):
        less = min(less,prices[l])
        profit= max(profit , prices[l]- less)
        l+=1
       return profit 