# solver.py

def solve(puz):
    find = find_empty(puz)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(puz, i, (row, col)):
            puz[row][col] = i

            if solve(puz):
                return True

            puz[row][col] = 0

    return False


def valid(puz, num, pos):
    # Check row
    for i in range(len(puz[0])):
        if puz[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(puz)):
        if puz[i][pos[1]] == num and pos[0] != i:
            return False

    # Check boardx
    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y*3, boardx_y*3 + 3):
        for j in range(boardx_x * 3, boardx_x*3 + 3):
            if puz[i][j] == num and (i,j) != pos:
                return False

    return True


def print_boardard(puz):
    for i in range(len(puz)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(puz[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(puz[i][j])
            else:
                print(str(puz[i][j]) + " ", end="")


def find_empty(puz):
    for i in range(len(puz)):
        for j in range(len(puz[0])):
            if puz[i][j] == 0:
                return (i, j)  # row, col

    return None, None
