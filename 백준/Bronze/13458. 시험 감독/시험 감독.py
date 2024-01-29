import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
b,c = map(int, input().rstrip().split())
answer = 0

for i in a :
    if b > c :
        if i > c :
            if i > b :
                if (i-b) % c != 0 :
                    answer += (i-b)//c + 2
                else :
                    answer += (i-b)//c + 1
            else : answer += 1
        else : answer += 1
    else : 
        if (i-b) % c != 0 :
            answer += (i-b)//c + 2
        else :
            answer += (i-b)//c + 1
        
print(answer)