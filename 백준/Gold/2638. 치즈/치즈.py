# 치즈

# 쉽지 않았던 문제. 전에 풀었던 플레 5 백조의 호수 같은 느낌이었음. 물론 골드 3이니 그보단 쉬웠겠지만.
# 그렇게 어렵게 느낀 이유는 잘못된 접근으로 백조의 호수를 떠올리며 문제를 풀었기 때문.
# 문제를 읽고 나는 먼저 내부 공기가 아닌 외부공기를 bfs로 먼저 찾고, 그 다음 치즈를 찾아 탐색함.
# 치즈 주변이 공기일 때, 외부 공기의 원소이면 그 수를 세고 2 이상인 것들을 공기로 바꿈.
# 다만 그렇게 하지 공기 찾을 때 bfs하나, 치즈 찾을 때 또 하나가 들어가니 답은 나왔지만 시간초과.

# 거의 2시간쯤 끙끙대다가 검색해서 들어간 글의 서두에 '공기를 기준으로 치즈를 탐색' 이라는 얘기가 있어서 충격.
# 결국 해법은 공기를 기준으로 치즈를 만나면 카운트를 + 1씩 하고, bfs이후 치즈들을 공기로 바꾸고 시간을 더하는 것.
import sys
from collections import deque
input = sys.stdin.readline

def bfs(cheese):
    deq = deque()
    deq.append((0, 0))
    air = set()         # 외부 공기.
    air.add((0, 0)) 
    melting_cheese = [[0] * M for _ in range(N)]
    melted = set()      # 공기 접촉면이 2개 이상인 치즈의 좌표.
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while deq:
        ci, cj = deq.popleft()

        for di, dj in dir:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in air:
                # 공기라면 deq에 추가.
                if cheese[ni][nj] == '0':
                    deq.append((ni, nj))
                    air.add((ni, nj))
                # 치즈라면 melting_cheese의 해당 좌표에 + 1.
                # 2 이상이면 melted에 추가.
                else:
                    if (ni, nj) not in melted:
                        melting_cheese[ni][nj] += 1
                        if 2 <= melting_cheese[ni][nj]:
                            melted.add((ni, nj))

    # 이번 턴에 녹은 치즈와 공기 의 합이 전체 칸 수 N * M 이면 이번에 모든 치즈가 녹은 것이므로 종료 신호 반환.
    if len(melted) + len(air) == N * M:
        return False
    else:
        for i, j in melted:
            cheese[i][j] = '0'
        return True


if __name__ == "__main__":
    N, M = map(int, input().split())
    cheese = [input().split() for _ in range(N)]
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
    ans = 0

    # bfs의 리턴값인 공기의 수가 전체 칸 수가 될 때 반복 종료.
    while True:
        if bfs(cheese):
            ans += 1
        else:
            ans += 1
            break
        
    print(ans)