# 부분수열의 합 2

# 골드 1은 역시 벽이구나 싶었음. 전에 골드 1, 2를 쉽게 푼 적도 있는데, 그게 상당히 쉬운 편이었던 것임.
# 시간상으론 dp도 풀릴 것 같아서 해봤는데, 메모리 초과.
# 최대나 최소를 구할 땐 dp를 채우며 중복체크를 하면 되는데, 경우의 수를 찾을 땐 중복도 찾아야 해서 그런 것.

# 우선 모든 부분집합을 구하고, 그 부분 집합의 합을 넣은 리스트를 만들어 모든 경우를 비교.
# 이 때 중복값을 고려해서 다음 원소가 다른 값이 올 때까지 1씩 더함으로써 계산 가능.
# 이런 답이 떠오르지 않는 문제는 시간 절약을 위해 더 빨리 검색해봤어야 함.
# 그동안 combinations을 쓸 수 있는 문제도 안 쓸 수 있으면 가급적 안 썼는데, 이런 부분집합 문제가 나오면 써야 할 듯.
import sys
from itertools import combinations
input = sys.stdin.readline

# 부분수열을 구하는 함수.
def get_sub_seq(sum_sub_seq, sub_seq):
    for i in range(len(sub_seq) + 1):
        for sub in combinations(sub_seq, i):
            sum_sub_seq.append(sum(sub))

# 부분수열의 합 리스트 2개를 받아 더해가며 합이 S인 경우를 계산하는 함수.
def count_case(sum_left, sum_right, len_left, len_right):
    count = 0
    left_p, right_p = 0, 0  # 각 리스트의 포인터

    # 각 포인터가 리스트 길이를 초과할 경우 종료.
    while left_p < len_left and right_p < len_right:

        # 각 포인터가 가리키는 값.
        left_v, right_v = sum_left[left_p], sum_right[right_p]
        tmp_sum = left_v + right_v  # 이 때의 합이 구하려 값, seq에서 구할 수 있는 어떤 부분 수열의 합이 됨.

        # 합이 S인 경우, 중복을 체크.
        if tmp_sum == S:

            # 현재 포인터의 값을 tmp 변수에 저장.
            # 그냥 원래 변수를 사용해도 원래 반복으로 돌아갈 수는 있으나, 중복 원소의 수를 계산하려면 기존 값이 필요.
            tmp_left_p, tmp_right_p = left_p, right_p
            
            # tmp를 증가시켜가면서 가리키는 값이 달라질 때 종료.
            while tmp_left_p < len_left and sum_left[tmp_left_p] == left_v:
                tmp_left_p += 1
            
            while tmp_right_p < len_right and sum_right[tmp_right_p] == right_v:
                tmp_right_p += 1
            
            # 중복이 없었다면 각 tmp는 1씩만 더해지고 while문이 종료될 것이므로 1 * 1 = 1이 count에 더해짐.
            # 왼쪽에서 중복이 2개, 오른쪽에서 3개 있었다면 단순 경우의 수 계산으로 2 * 3 = 6이 더해짐.
            count += (tmp_left_p - left_p) * (tmp_right_p - right_p)

            # tmp로 확인한 위치도 탐색을 한 것이므로 그 위치에서 다시 탐색을 시작하기 위해 포인터를 재할당.
            left_p, right_p = tmp_left_p, tmp_right_p
        
        # tmp_sum이 S보다 큰 경우, 부분수열의 합이 내림차순 정렬되어있는 오른쪽 수열의 포인터를 +1. (=> tmp_sum 감소)
        elif tmp_sum > S:
            right_p += 1
        # 작은 경우는 오름차순 정렬인 왼쪽 수열의 포인터를 + 1. (=> tmp_sum 증가)
        else:
            left_p += 1

    if S == 0:
        return count - 1
    else:
        return count

if __name__ == "__main__":
    N, S = map(int, input().split())
    seq = list(map(int, input().split()))

    seq_left, seq_right = seq[:N // 2], seq[N // 2:]    # 수열을 왼쪽과 오른쪽으로 2분할.
    sum_left_sub, sum_right_sub = [], []    # 부분 수열의 합 리스트를 저장한 리스트.

    get_sub_seq(sum_left_sub, seq_left)
    sum_left_sub.sort() # 왼쪽은 오름차순 정렬. ex) 13 9 5

    get_sub_seq(sum_right_sub, seq_right)
    sum_right_sub.sort(reverse = True)  # 왼쪽은 내림차순 정렬. ex) -7 -5 -2

    len_left, len_right = len(sum_left_sub), len(sum_right_sub)

    print(count_case(sum_left_sub, sum_right_sub, len_left, len_right))