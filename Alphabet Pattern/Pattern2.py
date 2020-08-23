'''

    G F E D C B A

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    print(chr(i + 64), end=" ")
    # abs don't allow negative number
