# 핀볼 게임

def find_warm_hole(warm_hole):
     for i in range(N):
        for j in range(N):
            if 6 <= game_board[i][j] <= 10:
                num = game_board[i][j]

                if warm_hole.get(num) == None:
                    warm_hole[num] = (i, j)
                else:
                    warm_hole[(i, j)] = warm_hole[num]
                    warm_hole[warm_hole[num]] = (i, j)


def pin_ball(si, sj, dir, dp):
    start_point = (si, sj)
    stack = [(si, sj, dir)]
    visited = []
    score = 0

    while stack:
        ci, cj, cd = stack.pop()
        ni, nj = ci + cd[0], cj + cd[1]

        if 0 <= ni < N and 0 <= nj < N:
            if (ni, nj) == start_point or game_board[ni][nj] == -1:
                break

            if game_board[ni][nj] == 0:
                stack.append((ni, nj, cd))
            
            elif 1 <= game_board[ni][nj] <= 5:
                nd = block[game_board[ni][nj]][cd]
                stack.append((ni, nj, nd))
                score += 1
            
            elif 6 <= game_board[ni][nj] <= 10:
                ni, nj = warm_hole[(ni, nj)]
                stack.append((ni, nj, cd))

        else:
            nd = (cd[0] * (-1), cd[1] * (-1))
            stack.append((ni, nj, nd))
            score += 1

    return score
        

if __name__ == "__main__":
    T = int(input())
    output = []

    for t in range(1, T + 1):
        N = int(input())
        game_board = [list(map(int, input().split())) for _ in range(N)]
        block = {
            1:{(1, 0):(0, 1), (0, 1):(0, -1), (-1, 0):(1, 0), (0, -1):(-1, 0)},
            2:{(1, 0):(-1, 0), (0, 1):(0, -1), (-1, 0):(0, 1), (0, -1):(1, 0)},
            3:{(1, 0):(-1, 0), (0, 1):(1, 0), (-1, 0):(0, -1), (0, -1):(0, 1)},
            4:{(1, 0):(0, -1), (0, 1):(-1, 0), (-1, 0):(1, 0), (0, -1):(0, 1)},
            5:{(1, 0):(-1, 0), (0, 1):(0, -1), (-1, 0):(1, 0), (0, -1):(0, 1)}
            }
        warm_hole = dict()
        find_warm_hole(warm_hole)
        dp = dict()
        ans = 0

        for i in range(N):
            for j in range(N):
                if game_board[i][j] == 0:
                    for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        ans = max(ans, pin_ball(i, j, dir, dp))

        output.append(f'#{t} {ans}')
    

    print("\n".join(output))