"""
1. Given a map of land and ocean in two-dimensional integer array
2. 1 is land, 0 is water
3. Count the number of islands. Islands are defined as a piece of land wholly surrounded by water.
"""

def count_islands(map):
    if not map:
        return 0
    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                count += 1
                dfs(map, i, j)
    return count

def dfs(map, i, j):
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]) or map[i][j] != 1:
        return
    map[i][j] = -1
    dfs(map, i + 1, j)
    dfs(map, i - 1, j)
    dfs(map, i, j + 1)
    dfs(map, i, j - 1)

map = [[1, 1, 0, 0, 0],
       [1, 1, 1, 0, 1],
       [1, 0, 1, 1, 1],
       [0, 0, 0, 0, 0]]
print(count_islands(map))

