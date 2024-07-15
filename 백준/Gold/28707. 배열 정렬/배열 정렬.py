# 배열 정렬

# 풀릴 듯 말 듯 했는데 시간이 많이 걸릴 것 같아 검색. 2만번 후반대 문제라 자료가 많지 않았음.
# 우선 처음 눈에 띈 건 입력 수가 매우 적은 것. 배열의 길이가 8이하이고 조작의 개수도 10개라 복잡한 연산의 필요를 느낌.
# 완전탐색으로 각각의 배열 값에 코스트를 묶어서 계산해야 하는 것까진 생각했으나, 쉽사리 다익스트라를 연관짓지는 못함.
# 다익스트라임가 필요함을 확인 후, 조작 후 배열의 값을 하나의 노드로 하여 코스트를 최소화 하는 방법까지 떠올림.
# 검색한 코드를 참고하여 코드 작성. 검색한 문제에선 클래스를 사용하여 노드를 구현했는데, 나는 그럴 필요를 느끼지 못함.

# 다 된 것 같은데 결국 내 코드는 풀리지 않았음. 검색한 코드를 게시자가 완전히 올리지 않아서 부족한 부분을 찾아 수정.
# 통과된 정답 코드와 내 코드의 차이점은, 클래스를 생성해 배열을 키로 하는 딕셔너리에 저장할 때 visited의 유무였음.
# 나는 현재 while에서 탐색중인 배열의 키 값만을 visited에 추가, graph내의 키값의 유무에 따라 값을 추가함.
# 클래스를 사용한 정답코드에선 현재 탐색한 배열을 방문처리하는 것은 같으나, 키값이 아닌 클래스 내부의 visited로 체크.
# 이렇게 하니 정답 배열을 찾는 특정 시점에서 내 코드는 graph길이가 15, 정답코드는 17개였음.
# 애초에 난 틀렸고 이건 맞으니 다른 점은 있을텐데, 사실 아직도 정확히 파악하진 못함.
# 클래스라 해도 결국 노드 하나 당 하나의 visited 값을 가지는 셈이고, 새 노드를 찾았을 때 graph에 추가하는 것도 같은데.
# 일단 시간이 너무 많이 들어 이쯤 하고 넘어가는 걸로. 나중에 다시 제대로 원인을 파악할 수 있으면 좋겠음.

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