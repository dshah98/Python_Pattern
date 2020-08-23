'''

   A
   A B
   A B C
   A B C D
   A B C D E

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(j + 64), end="")
    print("")

