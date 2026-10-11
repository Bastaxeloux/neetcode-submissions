class Solution:
    def isvalid(self,line):
        seen = set()
        for e in line:
            if e != "." :
                if e in seen :
                    return False
                seen.add(e)
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board),len(board[0])
        for row in board:
            if not self.isvalid(row):
                return False
        for j in range(m):
            col = [row[j] for row in board]
            if not self.isvalid(col):
                return False
        cells = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cells[3*(i//3)+j//3].append(board[i][j])
        for cell in cells :
            if not self.isvalid(cell):
                return False
        return True
