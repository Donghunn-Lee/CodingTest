# 세 용액

# 최근에 푼 용액 문제의 응용버전.
# 이번엔 용액이 두 개가 아니라 3개여서 난 처음에 두 수를 더한 모든 값을 리스트에 추가하려고 했으나
# 그렇게 투 포인터를 돌린다 해도 한 값을 두 번 사용하게 되는 경우가 발생한다는 사실을 금방 깨달음.
# 좀 고민하다가 뭔가 애매해서 그냥 찾아본 답은, 투 포인터 탐색을 N번 반복하는 것이었음.
# 리스트를 반복하여 값을 하나 고르고, 중복이 아닌 다른 두 값과 앞서 고른 값을 더해 그 값의 최소치를 계산.

import sys
input = sys.stdin.readline

# 투 포인터를 N번 반복.
# nlogn + n^2
def two_pointer():
    near_zero = []
    mix = 1e11

    for cur in range(N):
        left, right = 0, N - 1

        while left < right:
            if left == cur:
                left += 1
                continue
            
            if right == cur:
                right -= 1
                continue

            cur_sum = liquid[left] + liquid[cur] +  liquid[right]

            if abs(cur_sum) < mix:
                near_zero = [liquid[left], liquid[cur], liquid[right]]
                mix = abs(cur_sum)
            
                if mix == 0:
                    break

            if cur_sum < 0:
                left += 1
            
            else:
                right -= 1

    near_zero.sort()

    return ' '.join(map(str, near_zero))


if __name__ == "__main__":
    N = int(input())
    liquid = list(map(int, input().split()))
    liquid.sort()

    print(two_pointer())