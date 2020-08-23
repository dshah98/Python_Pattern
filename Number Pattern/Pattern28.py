'''

    1 3 5 7
    3 5 7 1
    5 7 1 3
    7 1 3 5

'''


n = int(input("Enter Number: "))
n = n*2
for i in range(1, n+1, 2):
    for j in range(i, n+i, 2):
        print((j-1) % n + 1, end="")
    print("")
