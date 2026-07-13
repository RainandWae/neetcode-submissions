# Two Pointer
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 # left pointer
        r = len(heights) - 1 # right pointer
        result = 0

        while l < r: # make sure two pointer doesnt point on the same value
            # min for getting shorter wall so water doenst rise above it
            # r - l for width of two pointer, getting area
            area = min(heights[l], heights[r]) * (r - l)
            # get maximum amount of water container can store
            result = max(result, area)

            # start moving pointer, but move pointer that are smaller value
            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1
        return result