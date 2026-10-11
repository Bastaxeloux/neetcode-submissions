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
        for row in board:
            if not self.isvalid(row):
                return False
        for j in range(len(board)):
            col = [row[j] for row in board]
            if not self.isvalid(col):
                return False
        cells = [[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                cells[3*(i//3)+j//3].append(board[i][j])
        print(cells)
        for cell in cells :
            if not self.isvalid(cell):
                return False
        return True
