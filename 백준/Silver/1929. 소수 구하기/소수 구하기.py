#소수 구하기

import sys

M, N = map(int, sys.stdin.readline().split())

eratosthenes = [False] + [True] * ((N - 1) // 2)

for i in range(1, int(N ** 0.5)):
    if eratosthenes[i]:
        eratosthenes[2 * i * (i + 1)::i * 2 + 1] = [False] * ((((N + 1) // 2) - i * i * 2) // (i * 2 + 1))

if M <= 2:
    sys.stdout.write("2\n")
sys.stdout.write('\n'.join([f'{x}' for x, val in zip(range(M+(M & 1 == 0), N + 1, 2), eratosthenes[M // 2:]) if val]))
