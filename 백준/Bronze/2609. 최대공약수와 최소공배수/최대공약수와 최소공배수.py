# 최대공약수와 최소공배수

A, B = map(int, input().split())

def cal_gcd(a, b):
    if a % b == 0:
        return b
    elif a !=0 and b!=0:
        return cal_gcd(b, a % b)
    else:
        return 1

if A != B:
    gcd = cal_gcd(max(A, B), min(A, B))
else:
    gcd = A


lcm = A * B // gcd
print(gcd)
print(lcm)