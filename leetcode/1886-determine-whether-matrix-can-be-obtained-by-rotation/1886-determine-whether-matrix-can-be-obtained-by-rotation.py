class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        k=0
        while k < 4:
            new_mat = [[0]*n for i in range(n)]
            for i in range(n):
                for j in range(n):
                    new_mat[j][n-1-i] = mat[i][j]
            if new_mat == target:
                return True
            mat = new_mat
            k+=1
        return False