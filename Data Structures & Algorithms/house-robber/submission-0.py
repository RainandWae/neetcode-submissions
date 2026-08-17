class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)  # memo, memo[i] = max money robbable starting from house i

        def dfs(i):
            # past last house, nothing left to rob
            if i >= len(nums):
                return 0

            # already computed this, reuse cached result
            if memo[i] != -1:
                return memo[i]

            # choice: skip this house (go to i+1), or rob it (take nums[i], skip next house, go to i+2)
            # since adjacent houses can't both be robbed
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)