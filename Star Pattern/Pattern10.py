'''

    * * * * *
     * * * *
      * * *
       * *
        *
'''


n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    # It has the same print statement as Pattern9 but range changed.
    print(" " * (n-i) + "* " * i)
