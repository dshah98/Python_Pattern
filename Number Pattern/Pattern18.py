'''

    1 2 3 4 5 4 3 2 1

'''


n = int(input("Enter Number: "))
for i in range(-n + 1, n):
    print(n - abs(i), end=" ")
    # abs don't allow negative number
