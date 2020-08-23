'''

    1             1
    1 2         2 1
    1 2 3     3 2 1
    1 2 3 4 4 3 2 1

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print(" " * (n-i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print("")
    # abs don't allow negative number
