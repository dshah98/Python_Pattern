'''

    A b C d E f G h

'''


n = int(input("Enter Number: "))
for i in range(1, n+1):
    if i % 2:
        print(chr(i + 64), end=" ")
    else:
        print(chr(i + 96), end=" ")
