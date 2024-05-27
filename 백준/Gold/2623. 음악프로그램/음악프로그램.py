# 음악프로그램

# 특정 노드 방문을 위한 선방문 조건 => 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    deq = deque()
    ans = []

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            deq.append(i)
    
    while deq:
        cur = deq.popleft()
        ans.append(str(cur))
        
        for n in edges[cur]:
            in_degree[n] -= 1

            if in_degree[n] == 0:
                deq.append(n)
    
    if len(ans) < N:
        return 0
    
    else:
        return "\n".join(ans)

if __name__ == "__main__":
    N, M = map(int, input().split())
    in_degree = [0] * (N + 1)
    edges = [[] for _ in range(N + 1)]

    for _ in range(M):
        K, *seq = map(int, input().split())

        for i in range(1, K):
            in_degree[seq[i]] += 1
            edges[seq[i - 1]].append(seq[i])

    print(topology_sort())