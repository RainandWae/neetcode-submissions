# BINARY SEARCH
# rotated array, no raw dog binary search 
# 1st, find pivot (index of smallest elem = where rotation happens)
# and then normal binary search on correct half (before or after pivot)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 
        
        # find pivot point, use l < r (not <=) 
        # since we want l and r to converge to same index
        while l < r:
            m = (l + r) // 2
            
            # if mid bigger than right, pivot is after mid
            if nums[m] > nums[r]: 
                l = m + 1
            else: # mid <= right, pivot is at mid or before
                r = m
        
        # l == r here, this is index of smallest elem
        pivot = l 

        # normal binary search, reused twice so make it a helper func
        def binary_search(left: int, right: int) -> int:
            while left <= right: 
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # search left half first (before pivot)
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        # not found, search right half (pivot onwards)
        return binary_search(pivot, len(nums) - 1)