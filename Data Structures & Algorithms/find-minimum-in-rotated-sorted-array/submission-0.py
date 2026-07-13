# BINARY SEARCH
# I hear sorted, I think hmm binary searchhh
# one part is always sorted, other part
# contain rotation + minimum element
# binary seach which side is sorted, e.g.
# left side sorted minimum cannot be there
# right side sorted, minimum in left half(or midpoint)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l = 0
        r = len(nums) -1

        # binary search
        while l <= r:
            # if left <= right mean already sorted == no rotation
            # min must be num[1], compare and break
            if nums[l] < nums[r]: 
                result = min(result, nums[l])
                break

            # else find middle
            m = (l + r) // 2
            result = min(result, nums[m]) # track smallest seen
            
            # left half sorted (nums[l] to nums[m] increasing)
            # means min is NOT in left half, search right
            if nums[m] >= nums[l]:
                l = m + 1
            else: # else left half has the rotation, min is in there
                r = m - 1
        return result