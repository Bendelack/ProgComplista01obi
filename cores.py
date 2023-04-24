r,g,b = map(int,input().split())

if r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255:
    if b - g == g - r and b - g != 0 and g - r != 0:
        print('S')
    elif (r == 255 and g == 0 and b == 0):
        print('S')
    elif (g == 255 and r == 0 and b == 0):
        print('S')
    elif (b == 255 and g == 0 and r == 0):
        print('S')
    elif (r == 0   and g == 0 and b == 0):
        print('S')
    elif (r == 255 and g == 255 and b == 255):
        print('S')
    else:
        print('N')
else:
    print('N')