class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort first, needed to skip duplicates properly

        def dfs(i, cur, total):
            # hit target exactly, save this combo
            if total == target:
                res.append(cur.copy())
                return
            # overshot target, or ran out of candidates, dead end
            if total > target or i == len(candidates):
                return

            # branch 1: include candidates[i], move to next index (no reuse, unlike combinationSum)
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # skip over duplicate values, avoid picking same value twice at this position
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # branch 2: skip candidates[i] entirely, try without it
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res