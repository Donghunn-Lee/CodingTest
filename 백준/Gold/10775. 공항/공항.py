# 공항

# 역시 어려운 union-find. 그래도 이번 문제를 통해 조금 더 감을 잡은 것 같음.
# 알고리즘 분류에 분리 집합이 있어서 이 의미를 찾으니 깨달음을 얻은 것.

# 핵심은 각 비행기가 들어올 때마다 도킹할 수 있는 게이트와 대체 게이트를 마련하는 것.
# 대체 게이트란 3번 비행기가 들어오고, 3번 게이트가 이미 찼을 때를 대비한 하위 게이트.
# 대체 게이트 -> root가 됨. 이를 통해 union-find 를 진행.

import sys
input = sys.stdin.readline

# find => root node 찾기.
def find_root(ap):
    stack = [ap]    # 대체 노드를 갱신시킬 게이트 번호를 저장할 스택.

    # 비행기가 들어갈 수 있는 root 탐색.
    while True:
        target_gate = alter_gate[ap]    # 현재 들어온 비행기와 같은 번호의 대체 게이트.

        # 비행기 번호와 대체 게이트 번호가 같다면 root를 찾은 것이므로
        if target_gate == ap:
            break

        # 일치하지 않다면 대체 게이트를 바꿔야 하는 대체 게이트 번호를 stack에 저장.
        # 대체 게이트의 그 다음 대체 게이트를 찾기 위해 ap에 현재 대체 게이트를 할당.
        # 다음 탐색에선 ap에 저장된 대체 게이트 번호의 비행기가 들어온 것을 가정하고 진행됨.
        else:
            stack.append(target_gate)
            ap = alter_gate[target_gate]
    
    
    # 스택에 저장된 게이트 번호들의 대체 게이트를 최종적으로 구한 root 게이트로 바꿔줌.
    for i in stack:
        alter_gate[i] = target_gate

    return target_gate


# unoin.
def union(a, b):
    # b == a - 1
    # a와 b의 root를 찾고, a의 바로 아랫 노드인 b의 root 게이트를 a게이트의 대체 게이트로 삼음.
    # a가 입력되어 union을 탐색하는 시점에서 a번의 게이트는 지금 채워지거나 이미 채워져 있음을 알아야 함.
    a_root = find_root(a)
    b_root = find_root(b)

    alter_gate[a_root] = b_root


if __name__ == "__main__":
    G = int(input())
    P = int(input())
    airplain_seq = [int(input()) for _ in range(P)]
    alter_gate = list(range(G + 1))
    ans = 0

    # 각 비행기를 순서대로 진입시키며, 가상 게이트인 0번 게이트가 root가 되는 경우 탐색 종료.
    for i in airplain_seq:
        root = find_root(i)

        if root == 0:
            break

        union(root, root - 1)
        ans += 1

    print(ans)