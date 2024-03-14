# 숨바꼭질

# 그리디로 풀 수 있을까 싶었는데 고민해보니 역시 + 1, - 1, * 2의 모든 경우를 다 계산해야한다는 생각에 도달함.
# 완전 탐색이며 최단 거리를 계산하는 문제라 bfs를 생각하면서도 그동안 bfs를 써 왔던 문제들과 조금 유형이 다르다는 생각이 들었지만 우선 써 봤더니 풀렸음.
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

    # n과 k가 같을 때의 조건이 없으면 바로 '틀렸습니다' 가 나옴.
    if n == k:
        return 0
    
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