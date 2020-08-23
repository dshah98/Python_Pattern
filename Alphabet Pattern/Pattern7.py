'''

         A
       A B A
     A B C B A
   A B C D C B A

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(-i+1, i):
        print(chr(i - abs(j) + 64), end="")
    print("")
