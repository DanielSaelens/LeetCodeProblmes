
def islandPerimeter(grid: list[list[int]]) -> int:
    counter = 0
    visited_island = 2

    def DFS(r, c):
        nonlocal counter
        if r < 0 or r >= len(grid):
            counter += 1
            return
        if c < 0 or c >= len(grid[0]):
            counter += 1
            return

        if grid[r][c] == visited_island:
            return

        if grid[r][c] == 0:
            counter += 1
            return

        else:
            grid[r][c] = visited_island

        DFS(r + 1, c)
        DFS(r - 1, c)
        DFS(r, c + 1)
        DFS(r, c - 1)

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 1:
                DFS(r, c)

    return counter


if __name__ == "__main__":
  
    test1 = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
    
    print(islandPerimeter(test1))