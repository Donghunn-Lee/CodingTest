# 트리 순회

# 재귀 함수 먼저 떠오르긴 했는데 매번 dfs때 재귀만 쓰다가 스택도 좀 써 봐야지 하고 스택으로 풀어보려니까 모르겠음.
# 그래서 그냥 패턴이 금방 보일 것 같은 재귀로 풀이.
# 전위 순환은 함수 실행시 문자 추가, 중위는 반복 내에서 추가, 후위는 반복 후에 추가 하면 해결.

#+++ 처음에 각각 함수를 만들었다가, 트리의 탐색 순서가 동일하다는 것을 깨닫고 하나의 함수에 세 가지 경우를 동시에 계산.

import sys
input = sys.stdin.readline

def cycles(parent):
    global preorder, inorder, postorder
    preorder += parent

    for i in tree[parent]:
        if i != '.':
            cycles(i)

        if parent not in inorder:
            inorder += parent

    postorder += parent


if __name__ == "__main__":
    N = int(input())
    tree = dict()
    preorder, inorder, postorder = '', '', ''

    for i in range(N):
        abc = input().rstrip().split()

        if i == 0:
            root = abc[0]

        tree[abc[0]] = abc[1:]

    cycles(root)

    print(preorder)
    print(inorder)
    print(postorder)