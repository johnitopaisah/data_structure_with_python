height = int(input("Enter the heigth of the triangle: "))

for row in range(1, height+1):
    if row <= (height//2):
        print('* '*(row))
    else:
        print('* '*(height-row+1))
