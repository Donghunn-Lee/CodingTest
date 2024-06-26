# 숨바꼭질

# 그리디로도 풀 수 있을 것 같은데 고민해봐도 방법을 떠올리지 못했음.
# 결국 + 1, - 1, * 2의 모든 경우를 다 계산함.
# 완전 탐색이며 최단 거리를 계산하는 문제라 bfs를 사용하여 풀긴 했으나,
# 역시 재귀로 더 간단하게 푸는 방법이 있었음. 그런데 잘 이해는 안되서 그냥 넘어가는 걸로.
import sys
from collections import deque
input = sys.stdin.readline

# 일반적인 bfs구조에 케빈 베이컨 문제에서 배웠던 현재 값에 1씩 거리를 더하는 방식을 적용.
# 거리 
def bfs(n, k):
    q = deque()
    q.append(n)
    visited = [False] * (100001)    # 입력 변수 최댓값만큼 생성.
    distance = [0] * (100001)

    # n이 k보다 큰 경우, 왼쪽으로는 -1 씩 이동밖에 못하므로 n - k를 출력.
    # 두 값이 같은 경우도 0 출력.
    if n >= k:
        return n - k
    
    while q:
        ci = q.popleft()
        gap = [ci + 1, ci - 1, ci * 2]

        for ni in gap:
            if 0 <= ni < 100001:
                if not visited[ni]:
                    q.append(ni)
                    visited[ni] = True
                    
                    # 현재 위치 ci에서 1초 후 다음 위치 ni로 이동하는 것이므로 아래와 같이.
                    distance[ni] = distance[ci] + 1

        # k 번째 값이 0에서 다른 값으로 할당되면 리턴.
        if visited[k]:
            return distance[k]

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(bfs(N, K))