import sys

def input_map():
    n = int(sys.stdin.readline())
    map_ = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        map_.append(row)
    return map_

def check(n, x, y, map_):
    for i in range(n):
        for j in range(n):
            if map_[x + i][y + j] != map_[x][y]:
                return False
    return True

def solve(n, x, y, map_, white, blue):
    if check(n, x, y, map_):
        if map_[x][y] == 1:
            blue += 1
        else:
            white += 1
    else:
        n //= 2
        white, blue = solve(n, x, y, map_, white, blue)
        white, blue = solve(n, x + n, y, map_, white, blue)
        white, blue = solve(n, x, y + n, map_, white, blue)
        white, blue = solve(n, x + n, y + n, map_, white, blue)
    return white, blue

def main():
    map_ = input_map()
    white, blue = solve(len(map_), 0, 0, map_, 0, 0)
    print(white)
    print(blue)

if __name__ == "__main__":
    main()
