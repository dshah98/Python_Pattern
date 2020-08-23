'''

    1 1 1 1 1 1
    1 1 1 1 2 2
    1 1 1 3 3 3
    1 1 4 4 4 4
    1 5 5 5 5 5

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    print("1 " * (n-i) + (str(i) + " ") * i)
