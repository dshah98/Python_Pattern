'''

    1
    1 0
    1 0 1
    1 0 1 0
    1 0 1 0 1

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    # i is used for row
    for j in range(1, i+1):
        # j is used for column
        print(j % 2, end=" ")
    print("")
