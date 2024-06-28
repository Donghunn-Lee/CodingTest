# 숫자 카드 2

import sys
input = sys.stdin.readline

def count_num():
    ans = []

    for i in target:
        if i in deck:
            ans.append(deck[i])
        else:
            ans.append(0)
    
    return " ".join(map(str, ans))

if __name__ == "__main__":
    N = int(input())
    card_data = list(map(int, input().split()))
    deck = dict()
    for i in card_data:
        if i in deck:
            deck[i] += 1
        else:
            deck[i] = 1
    M = int(input())
    target = list(map(int, input().split()))

    print(count_num())