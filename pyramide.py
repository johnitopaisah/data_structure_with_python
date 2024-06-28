r = 8
if r%2 != 0:
    print(' '*((r//2)+5), '*', end='')
for i in range(r):
    print(' '*(r-i+1),'*'*(i*2))