'''

          7
         6 6
        5 5 5
       4 4 4 4
      3 3 3 3 3
     2 2 2 2 2 2
    1 1 1 1 1 1 1

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    # i is used for row
    print(" " * (i-1), end="")
    for j in range(i, n+1):
        # j is used for column
        print(i, end=" ")
    print("")
