# 구간 합 구하기 4

# 누적 합 문제.
# 테스트 케이스가 여러개라서 당연히 한 번에 값을 다 구해두고, 주어진 인덱스를 뽑아 사용할 것을 생각함.
# 그런데 인덱스를 어떻게 해야 할 지를 모르겠어서 찾아봄. 생각보다 더 단순했음.
# [뒷 인덱스] - [앞 인덱스 - 1] 하면 앞에서 정해진 구간 앞에서 더한 값을 빼는 꼴이 됌.
import sys
input = sys.stdin.readline

def cal_prefix_sum():
    tmp = 0

    for i in seq:
        tmp += i
        prefix_sum.append(tmp)

if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    prefix_sum = [0]
    cal_prefix_sum()
    ans = []

    for _ in range(M):
        a, b = map(int, input().split())
        ans.append(str(prefix_sum[b] - prefix_sum[a - 1]))
    
    print("\n".join(ans))