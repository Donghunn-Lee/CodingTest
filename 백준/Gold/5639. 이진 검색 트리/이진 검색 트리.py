# 이진 검색 트리

# 개인적으론 어제 풀었던 치즈보다 더 어려웠던 문제.
# 재귀로 푸는 건 보자마자 알았지만 그 로직을 짜기가 너무 어려웠음.
# 내 문제는 한 번에 왼쪽 오른쪽 전부 순환을 돌려고 했던 것.
# 해법은 현재 노드를 기준으로 왼쪽과 오른쪽을 나누어 탐색했어야 했음.

import sys
sys.setrecursionlimit(8000)
#   후위 순환
def postorder(root, end):
    global ans

    if root > end:
        return
    
    right = end + 1

    for i in range(root + 1, end + 1):
        if tree[root] < tree[i]:
            right = i
            break

    postorder(root + 1, right - 1)
    postorder(right , end)
    ans.append(tree[root])

if __name__ == "__main__":
    tree = list(map(lambda x: int(x[:-1]), sys.stdin.readlines()))
    N = len(tree)
    ans = []
    
    postorder(0, N - 1)

    print("\n".join(map(str, ans)))
