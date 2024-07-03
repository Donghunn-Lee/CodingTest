# 가장 긴 증가하는 부분 수열5

# LIS문제는 몇 개 풀었지만 풀 때마다 어려움. dp중에 만만한 문제가 있었던가. 아무튼 얼마 풀다 못해 검색함.
# 우선 이 문제의 경우 LIS의 길이만이 아니라 LIS 자체를 구해야 하기 때문에 dp리스트가 필요함.
# 주어진 수열을 차례로 탐색하면서 이진 탐색으로 LIS를 생성함.
# 이 때 dp리스트엔 현재 탐색중인 수와 그 수가 들어갈 위치를 튜플로 저장함.
# 탐색이 끝나면 dp테이블의 뒤에서부터 LIS 인덱스에 맞는 수를 찾아 ans리스트에 추가해가며 결과를 출력.
import sys
input = sys.stdin.readline

# 이진 탐색.
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

def cal_LIS(seq):
    LIS = [seq[0]]
    dp = [(0, seq[0])]

    for i in range(1, N):
        if LIS[-1] < seq[i]:
            dp.append((len(LIS), seq[i]))
            LIS.append(seq[i])
        
        else:
            idx = binary_search(LIS, seq[i])
            LIS[idx] = seq[i]
            dp.append((idx, seq[i]))
    
    last_idx = len(LIS) - 1
    ans = []

    # 역추적.
    # 뒤에서부터 다음 인덱스의 수가 발견될 때마다 ans리스트에 추가.
    for i in range(len(dp) - 1, -1, -1):
        if dp[i][0] == last_idx:
            ans.append(dp[i][1])
            last_idx -= 1
    
    ans.reverse()

    return str(len(ans)) + "\n" + " ".join(map(str, ans))


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    print(cal_LIS(A))