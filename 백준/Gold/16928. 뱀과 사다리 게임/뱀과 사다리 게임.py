# 뱀과 사다리 게임

# 이게 무슨 게임인지 몰라서 조금 당황했지만, 생각해보니 그냥 0부터 100까지 리스트만 있으면 되는 거라 단순했던 문제.
# 1부터 100의 각 칸까지 도달할 수 있는 최소 주사위 롤 횟수를 저장하는 dp 리스트 count를 기반으로 최소횟수 => bfs 사용.
# 그리고 탐색 과정에서 사다리와 뱀의 간선 리스트를 사용해 칸을 이동시켜주기만 하면 됨.
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    deq.append(1)
    visited = [False] * 101
    dice = (1, 2, 3, 4, 5, 6)
    count = [0] * 101

    while deq:
        ci = deq.popleft()

        for d in dice:
            ni = ci + d
            if 0 <= ni <= 100 and not visited[ni]:
                # 사다리 칸 도착시 jump.
                if ni in ladder:
                    jump_up = ladder[ni]
                    deq.append(jump_up)
                    visited[jump_up] = True

                    # 이동한 칸을 더 적은 횟수의 다른 경로로 도달할 수 있는 경우를 대비해서 값의 초기화 유무 확인.
                    if count[jump_up]:
                        count[jump_up] = min(count[jump_up], count[ci] + 1)
                    else:
                        count[jump_up] = count[ci] + 1
                # 뱀 칸 도착시 slip.
                elif ni in snakes:
                    slip_down = snakes[ni]
                    deq.append(slip_down)
                    visited[slip_down] = True
                    if count[slip_down]:
                        count[slip_down] = min(count[slip_down], count[ci] + 1)
                    else:
                        count[slip_down] = count[ci] + 1
                    
                # 일반 칸
                else:
                    deq.append(ni)
                    count[ni] = count[ci] + 1
                
                # 덱을 사용해 popleft를 하는 bfs에선 처음 발견하는 경우가 최소 횟수 or 최소 경로.
                if count[100]:
                    return count[100]
                
                # 일반 칸뿐만 아니라 사다리, 뱀도 그 시작점 또한 방문 처리가 필요하므로 맨 밑에 위치.
                visited[ni] = True
                

if __name__ == "__main__":
    N, M = map(int, input().split())
    ladder, snakes = dict(), dict()
    
    for _ in range(N):
        x, y = map(int, input().split())
        ladder[x] = y

    for _ in range(M):
        u, v = map(int, input().split())
        snakes[u] = v

    print(bfs())