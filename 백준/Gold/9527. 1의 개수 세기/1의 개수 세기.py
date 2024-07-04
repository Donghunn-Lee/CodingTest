# 1의 개수 세기

# 일단 스스로는 못 풀었고, 되게 코드가 짧을 것 같았고 실제로 그랬는데 한참 이해하지 못했던 문제. 난 이진수에 너무 약함.
# 핵심 점화식은 2의 i승 이전까지 수들의 1의 개수 누적합이 2 ** (i - 1) + 2 * ((i - 1)까지 누적합).

import sys
input = sys.stdin.readline

# 미리 구해놓은 2의 거듭제곱수의 누적합을 사용해 주어진 수 까지의 누적합을 반환.
def count_one(n):
    cnt = 0
    bin_num = bin(n)[2:]    # 이진 문자열 변환 후 0b 제외.
    length = len(bin_num)

    # 가장 큰 자릿수인 왼쪽부터 계산 시작.
    for i in range(length):

        # 1인 경우,
        if bin_num[i] == '1':

            # 해당 자릿수 보다 작은 것 중 가장 큰 2의 거듭제곱을 찾아 누적합을 더함.
            # 또한 2^n ~ 2^(n+1)의 수는 가장 큰 자리의 수가 모두 1이므로 그 개수도 함께 더함.
            pow = length - i - 1
            cnt += pow_sum[pow] + (n - 2 ** pow + 1)

            # 이진수 왼쪽의 1을 이미 계산했으므로 주어진 수에서 1을 빼줘야 함. ex) '1'010 0010 -> 00'1'0 0010
            n = n - 2 ** pow
    
    return cnt


if __name__ == "__main__":
    A, B = map(int, input().split())
    pow_sum = [0 for i in range(60)]

    for i in range(1, 60):
        pow_sum[i] = 2 ** (i - 1) + 2 * pow_sum[i - 1]
    
    # A부터 B까지이므로 B까지의 누적합에서 A이전의 누적합을 빼줌.
    print(count_one(B) - count_one(A - 1))