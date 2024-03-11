# 숨바꼭질 6

# 최대 공약수를 계산해야하는 문제인 줄 몰랐음.
# 처음 제출했던 방식은 시작점과 전체 점들 중 두 수의 차의 절댓값을 모두 구하고
# 그 중 가장 적은 것을 기준으로 1씩 빼가가며 반복,
# 그 안에서 target과 거리를 같이 증가시켜가면서 계산했서 답은 도출했으니 당연히 시간초과가 나왔음.
# 찾아보니 최대공약수라는 단어만 보고 깨달아서 아래 코드를 다시 작성.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 두 수만이 아니라 수열의 전체 원소의 최대공약수를 구하는 함수.
# 수열과 시작 인덱스를 받아서 인덱스가 수열 마지막에 도달하면 해당 값을 반환.
# 참조 값으로 받은 리스트이므로 처음 넣은 리스트 자체가 바뀜.
def gcd_seq(seq, i):
    if i == N - 1:
        return seq[i]

    while seq[i] % seq[i + 1] != 0:
        seq[i], seq[i + 1] = seq[i + 1], seq[i] % seq[i + 1]

    return gcd_seq(seq, i + 1)

# 수빈이가 걸으며 동생을 찾는 함수.
# 시작점과 찾을 대상들을 입력, 시작점과의 차이를 계산해서 저장.
# 이후 수열 최대공약수 계산 함수를 사용해 답을 반환.

def walking(start, target):
    distance = []

    for i in target:
        distance.append(abs(i - start))

    return gcd_seq(distance, 0)

if __name__ == "__main__":
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    print(walking(S, A))