# 전깃줄 - 2

# LIS인 걸 깨닫고 내가 전에 풀었던 LIS를 참고해서 푸는데, idx를 넣을 때 값이 자꾸 헷갈려서 여기서 한 번,
# 또 출력문에 ans가 아닌 LIS를 적어놓고 왜 자꾸 답이 틀리게 나오지? 하면서 위쪽에서만 디버깅 돌려서 두 번.
# 두 번의 고비에 너무 많은 시간을 잡아먹은 문제.

import sys
input = sys.stdin.readline

# bisect 알고리즘
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

# LIS 알고리즘에서 LIS에 포함되지 않는 전깃줄을 출력하는 로직 추가.
def create_LIS(cable):
    LIS_tmp = [cable[0][1]]   # LIS를 구하기 위한 리스트. 단, 들어간 순서를 고려해야 하므로 진짜LIS는 아님.
    LIX_idx = [(0, cable[0][1])]  # 진짜 LIS를 구하기 위해 순서와 값을 저장하는 리스트.

    # 전체 리스트를 탐색.
    for i in range(1, N):

        # LIS_tmp의 마지막 값, 즉 가장 큰 값보다 더 큰 수를 찾은 경우, 해당 값과 인덱스를 저장.
        if LIS_tmp[-1] < cable[i][1]:
            LIX_idx.append((len(LIS_tmp), cable[i][1]))
            LIS_tmp.append(cable[i][1])
        
        # 증가하는 값이 아닌 경우, 이분탐색으로 해당 값이 들어갈 수 있는 자리를 찾아 해당 위치의 값을 갱신.
        # LIS_idx 내에 같은 값이 여러 개인 경우, 가장 뒤에 있는 값이 LIS에 들어갈 수 있는 값임.
        else:
            idx = binary_search(LIS_tmp, cable[i][1])
            LIS_tmp[idx] = cable[i][1]
            LIX_idx.append((idx, cable[i][1]))
    
    # 앞에서 뒤로 탐색을 진행했으므로, 역순으로 탐색하여 진짜 LIS를 구성.
    last_idx = len(LIS_tmp) - 1
    LIS = []
    for i in range(N - 1, -1, -1):
        if LIX_idx[i][0] == last_idx:
            LIS.append(LIX_idx[i][1])
            last_idx -= 1
    
    # 문제에서 요구하는 답은 LIS가 아니라 LIS가 아닌 값이므로 cable를 탐색해서 없애야 할 전깃줄을 구함.
    ans = []
    for i, j in cable:
        if j not in LIS:
            ans.append(i)

    ans.sort()

    return str(len(ans)) + "\n" + "\n".join(map(str, ans))
    

if __name__ == "__main__":
    N = int(input())
    cable = []
    for _ in range(N):
        a, b = map(int, input().split())
        cable.append((a, b))
    cable.sort(key = lambda x : x[0])

    print(create_LIS(cable))