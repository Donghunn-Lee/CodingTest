# 합이 0인 네 정수

# 딱 보고 정렬과 투 포인터를 써야 하는 문제라는 것은 파악함. 그러나 그 다음은 나아가지 못함.
# 시간 내에 순서쌍을 만드는 방법이 도저히 떠오르지 않을 듯해서, 빠르게 검색.

# 답은 4개의 배열을 두 개씩 더해서 새로운 두 배열을 만들고 정렬, 두 배열 간의 합이 0인 경우를 투 포인터로 찾아내는 것.
# 막상 방법을 알고보니 그리 어렵지 않은 듯했으나, 역시 답을 찾아보지 않았다면 혼자서는 생각해내기 어려웠을 듯함.
# 이런 경우도 있다는 것을 기억속에 남기는 것이 다음을 위해 도움이 될 것이라 생각함.

import sys
input = sys.stdin.readline

def two_pointer():
    ans = 0
    len_ab, len_cd = len(ab), len(cd)   # 전체 길이로 리스트 범위를 확인해야 하므로, 저장해 사용하는 것이 효율적임.
    left, right = 0, len_cd - 1         # 포인터의 양쪽 값.

    # 포인터가 ab와 cd의 범위를 벗어날 때까지 반복.
    while left < len_ab and 0 <= right:
        if ab[left] + cd[right] == 0:
            nxt_left, nxt_right = left + 1, right - 1

            while nxt_left < len_ab and ab[left] == ab[nxt_left]:
                nxt_left += 1
            
            while 0 <= nxt_right and cd[right] == cd[nxt_right]:
                nxt_right -= 1
            
            ans += (nxt_left - left) * (right - nxt_right)
            left, right = nxt_left, nxt_right
        

        elif 0 < ab[left] + cd[right]:
            right -= 1

        else:
            left += 1

    return ans


if __name__ == "__main__":
    N = int(input())
    seq = [list(map(int, input().split())) for _ in range(N)]

    ab, cd = [], []
    for i in range(N):
        for j in range(N):
            ab.append(seq[i][0] + seq[j][1])
            cd.append(seq[i][2] + seq[j][3])
    
    ab.sort()
    cd.sort()

    print(two_pointer())