class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        dxn = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!="O":
                return

            board[r][c] = "C"            

            for i,j in dxn:
                dfs(r+i,c+j)

        for r in range(row):
            for c in range(col):
                if (r in [0,row-1] or c in [0,col-1]) and board[r][c] == "O":
                    dfs(r,c)


        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c]="X"

        for r in range(row):
            for c in range(col):
                if board[r][c] == "C":
                    board[r][c]="O"
        