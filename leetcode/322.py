# https://leetcode.com/problems/coin-change
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = (amount + 1) * [amount + 1]
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]
