class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # hit target exactly, save this combo
            if total == target:
                res.append(cur.copy())
                return
            # ran out of nums, or overshot target, dead end
            if i >= len(nums) or total > target:
                return

            # branch 1: include nums[i] again (can reuse same number, stay at index i)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # branch 2: skip nums[i] entirely, move to next number
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res