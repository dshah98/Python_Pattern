'''

    * * * * *
    * * * *
    * * *
    * *
    *

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    # i is used for row and start with 1
    for j in range(i, n+1):
        # j is used for column
        print("* ", end="")
    print("")
