'''

    PATTERN
    * * * * * * * .....
    Same as numbers.

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    # Start with 1 and continues to the number entered adding 1 everytime.
    print("*", end=" ")
