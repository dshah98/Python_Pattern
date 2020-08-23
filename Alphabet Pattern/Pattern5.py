'''

   A
   B A
   C B A
   D C B A
   E D C B A
'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(chr(j + 64), end="")
    print("")

