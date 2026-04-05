class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            for j in range(i,n-1-i):
                # save the top
                temp = matrix[i][j]

                #left-b to left-t
                matrix[i][j] = matrix[n-1-j][i]

                #right-b to left-b
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j] 

                #right-t to right-b
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]

                #left-t to right-t
                matrix[j][n-1-i] = temp
                
