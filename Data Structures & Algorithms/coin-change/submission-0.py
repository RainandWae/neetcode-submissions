class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # memo[amount] = min coins needed to make that amount

        def dfs(amount):
            # 0 amount left, no coins needed
            if amount == 0:
                return 0

            # already computed this, reuse cached result
            if amount in memo:
                return memo[amount]

            res = 1e9  # start with "impossible" placeholder (infinity)

            # try every coin, pick whichever gives fewest total coins
            for coin in coins:
                if amount - coin >= 0:  # only use coin if it doesn't overshoot
                    res = min(res, 1 + dfs(amount - coin))  # 1 (this coin) + coins needed for the rest

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        # if still infinity, no combination of coins works, return -1
        return -1 if minCoins >= 1e9 else minCoins