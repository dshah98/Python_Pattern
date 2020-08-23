'''

    * * * * *
      * * * *
        * * *
          * *
            *

'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    # (start, stop, step)
    print(" " * (n-i) + "*" * i)

