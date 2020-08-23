'''

          *
        * * *
      * * * * *
    * * * * * * *

'''


n = int(input("Enter Number: "))*2
for i in range (1, n+1, 2):
    print(" " * (n-i-1) + "* " * i)
