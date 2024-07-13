# 낚시왕

# 진짜 얼마만인지, 너무 오랜만에 오기 생겨서 몇 시간씩 붙잡고 있었던 문제.
# 다른 건 다 모범답안대로 했는데, 상어의 이동 매커니즘을 아직도 100% 이해하진 못한 것 같음.
# 핵심은 상어의 이동이 길이 * 2 - 2의 사이클 안에서 이루어진다는 것. 그러나 계산식을 짜내지 못함.
# 검색해서 고쳐쓰긴 했는데, 여전히 어려움. 이거 쓰면서 다시 보니까 조금 이해 되는 듯.

# 아 이해됬다. 0 1 2 3 2 1의 사이클을 가졌다면, 첫 번째 1은 아래방향, 마지막 1은 윗 방향 이동이 됨.
# 그래서 아래 방향 이동은 그냥 cs에 현재 위치를 더해주고, 윗 방향 이동은 cycle에서 현재 위치를 빼주는 것이었음.
# 그 다음 나온 값이 좌표 길이보다 크다면 사이클에서 뒤쪽 순번, 즉 역방향 이동(-1)이 되므로 사이클에서 다시 빼 주는 것.
# 이제야 이해가 되네. 나머지 상어 잡기와 포식은 어렵지 않았음.
import sys
input = sys.stdin.readline

def fishing(cur):
    global caught_shark

    for i in range(R):
        if water[i][cur]:
            caught_shark += water[i][cur][2]
            water[i][cur] = 0
            break


def move():
    moved = [[0] * C for _ in range(R)]
    dupliated = set()

    for i in range(R):
        for j in range(C):
            if water[i][j]:
                cs, cd, cz = water[i][j]
                di, dj = dir[cd]
                ni, nj = i, j

                if di == 1 or di == -1:
                    if di == -1:
                        ni = cs + cycle_r - i
                    else:
                        ni = cs + i

                    ni %= cycle_r

                    if R <= ni:
                        ni = cycle_r - ni
                        di = -1
                    else:
                        di = 1

                else:
                    if dj == -1:
                        nj = cs + cycle_c - j
                    else:
                        nj = cs + j

                    nj %= cycle_c

                    if C <= nj:
                        nj = cycle_c - nj
                        dj = -1
                    else:
                        dj = 1

                if not moved[ni][nj]:
                    moved[ni][nj] = (cs, rvs_dir[(di, dj)], cz)
                else:
                    if moved[ni][nj][2] < cz:
                        moved[ni][nj] = (cs, rvs_dir[(di, dj)], cz)
    
    return moved
                
if __name__ == "__main__":
    R, C, M = map(int, input().split())
    water = [[0] * C for _ in range(R)]
    dir = {1 : (-1, 0), 2 : (1, 0), 3 : (0, 1), 4 : (0, -1)}
    rvs_dir = {dir[i]: i for i in dir}
    ch_dir = {1 : 2, 2 : 1, 3 : 4, 4 : 3}

    caught_shark = 0
    cycle_r, cycle_c = R * 2 - 2, C * 2 - 2
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        water[r - 1][c - 1] = (s, d, z)
    
    for i in range(C):
        fishing(i)
        water = move()

    print(caught_shark)