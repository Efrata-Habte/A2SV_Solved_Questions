class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows -1
        right = cols-1
        left = 0

        answer = []

        while left<=right and top<= bottom:
            
            # on top
            # left -> right
            for i in range(left,right+1):
                answer.append(matrix[top][i])
            top+=1

            # on right
            # top -> bottom
            for i in range(top,bottom+1):
                answer.append(matrix[i][right])
            right-=1

            # on bottom
            # right -> left
            if top<= bottom: # avoid double visiting
                for i in range(right,left-1,-1):
                    answer.append(matrix[bottom][i])
                bottom-=1

            # on left
            # bottom -> top
            if left <= right:
                for i in range(bottom,top-1,-1):
                    answer.append(matrix[i][left])
                left+=1

        return answer
