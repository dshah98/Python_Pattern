'''

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    # i is used for row
    for j in range(1, i+1):
        # j is used for column
        # This will loop according to i every time.
        # It will come to the new line as many time i will be executed with +1 number.
        # Pattern11 and Pattern12 have same structure, the only change is at print according to columns.
        print(j, end=" ")
    print("")
