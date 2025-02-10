#
# def islandPerimeter(grid):
#     visit = set()
#     row = len(grid)
#     col = len(grid[0])
#     count = 0
#     def dfs(i,j):
#         if i >= row or i< 0 or j >= col or j<0 or grid[i][j] == 0:
#             return 1
#         if (i,j) in visit:
#             return 0
#         visit.add((i,j))
#         count = dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
#         return count
#     for i in range(row):
#         for j in range(col):
#             if grid[i][j] == 1:
#                 count = dfs(i,j)
#                 return count

'''
time : O(n*m)
space: O(n*m)
'''

def islandPerimeter(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += (1 if (i+1 >= len(grid) or grid[i+1][j] == 0) else 0)
                res += (1 if (i-1 < 0 or grid[i - 1][j] == 0) else 0)
                res += (1 if (j + 1 >= len(grid) or grid[i][j+1] == 0) else 0)
                res += (1 if (j - 1 < 0 or grid[i][j-1] == 0) else 0)
    return res

'''
time: O(n*m)
space: O(1)
'''