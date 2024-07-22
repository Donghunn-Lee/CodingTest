# 카드 게임

# 다시 오랜만에 검색 없이 혼자 풀어낸 문제.
# 딱 봐도 이분탐색인가 싶었는데 플레 5인데 이것밖에 없나? 하는 의구심을 가지고 풀었음.
# 더 있던 것은 이분탐색으로 찾은 값을 리스트에서 제거하고, 값을 제거하여 다시 정렬할 때의 시간복잡도였음.
# 그 시간을 줄이기 위해, 리스트 길이를 조정하지 않고 visited 집합을 만들어 방문한 idx를 저장하여 체크함.
# 이분탐색의 결과가 같은 경우, 더 큰 수를 내야 하므로 사용하지 않은 카드를 찾을 때까지 idx를 증가시킴.
# 찾은 값을 저장해가며 출럭.

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

        while idx < M - 1 and idx in visited:
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
