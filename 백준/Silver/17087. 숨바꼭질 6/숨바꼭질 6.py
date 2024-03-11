from math import gcd
n,x  = map(int, input().split())
a_list = [abs(i-x) for i in map(int, input().split())]
print(gcd(*a_list))