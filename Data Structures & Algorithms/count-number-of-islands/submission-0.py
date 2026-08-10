class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # down, up, right, left
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # out of bounds, or already visited/water, stop
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"  # mark visited by sinking land into water

            # explore all 4 neighbors
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)  # sink entire island connected to this cell
                    islands += 1  # found one new island

        return islands