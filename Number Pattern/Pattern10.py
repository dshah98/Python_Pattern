'''

    1 0 0 0 0
    0 2 0 0 0
    0 0 3 0 0
    0 0 0 4 0
    0 0 0 0 5

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    # i is used for row
    for j in range(1, n+1):
        # j is used for column
        if i == j:
            print(i , end=" ")
        else:
            print("0 ", end="")
    print("")
