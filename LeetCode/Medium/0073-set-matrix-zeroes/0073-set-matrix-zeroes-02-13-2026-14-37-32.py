class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        original_zero=[]

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    original_zero.append((i,j))
        print(original_zero)
        
        for i,j in original_zero:
            r=0
            c=0
            while r<row:
                matrix[r][j]=0
                r+=1
            while c<col:
                matrix[i][c] =0
                c+=1
        
        