class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            ma =0
            x = 999999
            cp =0
            for i in range(0, len(prices)):
                if prices[i] < x:
                    x = prices[i]
                else:
                    cp = prices[i] - x
                    ma = max(cp , ma)

            return ma