'''

    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1

'''


n = int(input("Enter Number: "))
for i in range(-n+1, n):
    print(str(n - abs(i)) * (n - abs(i)))
    # abs don't allow negative number
