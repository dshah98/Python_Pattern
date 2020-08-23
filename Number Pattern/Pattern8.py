'''

    1 2 3 4 5 6 7
     1 2 3 4 5 6
      1 2 3 4 5
       1 2 3 4
        1 2 3
         1 2
          1

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    # i is used for row
    print(" " * (n-1), end="")
    for j in range(1, i+1):
        # j is used for column
        print(j, end=" ")
    print("")
