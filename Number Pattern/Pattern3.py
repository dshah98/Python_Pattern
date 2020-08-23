'''

    PATTERN
    ....10 9 8 7 6 5 4 3 2 1

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    # (start, stop, step)
    # Start with the entered number and decreases to 0
    print(i, end=" ")
