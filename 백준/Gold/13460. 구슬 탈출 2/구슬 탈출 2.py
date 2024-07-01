# 구슬 탈출 2

# 간만에 푸는 골드 이상 문제.
# 왜 나는 이걸 처음에 dfs로 풀 생각을 했는지 참 아쉬울 따름. 완전 탐색이며 최소 횟수임을 알았을 때 bfs를 생각해야 했음.
# 나는 공을 움직일 때 board에서 R과 B를 실제로 재할당해가며 움직임. 또한 겹침 방지를 위해 기울임 방향에 따른 좌표를 계산해야했음.
# 때문에 풀었어도 시간 효율이 말이 안 됐을 것.
# bfs로 이 문제를 푸는 데 있어서의 핵심은 deque에 넣는 요소가 각 공의 좌표와 기울임 횟수라는 것.
# 그리고 공 이동 시 이동 거리를 계산한다는 것.
# 이를 통해 공이 겹쳤을 때, 더 많이 움직인 공이 더 멀리 있던 공이므로 해당 공을 뒤로 이동시킬 수 있음.

import sys
from collections import deque
input = sys.stdin.readline

# 주어진 좌표와 방향을 따라 공을 이동.
# 벽이거나 O를 만날 떄까지 이동하며, 이동 거리를 계산해 정지 좌표와 함께 반환.
def tilt(ci, cj, di, dj):
    cnt = 0

    while board[ci + di][cj + dj] != '#' and board[ci][cj] != 'O':
        ci, cj = ci + di, cj + dj
        cnt += 1
    
    return ci, cj, cnt

def bfs():
    ri, rj = red
    bi, bj = blue

    deq = deque()
    deq.append((ri, rj, bi, bj, 1))
    visited = set()
    visited.add((ri, rj, bi, bj))

    while deq:
        ri, rj, bi, bj, moved_cnt = deq.popleft()

        # 증가하는 bfs에서 처음으로 10이 넘었다는 건 이 오른쪽의 요소들도 모두 10 이상이라는 뜻.
        if 10 < moved_cnt:
            break

        # 기울임
        for i in range(4):
            # 보드를 기울여 이동한 공의 좌표와 이동 거리를 계산.
            nri, nrj, rcnt = tilt(ri, rj, di[i], dj[i])
            nbi, nbj, bcnt = tilt(bi, bj, di[i], dj[i])

            # 파란 공이 빠져나간 경우 이미 실패이므로 continue.
            if board[nbi][nbj] == 'O':
                continue
            
            # continue 되지 않고 빨간 공이 빠져나간 경우, bfs이므로 최소 횟수를 반환.
            if board[nri][nrj] == 'O':
                return moved_cnt
        
            # 빠져나간 공이 없고, 두 공이 겹쳐있다면 더 많이 이동했던 공을 1칸 뒤로 이동.
            if nri == nbi and nrj == nbj:
                if rcnt < bcnt:
                    nbi -= di[i]
                    nbj -= dj[i]
                else:
                    nri -= di[i]
                    nrj -= dj[i]

            # 방문체크 후 deque에 추가.
            if (nri, nrj, nbi, nbj) not in visited:
                deq.append((nri, nrj, nbi, nbj, moved_cnt + 1))

    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if board[i][j] == 'R':
                red = (i, j)
            elif board[i][j] == 'B':
                blue = (i, j)
    
    di = (0, 0, -1, 1)
    dj = (-1, 1, 0, 0)

    print(bfs())