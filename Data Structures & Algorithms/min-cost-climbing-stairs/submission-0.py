class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)  # memo, memo[i] = min cost to reach top starting from step i

        def dfs(i):
            # past the top, no more cost to add
            if i >= len(cost):
                return 0

            # already computed this, reuse cached result
            if memo[i] != -1:
                return memo[i]

            # cost of this step + cheaper of (jump 1 step) or (jump 2 steps)
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        # can start from step 0 or step 1, pick whichever is cheaper
        return min(dfs(0), dfs(1))