# 골드바흐의 추측
import sys
input = sys.stdin.readline
max = 1000000
primes = [True for _ in range(max)]
# ans = []

for i in range(2, int(max ** 0.5) + 1):
    if primes[i]:
        for j in range(i*2, max, i):
            primes[j] = False
            
while True:
    N = int(input())
    b = 0
    if N == 0:
        break

    for a in range(3, N):
        if primes[a]:
            if primes[N - a]:
                print(f'{N} = {a} + {N - a}')
                b = 1
                break
        
    if b == 0:
        print('Goldbach\'s conjecture is wrong.')

