from typing import List


def numIslands(grid: List[List[str]]) -> int:
    counter = 0

    def DFS(r, c):
        if r < 0 or r >= len(grid):
            return
        if c < 0 or c >= len(grid[0]):
            return
        
        if grid[r][c] != "1":
            return
        else:
            grid[r][c] = "0"

        DFS(r + 1, c)
        DFS(r - 1, c)
        DFS(r, c + 1)
        DFS(r, c - 1)
        
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "1":
                counter += 1
                DFS(r, c)

    return counter


if __name__ == "__main__":
    grid = [["1", "1", "1", "0", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    print(numIslands(grid))