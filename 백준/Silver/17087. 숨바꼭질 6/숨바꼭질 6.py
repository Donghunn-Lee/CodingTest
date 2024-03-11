# 숨바꼭질 6

# 최대 공약수를 계산해야하는 문제인 줄 몰랐음.
# 처음 제출했던 방식은 시작점과 전체 점들 중 두 수의 차의 절댓값을 모두 구하고
# 그 중 가장 적은 것을 기준으로 1씩 빼가가며 반복,
# 그 안에서 target과 거리를 같이 증가시켜가면서 계산했서 답은 도출했으니 당연히 시간초과가 나왔음.
# 찾아보니 최대공약수라는 단어만 보고 깨달아서 아래 코드를 다시 작성.

import sys
input = sys.stdin.readline

# 최대공약수 계산 함수.
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

# 수빈이가 걸으며 동생을 찾는 함수.
# 시작점과 찾을 대상들을 입력, 시작점과의 차이를 계산해서 저장.
# 이후 두 수의 최대공약수를 구하고, 그 결과와 다음 수의 최대공약수를 다시 계산하여 최종 result를 반환.

def walking(start, target):
    distance = []

    for i in target:
        distance.append(abs(i - start))

    result = distance[0]

    for i in range(1, len(distance)):
        result = gcd(result, distance[i])

    return result

if __name__ == "__main__":
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    print(walking(S, A))