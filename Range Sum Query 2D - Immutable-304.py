class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        row, col = len(self.matrix), len(self.matrix[0])
        for r in range(row):
            for c in range(col):
                if r == 0:
                    if c == 0:
                        continue
                    self.matrix[r][c] = self.matrix[r][c]+self.matrix[r][c-1]
                    # print(self.matrix[r][c-1])
                elif c==0:
                    self.matrix[r][c] = self.matrix[r][c]+self.matrix[r-1][c]
                else:
                    self.matrix[r][c] = self.matrix[r][c]+self.matrix[r][c-1]-self.matrix[r-1][c-1]+self.matrix[r-1][c]
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.matrix[row2][col2])
        print(self.matrix[row1][col1])
        print(self.matrix[row2][col1])
        print(self.matrix[row1][col2])

        return self.matrix[row2][col2]+self.matrix[row1][col1]-self.matrix[row2][col1]-self.matrix[row1][col2]

# Your NumMatrix object will be instantiated and called as such:

matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7], 
          [1, 0, 3, 0, 5]]

obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)