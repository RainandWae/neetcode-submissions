# Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # binary search on columns
        # top = smallest columns
        # bottom = biggest
        top = 0
        bottom = rows - 1
        while top <= bottom:
            # pick middle row
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        # loop ended without break = target not in any row
        if not (top <= bottom):
            return False

        # row binary search
        row = (top + bottom) // 2
        
        # normal binary search in row 
        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False