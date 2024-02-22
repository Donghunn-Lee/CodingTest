N = int(input())
card = [0] + list(map(int, input().split()))
price = {1 : card[1]}

def DP (n) :
    if n <= 0:
        return 0
    
    if n in price:
        return price[n]
    
    tmp = 0

    for i in range(1, n):
        tmp = max(tmp, DP(n - i) + DP(i))

    price[n] = max(tmp, card[n])
    
    return price[n]

print(DP(N))