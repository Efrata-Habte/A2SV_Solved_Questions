class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])

        transpose=[[None]*row for i in range(col)]

        for r in range(row):
            for c in range(col):
                transpose[c][r]=matrix[r][c]

        return transpose
