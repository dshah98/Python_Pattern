'''

    5 5 5 5 5
    4 5 5 5 5
    3 4 5 5 5
    2 3 4 5 5
    1 2 3 4 5

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j+n-i, end="")
    print(str(n) * (n-i))
