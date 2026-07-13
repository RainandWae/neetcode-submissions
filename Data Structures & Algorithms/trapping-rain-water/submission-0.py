# TWO POINTER
# mistake, thinking of calculating area of water in big chunk
# no can do, very simply we calculate water that can be present
# in an index, one at a time, at a index we look left, look right,
# find height of two pointer, left minus right, and get result and store
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        maxArea = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                maxArea += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                maxArea += rightMax - height[r]
        return maxArea