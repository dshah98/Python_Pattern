'''

    * * * * *
    * * * * *
    * * * * *
    * * * * *

'''


n = int(input("Enter Number: "))
for i in range(0, n+1):
    # i is used for row
    for j in range(0, n+1):
        # j is used for column
        print("* ", end="")
    print("")
