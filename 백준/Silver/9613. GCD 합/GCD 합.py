# GCD 합
import sys
input = sys.stdin.readline

def cal_gcd(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b

def sum_gcd(seq):
    tmp_sum = 0

    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            tmp_sum += cal_gcd(seq[i], seq[j])
    
    return tmp_sum

        

if __name__ == "__main__":
    t = int(input())
    ans = []

    for i in range(t):
        n, *seq = map(int, input().split())
        ans.append(sum_gcd(seq))
    
    print('\n'.join(map(str, ans)))


    