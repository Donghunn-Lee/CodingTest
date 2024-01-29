from sys import stdin, stdout

input = stdin.readline

n = int(input())

output = []

for _ in range(n) :
    tmp = map(lambda x : x[::-1], input().split())
    output.append(' '.join(tmp))

print('\n'.join(output))