# 계단 수

# 그냥 벽.
# 비트 연산 문제는 거의 풀어 본 적이 없어서 그렇기도 하지만, 머릿속에 쉽게 와 닿지가 않음.
# 연산 수가 많으니 dp를 써야 하는 건 알겠는데 어떻게 써야 할 지가 벽이었음.
# 그나마 이건 참고한 게시글에서 설명을 잘 해줘서 조금 이해할 수 있었음. (https://konkukcodekat.tistory.com/139)

# 핵심은 0부터 9까지 모두 한 번씩 사용되어야 한다는 조건을 0b1111111111의 비트를 사용해 체크한다는 것.
# dp[자리수][마지막(우측)숫자][사용된 숫자들의 비트 값] 형태의 3차원 dp테이블을 생성. 1의 자리 값에 먼저 1을 할당.
# 반복 = 길이 N * 숫자 범위(0~9) * 0에서 9까지 표시 가능한 10자리 비트의 십진수 값(2**10 = 1024 => 0부터 1023까지).
# 마지막 숫자 값에 따라서 0보다 크면 1씩 빼는 게 가능하고, 9보다 작으면 1씩 더하는 것이 가능하기에 조건을 구분.
# 계산 후 0을 빼고 1부터 9까지를 첫 번째로 하며 10개 숫자를 모두 사용한(0b1111111111인) 경우의 합을 계산하여 출력.

import sys
input = sys.stdin.readline

def find_stair_num():
    # dp[자리수][마지막(우측)숫자][사용된 숫자들의 비트 값]
    dp = [[[0] * bit_range for _ in range(num_range)] for _ in range(N + 1)]
    ans = 0

    # 1 ~ 9로 시작하는 길이 1의 dp를 갱신. ex) 0b0000000001, 0b0000000010, 0b0000000100 ...
    for i in range(num_range):
        dp[1][i][1 << i] = 1
    
    # 길이 N을 채울 때까지.
    # 식 내에서 N + 1을 계산하므로 N - 1까지 반복하면 길이 N을 구할 수 있음.
    for i in range(1, N):
        # 각 자리마다 0부터 9를 모두 대입하며
        for j in range(num_range):
            # 0부터 1023까지의 모든 비트값을 계산
            for bit in range(bit_range):

                # 0에선 1을 뺄 수 없고, 9에선 1을 더할 수 없음.
                if 0 <= j < 9:
                    tmp = bit | 1 << (j + 1)
                    dp[i + 1][j + 1][tmp] += dp[i][j][bit]
                    dp[i + 1][j + 1][tmp] %= mod

                if 0 < j <= 9:
                    tmp = bit | 1 << (j - 1)
                    dp[i + 1][j - 1][tmp] += dp[i][j][bit]
                    dp[i + 1][j - 1][tmp] %= mod

    # 조건을 만족하는 계단 수의 합을 도출.
    for i in range(1, num_range):
        ans += dp[N][i][0b1111111111]   # => 1023
        ans %= mod
    
    return ans


if __name__ == "__main__":
    N = int(input())
    mod = 1_000_000_000
    num_range = 10
    bit_range = 1 << 10

    print(find_stair_num())