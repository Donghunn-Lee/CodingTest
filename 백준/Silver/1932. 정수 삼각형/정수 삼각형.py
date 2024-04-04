import sys

def solve(N,seq):
    pt = N - 1
    for _ in range(N-1):
        last = seq.pop()
        for i in range(pt):
            seq[pt - 1][i] += max(last[i], last[i + 1])
        pt -= 1
    
    print(seq[0][0])

N = int(sys.stdin.readline())
seq = []
for _ in range(N):
    seq.append(list(map(int,sys.stdin.readline().split())))

solve(N,seq)