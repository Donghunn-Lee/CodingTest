# 세 용액

import sys
input = sys.stdin.readline

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