
def searchMatrix(matrix, target: int) -> bool:
    row, col = len(matrix)-1, 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            col += 1
        else:
            row -= 1
    return False

print(searchMatrix([
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
], 3))


