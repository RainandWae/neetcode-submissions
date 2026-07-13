class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        # current number in set
        curr = [0]
        # no. streak
        streak = 0

        # while loop until end of nums
        i = 0
        while i < len(nums):
            # curr is iterated, expecting next number
            # if fail reset streak
            # if not skip dupe, iterate 1 expecting next
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            
            # current number equal to current number in position i
            # ==> skipping duplicate number(is sorted)
            while i < len(nums) and nums[i] == curr:
                i += 1 # iterate
            
            streak += 1
            curr += 1 # add 1 to current, expecting the next number
            res = max(res, streak)
        return res