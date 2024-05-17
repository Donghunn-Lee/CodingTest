# 두 배열의 합

# 완전 탐색으로 A의 누적합을 하나 구하고 B의 모든 누적합을 다 돌리는 방법이 떠올랐지만 당연히 이건 아닌 것 같았음.
# 고민하다가 뭔가 다른 방법이다 싶어 분류 확인. 이분 탐색과 누적 합. 해시를 사용한 집합과 맵도 있던데 이건 잘?

# 해답은 누적 합 리스트를 각각 구하고, 이분 탐색으로 값이 존재하는 경우 인덱스를 반환받아 개수를 계산함.
# 이분 탐색은 파이썬 라이브러리 bisect를 사용.

# +++ 집합은 모르겠고 딕셔너리를 활용한 방법은 있었음. 처음부터 끝까지의 누적합을 먼저 구하고, 인덱스가 더 큰 원소에서 작은 원소를 빼면 두 인덱스 사이의 누적합이 나오는 것을 이용한 방법. 이게 더 효율적으로 보이긴 함.

import sys, bisect
input = sys.stdin.readline

# 각 배열의 누적 합 구하기.
def cal_cumulative_sum(sum_A, sum_B):
    for i in range(N):
        tmp = A[i]
        sum_A.append(tmp)

        for j in range(i + 1, N):
            tmp += A[j]
            sum_A.append(tmp)

    for i in range(M):
        tmp = B[i]
        sum_B.append(tmp)

        for j in range(i + 1, M):
            tmp += B[j]
            sum_B.append(tmp)

    # 이분탐색을 위해선 정렬이 필수.
    sum_A.sort()
    sum_B.sort()


def sum_sub_array():
    count = 0
    sum_A, sum_B = [], []
    cal_cumulative_sum(sum_A, sum_B)

    # 이분탐색을 들어만 봤지, bisect는 전에 어디서 본 것 같긴 한데 써 보기는 처음임.
    # 조금 이해가 잘 안 되다가 갑자기 딱 됐음. 주어진 배열에서 특정 값의 왼쪽 인덱스와 오른쪽 인덱스를 구할 수 있는 것.
    # 특정 값이 여러 개라면 오른쪽 인덱스 - 왼쪽 인덱스는 특정 값의 개수가 됨. 이 점을 풀이에 활용.
    for i in range(len(sum_A)):
        left = bisect.bisect_left(sum_B, T - sum_A[i])
        right = bisect.bisect_right(sum_B, T - sum_A[i])

        # right - left를 더하므로, 구하는 값이 없는 경우 같은 값이 들어가서 count에 0이 더해져 의미 없음.
        count += right - left

    return count


if __name__ == "__main__":
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    print(sum_sub_array())