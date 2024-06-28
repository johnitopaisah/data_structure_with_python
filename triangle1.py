height = int(input("Enter the heigth of the triangle: "))

for row in range(1, height+1):
    if row <= (height//2):
        print('* '*(row), end=' ')
    else:
        print('* '*(height-row+1), end=' ')
    print()

# height = int(input("Enter the heigth of the triangle: "))

# for row in range(1, height+1):
#     if row <= (height//2):
#         print('* '*(row), end=' ')
#     else:
#         print(' '*(height-row+1), end=' ')
#     print()