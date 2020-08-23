'''

    * 4 * 16 * 32 *

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    if i % 2 == 1:
        print("*", end=" ")
    else:
        print(i * i, end=" ")
