class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        spiral = []
        while top <= bottom and left <= right:
            top_left, top_right, bottom_right, bottom_left = [], [], [], []
            for j in range(left, right + 1):
                top_left.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                top_right.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    bottom_right.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    bottom_left.append(matrix[i][left])
                left += 1
            spiral += top_left
            spiral += top_right
            spiral += bottom_right
            spiral += bottom_left
        return spiral