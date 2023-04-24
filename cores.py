r,g,b = map(int,input().split())
lista = [r, g, b]
lista.sort()

if lista[0] >= 0 and lista[0] <= 255 and lista[1] >= 0 and lista[1] <= 255 and lista[2] >= 0 and lista[2] <= 255:
    if lista[2] - lista[1] == lista[1] - lista[0] and lista[2] - lista[1] != 0 and lista[1] - lista[0] != 0:
        print('S')
    elif (lista[0] == 255 and lista[1] == 0 and lista[2] == 0):
        print('S')
    elif (lista[1] == 255 and lista[0] == 0 and lista[2] == 0):
        print('S')
    elif (lista[2] == 255 and lista[1] == 0 and lista[0] == 0):
        print('S')
    elif (lista[0] == 0   and lista[1] == 0 and lista[2] == 0):
        print('S')
    elif (lista[0] == 255 and lista[1] == 255 and lista[2] == 255):
        print('S')
    else:
        print('N')
else:
    print('N')