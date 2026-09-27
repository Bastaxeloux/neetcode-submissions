class Solution:
    def isValidLine(self,line):
        seen = set()
        for e in line :
            if e.isalnum():
                if e in seen :
                    return False
                seen.add(e)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every line and column
        for l in board :
            if not self.isValidLine(l):
                return False
        for j in range(len(board[0])):
            col = [line[j] for line in board]
            if not self.isValidLine(col) :
                return False
        cells = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isalnum():
                    cells[i//3+3*(j//3)].append(board[i][j])
        for liste in cells :
            if not self.isValidLine(liste):
                return False
        return True
        