# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bp = prices[0]
        sp = prices[0]
        profit = 0
        for i, p in enumerate(prices[1:]):
            if p < bp:
                bp = p
                sp = p
            elif p > sp:
                sp = p
                if sp - bp > profit:
                    profit = sp - bp
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    print(result)