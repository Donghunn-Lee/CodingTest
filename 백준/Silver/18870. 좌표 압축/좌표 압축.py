# 좌표 압축
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    sorted_seq = sorted(set(seq))

    compressioned = dict()

    for i in range(len(sorted_seq)):
        compressioned[sorted_seq[i]] = i
    
    for i in range(N):
        seq[i] = compressioned[seq[i]]
    
    print(" ".join(map(str, seq)))