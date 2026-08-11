class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n  # memo, cache[i] = number of ways to reach top from step i

        def dfs(i):
            # reached exactly n, valid path, count as 1 way
            # overshot n, invalid path, count as 0
            if i >= n:
                return i == n

            # already computed this, reuse cached result
            if cache[i] != -1:
                return cache[i]

            # ways from i = ways from taking 1 step + ways from taking 2 steps
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)