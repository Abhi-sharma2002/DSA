class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m =0
        mi = 99999
        cp =0

        for i in range(0,len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            else:
                cp = prices[i] - mi
                m = max(m , cp)
        return m

        