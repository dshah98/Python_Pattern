'''

    1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    # i is used for row
    for j in range(1, i+1):
        # j is used for column
        print(i-j+1, end=" ")
    print("")
