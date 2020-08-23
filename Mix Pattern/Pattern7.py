'''

         *
        1 2
       * * *
      1 2 3 4
     * * * * *
    1 2 3 4 5 6

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    if i % 2 == 1:
        print("* " * i)
    else:
        for j in range(1, i+1):
            print(j, end=" ")
        print("")
