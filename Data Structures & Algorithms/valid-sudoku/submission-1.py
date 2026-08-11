class Solution:
    def isListValid(self,nums):
        seen = set()
        for num in nums:
            if num.isalnum():
                if num in seen :
                    return False
                else :
                    seen.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for i in range(len(board)):
            line = board[i]
            if not self.isListValid(line) :
                return False
        for j in range(len(board[0])):
            col = [line[j] for line in board]
            if not self.isListValid(col) :
                return False
        cells = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isalnum():
                    cells[i//3+3*(j//3)].append(board[i][j])
        for liste in cells :
            if not self.isListValid(liste):
                return False
        return True
            

        