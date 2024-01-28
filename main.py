# printing a X shape based the input user for seven rows

shape = input('Please enter prefer char for the X shape, thanks \n')
x = 0
y = 6
for row in range(7):
    for col in range(7):
        if row==x and col==y:
            print(shape,end='')
            x+=1
            y-=1
        elif row==col:
            print(shape, end='')
        else:
            print(end=' ')
    print()
