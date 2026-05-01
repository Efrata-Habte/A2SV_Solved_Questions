class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0

        dxn = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c, dxn):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for i, j in dxn:
                dfs(r + i, c + j, dxn)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c, dxn)
        return count
