# 최빈수 구하기
from collections import Counter

n = int(input())
score = [[0 for j in range(2)] for i in range(n)]

for i in range(n) :
    score[i][0] = int(input())
    score[i][1] = Counter(input().split()).most_common(1)

for j in range(n) :
    print('#{0} {1}'.format(score[j][0], int(score[j][1][0][0])))


