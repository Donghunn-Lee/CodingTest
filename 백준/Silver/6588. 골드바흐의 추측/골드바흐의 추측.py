# 골드바흐의 추측
import sys
input = sys.stdin.readline
max = 1000000
primes = [True for _ in range(max)]
input_list = []
ans = []
flag = True

for i in range(2, int(max ** 0.5) + 1):
    if primes[i]:
        for j in range(i*2, max, i):
            primes[j] = False


while flag:

    a = int(input())

    if a == 0:
        flag = False
    else:
        input_list.append(a)



for N in input_list:
    b = 0
    if N == 0:
        break

    for a in range(3, N//2 + 1):
        if primes[a]:
            if primes[N - a]:
                ans.append(f'{N} = {a} + {N - a}')
                b = 1
                break
        
    if b == 0:
        ans.append('Goldbach\'s conjecture is wrong.')

sys.stdout.write('\n'.join(ans)+'\n')