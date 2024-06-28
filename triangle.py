heigth = int(input("Enter the heigth of the triangle: "))

first_half = heigth//2
sec_half = heigth - first_half

for i in range(1, first_half+1):
    for j in range(1, i+1):
        print("*", end=' ')
    print()
for i in range(sec_half, 0, -1):
    for j in range(1, i+1):
        print("*", end=' ')
    print()
