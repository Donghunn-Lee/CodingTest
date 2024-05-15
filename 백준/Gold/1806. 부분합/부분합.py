# 부분합

# 수열에서 조건을 만족하는 부분합을 구하고, 그 부분합 중 최소 길이의 부분합을 찾아 길이를 리턴하는 문제.
# 골드 12만 풀다 4를 만나니 확실히 방법까지 도달할 수 있는 게 뭔가 맘이 편했음.
# 투 포인터를 써야겠다고 바로 접근하여 푸는데, 문제는 합을 구하는 방식.
# 나는 sum(seq[start:end])를 사용함. 저번 문제에서 사용했던 기억이 있었기 때문.
# 하지만 아니었음. sum을 구하는 것도 길이만큼 시간복잡도가 들어감. 답은 포인터를 움직일 때 해당 값을 바로 더하고 빼기.
# 그것만 생각하면 꽤 쉬운 문제.

import sys
input = sys.stdin.readline
INF = 1e9

def two_pointer(seq):
    start, end = 0, 0
    min_length = INF
    tmp_sum = 0

    while True:
        
        # 이 조건을 제대로 이해하지 못해서 다른 코드로도 풀려야 하는 게 아닌가? 하고 한참 고민함.
        # 나는 그냥 end가 최대 길이에 도달하면 바로 종료시켜버렸는데,
        # end를 최대 길이에 세워두고 start를 좁혀도 여전히 S보다 tmp_sum이 큰 경우가 존재함. 당연한 건데 깨닫지 못함.
        if S <= tmp_sum:
            min_length = min(min_length, end - start)
            tmp_sum -= seq[start]
            start += 1

        # end가 N이면 반복을 종료하지만, S <= tmp_sum 이 False가 될 때 이 elif 문이 실행되므로 길이를 좁힐 수 있음.
        elif end == N:
            break
    
        else:
            tmp_sum += seq[end]
            end += 1

        
    if min_length == INF:
        return 0
    
    else:
        return min_length

if __name__ == "__main__":
    N, S = map(int, input().split())
    seq = list(map(int, input().split()))

    print(two_pointer(seq))