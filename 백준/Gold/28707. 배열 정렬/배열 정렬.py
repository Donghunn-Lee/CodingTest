# # 배열 정렬

# # 풀릴 듯 말 듯 했는데 시간이 많이 걸릴 것 같아 검색. 2만번 후반대 문제라 자료가 많지 않았음.
# # 우선 처음 눈에 띈 건 입력 수가 매우 적은 것. 배열의 길이가 8이하이고 조작의 개수도 10개라 복잡한 연산의 필요를 느낌.
# # 완전탐색으로 각각의 배열 값에 코스트를 묶어서 계산해야 하는 것까진 생각했으나, 쉽사리 다익스트라를 연관짓지는 못함.
# # 다익스트라임가 필요함을 확인 후, 조작 후 배열의 값을 하나의 노드로 하여 코스트를 최소화 하는 방법까지 떠올림.
# # 검색한 코드를 참고하여 코드 작성. 검색한 문제에선 클래스를 사용하여 노드를 구현했는데, 나는 그럴 필요를 느끼지 못함.
# # 그러나 바꾸고 나니 visited의 추가, list변환과 tuple 변환을 계속해가며 시간이 많이 길어질 수도 있겠다고 생각함.

# import sys, heapq
# input = sys.stdin.readline

# def sol(seq):
#     graph = dict()
#     graph[seq] = 0
#     q = []
#     heapq.heappush(q, (graph[seq], seq))
#     visited = set()

#     while q:
#         cost, cur_seq = heapq.heappop(q)

#         if cur_seq in visited:
#             continue

#         for l, r, c in operation:
#             nxt_seq = list(cur_seq)
#             nxt_seq[l], nxt_seq[r] = nxt_seq[r], nxt_seq[l]
#             nxt_seq = tuple(nxt_seq)
#             nxt_cost = cost + c
        
#             if nxt_seq not in graph:
#                 graph[nxt_seq] = nxt_cost
#                 heapq.heappush(q, (nxt_cost, nxt_seq))
                
#             elif nxt_cost < graph[nxt_seq]:
#                 graph[nxt_seq] = nxt_cost
#                 heapq.heappush(q, (nxt_cost, nxt_seq))
        
#         visited.add(cur_seq)
    
#     return graph


# if __name__ == "__main__":
#     N = int(input())
#     A = tuple([0] + list(map(int, input().split())))
#     M = int(input())
#     operation = [tuple(map(int, input().split())) for _ in range(M)]

#     target_seq = tuple(sorted(A))

#     graph = sol(A)

#     print(graph[target_seq] if graph.get(target_seq) else -1)

import sys, heapq

input = sys.stdin.readline

class Node:
    def __init__(self, arr, cost):
        self.arr = arr
        self.visited = False
        self.cost = cost

def solution(arr, manipulates):
    graph = dict()
    graph[arr] = Node(arr, 0)
    hq = [] # 다익스트라를 위한 우선순위 큐
    heapq.heappush(hq, (graph[arr].cost, arr))
    
    while hq:
        cost, arr = heapq.heappop(hq)
        node = graph[arr]
        
        if node.visited:
            continue
        
        for l, r, c in manipulates:
            tmp = list(arr)
            next_cost = cost + c
            tmp[l-1], tmp[r-1] = tmp[r-1], tmp[l-1]
            tmp = tuple(tmp)
            
            if graph.get(tmp) is None:
                graph[tmp] = Node(tmp, next_cost)
                heapq.heappush(hq, (next_cost, tmp))
                continue
            if next_cost < graph[tmp].cost:
                graph[tmp].cost = next_cost
                heapq.heappush(hq, (next_cost, tmp))

        node.visited = True
        
    return graph

if __name__ == "__main__":
    N = int(input())
    arr = tuple(map(int, input().split()))
    # arr.insert(0, 0) # 1부터 시작하므로 안쓰는 0번 인덱스에 최소값 0 삽입
    M = int(input())
    manipulates = [list(map(int, input().split())) for _ in range(M)]
    
    # 비내림차순 배열
    target = tuple(sorted(arr))
    
    graph = solution(arr, manipulates)
    
    print(graph[target].cost if graph.get(target) else -1)