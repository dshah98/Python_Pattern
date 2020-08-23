'''

   A
   b B
   C c C
   d D b D
   E e E e E

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(chr(i + (32 * (3 - j % 2))), end=" ")
    print("")

