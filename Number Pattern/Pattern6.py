'''

    5
    4 5
    3 4 5
    2 3 4 5
    1 2 3 4 5

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    # i is used for row
    for j in range(i, n+1):
        # j is used for column
        print(j, end=" ")
    print("")
