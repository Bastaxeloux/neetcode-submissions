class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow = len(matrix)
        lcol = len(matrix[0])
        a,b = 0, lrow*lcol-1
        while a<=b :
            print("a=",a,"b=",b)
            mid_idx=(a+b)//2
            print("mid_idx=",mid_idx)
            row = (mid_idx//lcol)
            col = (mid_idx%lcol)
            print("row,col=",row,col)
            if matrix[row][col]<target:
                a = mid_idx+1
            elif matrix[row][col]>target:
                b = mid_idx-1
            elif matrix[row][col]==target:
                return True
        return False
