'''

    Aa
    BbBb
    CcCcCc
    DdDdDdDd

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(j + 64) + chr(j + 96), end="")
    print("")
