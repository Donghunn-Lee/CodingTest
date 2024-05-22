# 용액

# 투 포인터를 쓰는 것 가진 혼자서 생각했던 문제.
# 그런데 좀만 생각해보면 알 수 있었을 텐데 구체적인 방법을 떠올리지 못하고 시간 절약을 위해 검색...
# 나는 가운데 0을 고려하느라 못 풀고 있던 건데 생각해보니 그럴 필요가 전혀 없었음. 음수 두 개의 합도 가능함.
# 그래서 우선 왼쪽과 오른쪽 인덱스를 만들고 절댓값이 더 낮은 조합이 나오면 인덱스와 값을 갱신.
# 값이 0이 나오거나 인덱스가 엇갈리면 종료.

import sys
input = sys.stdin.readline

def two_pointer():
    left, right = 0, N - 1
    near_zero = [left, right]
    mix = abs(liquid[left] + liquid[right])

    while left < right:
        tmp_sum = liquid[left] + liquid[right]

        if abs(tmp_sum) < mix:
            near_zero = [left, right]
            mix = abs(tmp_sum)
        
            if mix == 0:
                break

        if tmp_sum < 0:
            left += 1
        
        else:
            right -= 1

    return near_zero

    
if __name__ == "__main__":
    N = int(input())
    liquid = list(map(int, input().split()))
    ans_idx = two_pointer()
    print(liquid[ans_idx[0]], liquid[ans_idx[1]])
    