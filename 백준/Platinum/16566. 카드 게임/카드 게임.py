# 카드 게임

import sys
input = sys.stdin.readline

# bisect 알고리즘
def binary_search(seq, num):
    low = -1
    high = len(seq)

    while low + 1 < high:
        mid = (low + high) // 2

        if seq[mid] < num:
            low = mid
        else:
            high = mid

    return high

def sol(card, target_card):
    ans = []
    visited = set()

    for target in target_card:
        idx = binary_search(card, target)

        if card[idx] == target:
            idx += 1

        while idx < M - 1 and (idx in visited or card[idx] <= target):            
            idx += 1
        
        ans.append(card[idx])
        visited.add(idx)
    
    return "\n".join(map(str, ans))

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    card = list(map(int, input().split()))
    card.sort()
    target_card = list(map(int, input().split()))

    print(sol(card, target_card))
