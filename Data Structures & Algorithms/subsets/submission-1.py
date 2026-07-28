class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []  # current subset being built

        # for each number, decide: 
        # include it or not (branches into 2 paths)
        def dfs(i):
            if i >= len(nums):
                # reached end, save a copy of 
                # current subset (copy, not reference)
                res.append(subset.copy())
                return

            # branch 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # branch 2: exclude nums[i], 
            # undo the append and try without it
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res