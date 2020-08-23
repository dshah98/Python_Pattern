'''

    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *

'''


n = int(input("Enter Number: "))
for i in range(-n+1, n):
    print("* " * (n - abs(i)))
    # abs don't allow negative number
