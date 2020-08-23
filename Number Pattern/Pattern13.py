'''

    1 2 3 4
     2 3 4
      3 4
       4
       4
      3 4
     2 3 4
    1 2 3 4

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    print(" " * (i-1), end="")
    for j in range(i, n+1):
        print(j, end=" ")
    print("")
for i in range(n, 0, -1):
    print(" " * (i-1), end="")
    for j in range(i, n+1):
        print(j, end=" ")
    print("")
