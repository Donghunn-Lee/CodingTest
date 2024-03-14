a = input().split('-')
r = sum(map(int, a[0].split('+')))
for i in range(1, len(a)):
    r -= sum(map(int, a[i].split('+')))
print(r)