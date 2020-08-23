'''

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1

'''


n = int(input("Enter Number: "))
for i in range(-n+1, n):
    t = n - abs(i)
    for j in range(1, t+1):
        print(j, end="")
    print("")
    # abs don't allow negative number
