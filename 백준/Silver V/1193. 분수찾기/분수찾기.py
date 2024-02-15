x=int(input())

s=0
i=0
while x>s:
    i+=1
    s+=i

s=s-i
if i%2==1:
    a=i-(x-s)+1
    b=x-s
else:
    a=x-s
    b=i-(x-s)+1

print(f'{a}/{b}')