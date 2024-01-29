# 스도쿠 검증

T = int(input())

for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        column = []
        for j in range(9):
            if sudoku[i].count(j+1) != 1:
                ans = 0

            if i % 3 == 0 and j % 3 == 0:
                box = []
                for k in range(3):
                    for r in range(3):
                        box.append(sudoku[i+k][j+r])
                for x in range(1, 10):
                    if box.count(x) != 1:
                        ans = 0

            column.append(sudoku[j][i])

        for x in range(1, 10):
            if column.count(x) != 1:
                ans = 0

    print(f"#{t} {ans}")