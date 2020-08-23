'''

    A B C D E
     B C D E
      C D E
       D E
        E

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    print(" " * (i-1), end="")
    for j in range(i, n+1):
        print(chr(j + 64), end=" ")
    print("")
