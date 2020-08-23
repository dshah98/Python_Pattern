'''

    1 2 3 4 5 4 3 2 1
    2 3 4 5 4 3 2
    3 4 5 4 3
    4 5 4
    5

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(-n+i, n-i+1):
        print(n-abs(j), end="")
    print("")
