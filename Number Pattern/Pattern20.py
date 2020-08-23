'''

    4
    3 4 3
    2 3 4 3 2
    1 2 3 4 3 2 1
    2 3 4 3 2
    3 4 3
    4

'''


n = int(input("Enter Number: "))
for i in range(-n+1, n):
    t = n - abs(i)
    for j in range(-t + 1, t):
        print(n - abs(j), end="")
    print("")
    # abs don't allow negative number
