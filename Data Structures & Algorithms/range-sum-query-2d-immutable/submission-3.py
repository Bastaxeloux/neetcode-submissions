class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i != 0 and j !=0:
                    # print(f"i={i} and j={j}")
                    matrix[n-1-i][m-1-j] += matrix[n-1-i][m-j] + matrix[n-i][m-1-j] - matrix[n-i][m-j]
                elif j !=0 and i == 0:
                    matrix[n-1-i][m-1-j] += matrix[n-1-i][m-j]
                elif j == 0 and i != 0 :
                    matrix[n-1-i][m-1-j] += matrix[n-i][m-1-j]
        self.matrix = matrix
        print(matrix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows,cols = len(self.matrix), len(self.matrix[0])
        total = self.matrix[row1][col1]
        if row2 + 1 < rows:
            total -= self.matrix[row2 + 1][col1]
        if col2 + 1 < cols:
            total -= self.matrix[row1][col2 + 1]
        if row2 + 1 < rows and col2 + 1 < cols:
            total += self.matrix[row2 + 1][col2 + 1]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)