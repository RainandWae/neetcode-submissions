class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case, only 1 house, just rob it
        if len(nums) == 1:
            return nums[0]

        # memo[i][flag] = max money starting from house i, flag tracks if house 0 was robbed
        # (needed because houses are circular, first and last can't both be robbed)
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            # past last house, OR flag set (house 0 robbed) and reached last house, can't rob last
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            # already computed this, reuse cached result
            if memo[i][flag] != -1:
                return memo[i][flag]

            # choice: skip this house, or rob it
            # flag becomes True if we rob house 0 specifically (i == 0), stays same otherwise
            memo[i][flag] = max(dfs(i + 1, flag),
                            nums[i] + dfs(i + 2, flag or (i == 0)))
            return memo[i][flag]

        # try 2 scenarios: start at house 0 (flag=True, marks house 0 as robbed)
        # or start at house 1 (flag=False, house 0 never robbed, so last house is fair game)
        return max(dfs(0, True), dfs(1, False))