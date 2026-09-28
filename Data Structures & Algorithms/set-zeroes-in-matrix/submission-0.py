class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            matrix[i] = [0] * m
        for j in zero_cols:
            for i in range(n):
                matrix[i][j] = 0