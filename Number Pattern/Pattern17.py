'''

    5 4 3 2 1 0 1 2 3 4 5

'''


n = int(input("Enter Number: "))
for i in range(-n, n+1):
    print(abs(i), end=" ")
    # abs don't allow negative number
