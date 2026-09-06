class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        # memo[i][j+1] = LIS length starting from index i, given previous picked index j
        # +1 offset lets us store j = -1 (no previous pick yet) as valid array index
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            # reached end of array, no more elements to consider
            if i == n:
                return 0

            # already computed this, reuse cached result
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            # option 1: skip nums[i], move on without using it
            LIS = dfs(i + 1, j)

            # option 2: include nums[i], only valid if no previous pick (j==-1) or nums[i] keeps it increasing
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS

        return dfs(0, -1)  # start at index 0, no previous element picked yet