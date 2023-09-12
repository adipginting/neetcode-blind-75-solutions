class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0

        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
        return profit
