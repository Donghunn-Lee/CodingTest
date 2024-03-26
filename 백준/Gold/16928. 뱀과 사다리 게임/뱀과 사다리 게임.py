# 뱀과 사다리 게임

# 이게 무슨 게임인지 몰라서 조금 당황했지만, 생각해보니 그냥 0부터 100까지 리스트만 있으면 되는 거라 단순했던 문제.
# 1부터 100의 각 칸까지 도달할 수 있는 최소 주사위 롤 횟수를 저장하는 dp 리스트 count를 기반으로 최소횟수 => bfs 사용.
# 그리고 탐색 과정에서 사다리와 뱀의 간선 리스트를 사용해 칸을 이동시켜주기만 하면 됨.

# +++ 혼자 무리없이 풀긴 했는데 다른 답들을 보니 역시 내 코드에서 좀 비효율적인 부분들이 많았음. 고로 반영하여 수정.
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    deq.append(1)
    visited = [False] * 101
    count = [0] * 101

    while deq:
        ci = deq.popleft()

        for d in range(1, 7):
            ni = ci + d
            if ni <= 100:
                if ni in move:
                    ni = move[ni]
                if not visited[ni]:
                    deq.append(ni)
                    visited[ni] = True
                    count[ni] = count[ci] + 1

                # # 덱을 사용해 popleft를 하는 bfs에선 처음 발견하는 경우가 최소 횟수 or 최소 경로.
                # if count[100]:
                #     return count[100]
    return count[100]

if __name__ == "__main__":
    N, M = map(int, input().split())
    move = dict()
    
    for _ in range(N + M):
        a, b = map(int, input().split())
        move[a] = b

    print(bfs())