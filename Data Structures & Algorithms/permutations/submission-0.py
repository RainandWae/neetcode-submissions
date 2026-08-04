class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        # pick = tracks which indices already used in current permutation
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        # perm is full length, valid permutation found, save a copy
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        # try every number at this position
        for i in range(len(nums)):
            if not pick[i]:  # only use numbers not already in current perm
                perm.append(nums[i])
                pick[i] = True

                self.backtrack(perm, nums, pick)  # recurse, fill next position

                # undo choice, try next possibility
                perm.pop()
                pick[i] = False