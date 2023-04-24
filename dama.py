#tabuleiro 8x8, portanto,64 casas.
lista = []
cond = True

while cond:
    x1,y1,x2,y2 = map(int,input().split())
    if(x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0):
        cond = False
    else:
        if(x1 == x2 and y1 == y2):
            lista.append(0)
        elif x1 == x2 or y1 == y2:
            lista.append(1)
        elif x1 + y1 == x2 + y2:
            lista.append(1)
        elif x1+y1 == 2 and x2 + y2 == 4:
            lista.append(1)
        elif x1-y1 == x2-y2:
            lista.append(1)
        else:
            lista.append(2)
for x in lista:
    print(x)




    #       	    1	2	3	4	5	6	7	8
    
    
    #         1	    2	3	4	5	6	7	8	9
    #         2	    3	4	5	6	7	8	9	10
    #         3	    4	5	6	7	8	9	10	11
    #         4	    5	6	7	8	9	10	11	12
    #         5	    6	7	8	9	10	11	12	13
    #         6	    7	8	9	10	11	12	13	14
    #         7	    8	9	10	11	12	13	14	15
    #         8	    9	10	11	12	13	14	15	16
