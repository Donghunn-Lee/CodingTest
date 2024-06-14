# 과일 탕후루

# 투 포인터를 많이 써 봤다고 생각했지만 아니었음. 제대로 알지 못하고 있었다고 생각.
# 혼자서 결국 못 풀고, 제출 수가 너무 적은 문제라 파이썬 코드가 없어서 자바 코드를 파이썬으로 변환해서 참고함.
# 내가 처음에 작성한 코드는 결국 N^2의 절반씩이나 되는 느낌. left가 증가할 때마다 right를 계속해서 초기화 했음.
# 하지만 제대로 된 투포인터는 left와 right가 어떠한 점프 없이 일정간격만 이동하는 것.

# 문제의 해답은 우선 nums 리스트에서 발견한 과일의 종류별 개수를 저장하며 right를 증가시킴.
# 이후 종류가 2개를 초과한 경우, kind가 다시 2가 될 때까지 nums에서 발견한 과일 수를 차감하며 left를 증가시킴.
# kind가 다시 2가 되었다면 다시 right를 증가시키며 탐색.
# kind가 2보다 많을 때 right도 같이 증가시키는 것이 처음엔 이해가 가지 않았지만,
# 최댓값을 매번 갱신하므로, 더 큰 경우가 존재하면 2 < kind에서 슬라이딩 윈도우로 이동해도 발견 가능하다는 것을 깨달음.

import sys
input = sys.stdin.readline

def two_pointer():
    left, right, kind, max_length, length = 0, 0, 0, 0, 0
    nums = [0] * 10     # 발견한 과일의 개수를 저장하는 리스트.

    # left가 N에 도달할 때까지 반복.
    while left < N:

        # right가 N이라면 현재 max_length가 최댓값이므로 left를 차감할 이유가 없음. 종료.
        if right == N:
            return max_length

        # 발견한 적 없는 과일이라면 kind += 1
        if nums[seq[right]] == 0:
            kind += 1
        
        # 현재의 길이와 과일 개수를 추가.
        length += 1
        nums[seq[right]] += 1

        # 발견한 과일 종류 수가 2를 초과한 경우, left를 증가시키며 과일 개수와 kind를 줄여야 함.
        if 2 < kind:
            # 발견한 과일 중 left 과일이 1개 남아있는 경우, 아래에서 차감시켜 0이 되므로 kind -= 1.
            if nums[seq[left]] == 1:
                kind -= 1
            
            # left에서 발견한 과일의 개수, 현재 길이를 차감.
            # 탐색을 위해 left += 1.
            nums[seq[left]] -= 1
            length -= 1
            left += 1
        
        # 차감, 증가 결과에 상관 없이 최댓값 갱신, right 증가.
        max_length = max(max_length, length)
        right += 1

    return max_length

if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    
    print(two_pointer())