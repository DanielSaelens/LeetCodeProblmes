def maxAreaOfIsland(grid: list[list[int]]) -> int:
    
    max_island = set()
    counter = 0

    def DFS(r, c):
        nonlocal counter
        
        if r < 0 or r >= len(grid):
            return
        if c < 0 or c >= len(grid[0]):
            return
        
        if grid[r][c] != 1:
            return
        else:
            grid[r][c] = 0

        counter += 1

        DFS(r + 1, c)
        DFS(r - 1, c)
        DFS(r, c + 1)
        DFS(r, c - 1)
    
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 1:
                counter = 0
                DFS(r, c)
                max_island.add(counter)

    max_island = max(max_island, default=0)

    return max_island


if __name__ == "__main__":
    grid = [[1, 1, 1, 0, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]
        
    print(maxAreaOfIsland(grid))