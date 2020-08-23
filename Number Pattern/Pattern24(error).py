'''

    1 2 3 4 5 4 3 2 1
    1 2 3 4   4 3 2 1
    1 2 3       3 2 1
    1 2           2 1
    1               1

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    for j in range(-n+1, n):
        if n - abs(j) <= i:
            print(n - abs(j), end="")
        else:
            print(" ", end="")
        print("")
    # abs don't allow negative number
