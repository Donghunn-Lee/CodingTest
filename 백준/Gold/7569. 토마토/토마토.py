# 토마토

# 비록 5티어지만, 내가 처음으로 골드에서 1트에 '맞았습니다!!' 를 띄운 역사적인 첫 번째 문제.
# 이렇게 지났는 줄은 몰랐는데 시간은 1시간 가까이 걸린 것 같음.
# 전에 하루 걸려 답 보고 풀었던 백조의 호수가 생각나는 문제. 그걸 풀어보지 않았다면 이 문제 역시 반나절은 썼을지도.
# 그래도 확실히 골드수준의 문제였다고 생각함. 최소 일수를 구하는 전형적인 bfs문제.
# 평소 써 오던 bfs 포멧에서 2차원을 3차원으로만 바꾸면 크게 어려움 없었음.

import sys
from collections import deque
input = sys.stdin.readline

def bfs(tomatos):
    today = deque()
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]
    unripe = 0  # 방문할 수 있는 노드를 다 돌았는데도 덜 익은 토마토가 남은 경우를 위해 계산. (unripe : 설익은)
    date = 0    # 날짜 계산

    # 최초 1회, 다른 토마토에 영향을 줄 익은 토마토를 today 덱에 추가.
    # 이 때 확인된 익은 토마토는 방문 표시.
    # 덜 익은 토마토를 세기 위해 발견시 unripe += 1.
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 1 and not visited[i][j][k]:
                    today.append((i, j, k))
                    visited[i][j][k] = True
                elif tomatos[i][j][k] == 0:
                    unripe += 1

    # 익은 토마토를 기준으로 today에서 원소를 하나씩 꺼내어 주변 검사.
    # 덜 익은 토마토 발견시 1을 재할당해 익게 만들어주고 방문표시, unripe 에서도 1씩 차감.
    # 새롭게 익은 토마토들은 today가 아닌 next_day 덱에 추가.
    while True:
        next_day = deque()  # 새롭게 익을 토마토를 저장하기 위한 덱

        while today:
            ci, cj, ck = today.popleft()

            for ei,ej,ek in ((0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)):
                ni, nj, nk = ci + ei, cj + ej, ck + ek
                if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and not visited[ni][nj][nk]:
                    if tomatos[ni][nj][nk] == 0:
                        tomatos[ni][nj][nk] = 1
                        visited[ni][nj][nk] = True
                        unripe -= 1
                        next_day.append((ni, nj, nk))
        
        # next_day가 비었을 경우 덜 익은 토마토를 발견하지 못함 == 익을 수 있는 토마토는 다 익었다는 뜻.
        # unripe가 0이 아니라면 구조상 익을 수 없는 토마토가 있다는 뜻이므로 -1을 리턴.
        # 0이라면 경과 날짜 date를 리턴.
        if not next_day:
            if unripe:
                return -1
            else:
                return date

        # 함수가 종료되지 않았다면 다음 날로 넘어가야 함.
        # 앞선 while문에서 이미 다음 날 익을 토마토를 다 1로 재할당했으므로 날짜에 +1.
        # 새롭게 익은 토마토들을 기준으로 다시 while문을 돌려야 하므로 today에 next_day를 할당.
        date += 1
        today = next_day             

if __name__ == "__main__":
    M, N, H = map(int, input().split())
    tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    print(bfs(tomatos))