class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = 999999
        ma = 0
        cp =0
        for i in range(len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            else:
                cp = prices[i] - mi
                ma = max(cp , ma)
        return ma
        



        