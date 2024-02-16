# 요세푸스 문제
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
josephus_per = [i for i in range(1, N + 1)]
result = []
i = K

while josephus_per:
    while i > len(josephus_per):
        i -= len(josephus_per)
    
    result.append(str(josephus_per.pop(i-1)))
    i += K-1




print('<',end='')
print(', '.join(result), end='')
print('>')
