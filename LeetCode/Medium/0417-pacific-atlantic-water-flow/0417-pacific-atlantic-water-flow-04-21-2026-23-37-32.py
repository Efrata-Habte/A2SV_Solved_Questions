class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return 

        row, col = len(heights) , len(heights[0])
        pas = set()
        atl = set()

        def dfs(r,c,visit , prev):
            if ((r,c) in visit or r<0 or c<0 or r==row or c==col or heights[r][c]<prev):
                return

            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1, visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for r in range(row):
            dfs(r,0,pas,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])

        for c in range(col):
            dfs(0,c,pas,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])

        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pas and (r,c) in atl:
                    res.append([r,c])


        return res     