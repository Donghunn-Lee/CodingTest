# 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_parent_node(parent):
    global ans

    for child in tree[parent]:
        if ans[child] == 0:
            ans[child] = parent
            find_parent_node(child)

if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    ans = [0] * (N + 1)

    for  _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    find_parent_node(1)

    print("\n".join(map(str, ans[2:])))