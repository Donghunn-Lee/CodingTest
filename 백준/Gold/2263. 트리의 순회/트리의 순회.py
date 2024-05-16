# 트리의 순회

# 재귀를 써야 한다는 점과 후위 순회의 마지막이 루트이고 중위순회는 중간에 껴 있다는 특징을 이용해 풀어보려고 했으나,
# 바로 풀어내기엔 너무 어려웠음. 그래도 검색해 찾은 답안과 방향 자체는 비슷했기에 조금 위안.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 인오더와 포스트오더의 각 start 와 end를 입력으로 받음.
def make_pre_order(in_start, in_end, post_start, post_end):

    # 이분탐색이나 분할정복처럼 start와 end가 수렴하면 종료.
    if in_start > in_end or post_start > post_end:
        return
    
    # 루트 노드값을 저장하고 출력에 추가.
    parents = post_order[post_end]
    pre_order.append(str(parents))

    # 왼쪽과 오른쪽 서브트리를 구성하기 위한 값을 계산. 양쪽의 차를 이용해 범위를 조정하기 위함.
    left = position[parents] - in_start
    right = in_end - position[parents]

    # 왼쪽 서브 트리 먼저 탐색되어야 전위순회 가능.
    # 앞서 구한 값으로  범위를 좁혀가며 분할 정복으로 왼쪽과 오른쪽 서브 트리를 탐색.
    make_pre_order(in_start, in_start + left - 1, post_start, post_start + left - 1)
    make_pre_order(in_end - right + 1, in_end, post_end - right, post_end - 1)


if __name__ == "__main__":
    N = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    
    position = [0] * (N + 1)
    for i in range(N):
        position[in_order[i]] = i
    
    pre_order = []

    make_pre_order(0, N - 1, 0, N - 1)

    print(" ".join(pre_order))
