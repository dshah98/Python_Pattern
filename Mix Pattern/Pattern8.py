'''

    A 1 1 1 1
    0 B 1 1 1
    0 0 C 1 1
    0 0 0 D 1
    0 0 0 0 E

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    print("0 " * (i-1) + chr(i+64) + " " + "1 " * (n-i))
