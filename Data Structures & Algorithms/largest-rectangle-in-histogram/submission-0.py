class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair(index, height)

        for i in range(len(heights)):
            h = heights[i]
            start = i 
            # check stack not empty
            # and if top value in stack and top value heights
            # is greater than height we just reached
            # so we have to pop our stack, check max rectangle area
            # and need to extend the current height backwards
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # 'i' is current index we are at,
                # minus height we just started at 'index'
                maxArea = max(maxArea, height * (i - index))

                # since this height is greater
                # than current height we are on
                # extend our start index backward to index just pop
                start = index
            stack.append((start, h))

        # for remaining entries in stack, we compute area
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea