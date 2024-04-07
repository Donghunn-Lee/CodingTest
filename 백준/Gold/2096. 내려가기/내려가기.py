# 내려가기

# 무심코 bfs로 풀려다 익숙한 테이블이 떠오르며 dp라는 사실을 인지.
# 맨 아래 부터 더할 수 있는 윗줄의 자리에 수를 더해가면서 최대, 최소 dp에 값을 갱신.
# 계산이 끝나면 각 dp리스트에서 최대, 최솟값을 뽑으면 되는 어렵지 않은 문제.

# 라고 생각했으나 메모리 제한이 괜히 강조되는 게 아니었음. 메모리 초과가 떠서 어떻게 해야 할 지 20분정도 고민.
# 모르겠다 싶어 알고리즘 분류를 확인 후 '슬라이딩 윈도우'라는 처음 보는 유형을 확인, 문제 답안을 구글링.
# 전체 배열을 저장하고 계산하는 게 아닌 각 배열을 입력 받을 때 바로 처리하고 배열을 재할당해서 메모리를 최소화 하는 것.
# 그 유형에서 '투 포인터'는 정한 범위의 크기가 변동되는 것, '슬라이딩 윈도우'는 범위는 고정하고 위치만 변동되는 것.

import sys
from collections import deque
input = sys.stdin.readline

# 거의 처음으로 풀어보는 함수에서 입력을 받는 경우의 문제.
def dp(n):
    # 첫 배열을 입력 후 max와 min dp에 할당.
    table = list(map(int, input().split()))
    max_dp = table
    min_dp = table

    for _ in range(n - 1):
        # 2번째 줄부터 반복해서 입력.
        # 이러면 얕은 복사가 아닌가 했는데 인덱스로 접근한 내부 원소 변경이 아닌 변수 재할당은 관계 없음.
        table = list(map(int, input().split()))

        # 각 자리마다 더할 수 있는 자리의 수 중 최댓값, 최솟값을 계속해서 재할당. 배열의 크기는 그대로, 내용만 바뀜.
        max_dp = [table[0] + max(max_dp[0], max_dp[1]), table[1] + max(max_dp[0], max_dp[1], max_dp[2]), table[2] + max(max_dp[1], max_dp[2])]
        min_dp = [table[0] + min(min_dp[0], min_dp[1]), table[1] + min(min_dp[0], min_dp[1], min_dp[2]), table[2] + min(min_dp[1], min_dp[2])]

    return max(max_dp), min(min_dp)


if __name__ == "__main__":
    N = int(input())
    ans = dp(N)

    print(ans[0], ans[1])