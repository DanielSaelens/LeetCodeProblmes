
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    old_color = image[sr][sc]
    if old_color == color:
        return image

    def DFS(sr: int, sc: int):
        if sr < 0 or sr >= len(image):
            return
        if sc < 0 or sc >= len(image[0]):
            return
        if old_color == image[sr][sc]:
            image[sr][sc] = color
            DFS(sr + 1, sc)
            DFS(sr - 1, sc)
            DFS(sr, sc + 1)
            DFS(sr, sc - 1)
    DFS(sr, sc)

    return image


if __name__ == "__main__":
    test1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(floodFill(test1, sr, sc, color))


        

    



