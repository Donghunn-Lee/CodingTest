# 음악프로그램

# 특정 노드 방문을 위한 선방문 조건 => 위상 정렬
# 간만에 검색하지 않고 풀어낸 문제. 위상 정렬을 쓰는 게 아마 4번째일텐데, 알고리즘을 기억해서 풀어낸 게 뿌듯함.
# 각 노드의 진입차수를 구하고, 차수가 0일때 덱에 넣고 탐색하며 그 순서를 저장해 출력.
# 이번 문제는 입력 정보로 간선이 아니라 M명의 보조 PD의 출연 순서가 주어짐. 이것만 그래프로 처리하면 쉬웠던 문제.
# 모든 조건에 부합하는 출연 순서를 도출할 수 없는 경우를 ans에 모든 노드를 담기 전에 while이 종료되는 경우라고 상정,
# ans의 길이가 N이하인 경우 0을 반환해 출력하도록 함.
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