# 간단한 369게임

n = int(input())
output = ''
for i in range(1, n + 1):
    count = 0
    for j in str(i):
        if int(j) % 3 == 0 and int(j) != 0:
            count += 1
    if count != 0:
        output += count*'-' + ' '
    else:
        output += str(i) + ' '
print(output)

