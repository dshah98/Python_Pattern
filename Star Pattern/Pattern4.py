'''

    *
    * *
    * * *
    * * * *
    * * * * *

'''


n = int(input("Enter Number: "))
for i in range(0, n+1):
    # i is used for row
    for j in range(0, i+1):
        # j is used for column
        # This will loop according to i every time.
        # It will come to the new line as many time i will be executed with +1 star [ * ].
        print("* ", end="")
    print("")
