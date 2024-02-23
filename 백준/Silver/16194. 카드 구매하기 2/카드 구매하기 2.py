# 카드 구매하기 2

N = int(input())

cardCosts = [0] + list(map(int, input().split()))

def minPrice (n):
  for i in range(2, n + 1):
    for j in range(1, i // 2 + 1):
      tmp = cardCosts[i - j] + cardCosts[j]
      if tmp < cardCosts[i]:
        cardCosts[i] = tmp
  return cardCosts[n]

print(minPrice(N))
