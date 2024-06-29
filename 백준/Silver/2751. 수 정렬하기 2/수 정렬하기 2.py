# 수 정렬하기 2

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    seq = sorted([int(input()) for _ in range(N)])
    print("\n".join(map(str, seq)))