# 너무 참신해서 저장
import sys
d = {1: 0, 2: 1}
def s(n: int) -> int:
    if n in d:
        return d[n]
    t = 1 + min(s(n // 3) + n % 3, s(n // 2) + n % 2)
    d[n] = t
    return t
print(s(int(sys.stdin.readline())))