T = int(input())
Base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for t in range(1, T + 1):
    init_text = input()
    bits = str()
    Ascii = str()
    tmp = str()
    for i in init_text:
        c = bin(Base64.index(i))
        bits += "0"*(8-len(c)) + c[2:]

    for j in range(len(bits)):
        tmp += bits[j]
        if j % 8 == 7:
            Ascii += chr(int(tmp, 2))
            tmp = str()
    print(f"#{t} {Ascii}")