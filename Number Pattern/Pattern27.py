'''

    1 2 3 4 5
    2 3 4 5 1
    3 4 5 1 2
    4 5 1 2 3
    5 1 2 3 4

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(i, n+i):
        print((j-1) % n + 1, end="")
    print("")
