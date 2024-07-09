# 싸이클 게임

# 최근 union-find 문제를 자주 접하는데, 여전히 쉽사리 이해가 잘 가지 않음.
# 그래도 이번 문제로 조금 더 이해도를 높인 듯함.
# 노드 간 연결을 확인하고, 가장 높거나 낮은 수를 root 노드로 정함.
# 어떤 집합에 포함되는 노드는 모두 해당 인덱스에 root 노드의 값을 가짐.
# 이 root를 찾아 할당하는 과정이 find 이고, 다른 root를 가진 집합의 연결시 실행하는 게 union.
# 이 문제도 기초적인 union-find 문제인 듯해서 그나마 쉽게 이해할 수 있었음.

import sys
input = sys.stdin.readline

def find(x):
    while x != parents[x]:
        x = parents[x]
    
    return x

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x == parent_y:
        return True

    if parent_x < parent_y:
        parents[parent_y] = parent_x
    else:
        parents[parent_x] = parent_y

    return False

if __name__ == "__main__":
    N, M = map(int, input().split())
    parents = [i for i in range(N)]
    ans = 0

    for i in range(1, M + 1):
        x, y = map(int, input().split())
        
        if union(x, y):
            ans = i
            break

    print(ans)