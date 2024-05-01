# 아기 상어

# 괜히 오기부려서 오래 걸린 문제.
# bfs를 입력 값에서 먹이를 먹을 때까지 한 번만 실행하도록 구성하고 외부에서 bfs를 반복하는 것이 정배.
# 그런데 굳이 bfs 안에서 하려고 애쓰다 너무 오래 걸렸음. 또 전부 완탐인데 그리디를 섞으려던 것도 문제였음.
# 일단 문제는 먹을 수 있는 모든 물고기를 발견할 때 까지 bfs로 탐색.
# 발견한 물고기들을 우선순위대로 정렬하여 가장 높은 우선순위의 물고기 한 마리를 포식.
# 아기 상어의 성장 여부를 확인하고 visited와 deq을 초기화, 해당 지점을 기점으로 다시 bfs 탐색 시작.
# 만약 먹을 수 있는 물고기를 발견하지 못했다면 마지막으로 물고기를 먹은 시점의 경과 시간을 리턴.
import sys
from collections import deque
input = sys.stdin.readline

# 아기 상어 위치 찾기.
def find_fishes():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                shark = (i, j)
                return shark


def hunting(shark, size, ate, sec):
    deq = deque()
    deq.append((shark[0], shark[1], sec))       # 상어의 좌표와 경과시간.
    dir = ((-1, 0), (0, -1), (0, 1), (1, 0))    # 우선순위대로의 direction이지만 정렬해야하므로 의미없음.
    graph[shark[0]][shark[1]] = 0   # 상어 위치를 9에서 초기화.
    visited = {shark}   
    
    # bfs를 반복
    while True:
        candidate = []  # 먹이 후보들을 저장하는 리스트. bfs시작 시 초기화.

        # bfs 로직.
        while deq:
            ci, cj, c_sec = deq.popleft()
            
            for di, dj in dir:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                    # 아기 상어보다 작은 물고기가 있는 경우.
                    if 0 < graph[ni][nj] < size:
                        # 후보에 추가. 정렬을 위해 시간도 같이 추가해야함.
                        candidate.append((ni, nj, c_sec + 1))
                    
                    # 아기 상어와 크기가 같은 물고기이거나 빈 칸인 경우.
                    elif graph[ni][nj] == size or graph[ni][nj] == 0:
                        visited.add((ni, nj))
                        deq.append((ni, nj, c_sec + 1))
                    
                    # 아기 상어보다 더 큰 물고기인 경우.
                    else:
                        visited.add((ni, nj))

        # 먹이 후보 물고기가 있는 경우
        if candidate:
            # 해당 물고기를 발견한 시간, 가장 높이 있는, 가장 왼쪽에 있는 물고기를 찾기 위해 정렬.
            candidate.sort(key = lambda x : (x[2], x[0], x[1]))
            ti, tj, t_sec = candidate[0]    # 우선순위 최상위의 물고기.

            graph[ti][tj] = 0
            ate += 1
            sec = t_sec

            # 먹은 마리수가 size와 동일해진 경우 1만큼 성장.
            if size == ate:
                size += 1
                ate = 0

            # 다시 bfs를 돌리기 위해 deq과 visited를 초기화.
            deq = deque()
            deq.append((ti, tj, t_sec))
            visited = set()
            visited.add((ti, tj))

        else:
            return sec

if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    shark = find_fishes()
    
    ans = hunting(shark, 2, 0, 0)

    print(ans)