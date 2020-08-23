'''

    5 5 5 5 5
    5 4 4 4 4
    5 4 3 3 3
    5 4 3 2 2
    5 4 3 2 1

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(i if i >= j else j, end="")
    print("")
