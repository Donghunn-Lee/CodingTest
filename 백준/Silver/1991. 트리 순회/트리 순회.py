# 트리 순회

# 재귀 함수 먼저 떠오르긴 했는데 매번 dfs때 재귀만 쓰다가 스택도 좀 써 봐야지 하고 스택으로 풀어보려니까 모르겠음.
# 그래서 그냥 패턴이 금방 보일 것 같은 재귀로 풀이.
# 전위 순환은 함수 실행시 문자 추가, 중위는 반복 내에서 추가, 후위는 반복 후에 추가 하면 해결.

import sys
input = sys.stdin.readline

def preorder(parent):
    global ans1
    ans1 += parent

    for i in tree[parent]:
        if i != '.':
            preorder(i)

def inorder(parent):
    global ans2

    for i in tree[parent]:
        if i != '.':
            inorder(i)
    
        if parent not in ans2:
            ans2 += parent
        

def postorder(parent):
    global ans3

    for i in tree[parent]:
        if i != '.':
            postorder(i)
    
    ans3 += parent
        

if __name__ == "__main__":
    N = int(input())
    tree = dict()
    ans1, ans2, ans3 = '', '', ''

    for i in range(N):
        abc = input().rstrip().split()

        if i == 0:
            root = abc[0]

        tree[abc[0]] = abc[1:]

    preorder(root)
    inorder(root)
    postorder(root)

    print(ans1)
    print(ans2)
    print(ans3)