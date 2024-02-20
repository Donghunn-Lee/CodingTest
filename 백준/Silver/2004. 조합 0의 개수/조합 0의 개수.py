# 조합 0의 개수

n, m = map(int, input().split())

def countNum(n , t):
    count = 0

    while n != 0:
        count += n // t
        n //= t
    return count


count_2 = countNum(n, 2) - countNum(n - m, 2) - countNum(m, 2)
count_5 = countNum(n, 5) - countNum(n - m, 5) - countNum(m, 5)

print(min(count_2, count_5))