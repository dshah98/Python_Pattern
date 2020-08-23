'''

    *
    # #
    * * *
    # # # #
    * * * * *

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    if i % 2:
        print("* "*i)
    else:
        print("# "*i)
