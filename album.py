largpag, altpag = map(int,input().split())# 7 5
l1, a1     = map(int,input().split())# 3 4
l2, a2     = map(int,input().split())# 3 4

# 13 8
# 4 9
# 6 5

#l1=l2;l1=a2;a1l2;a1=a2*.
# if l1 > largpag or l2 > largpag or a1 > largpag or a2 > largpag:
#     print('N')
# else:
# if a1 + a2 > altpag:
if a1 + a2 <= altpag and l1 <= largpag and l2 <= largpag:
    resposta = 'S'
elif a1 + l2 <= altpag and a2 <= largpag and l1 <= largpag:
    resposta = 'S'
elif a2 + l1 <= altpag and l2 < largpag and a1 <= largpag:
    resposta = 'S'
elif l1 + l2 <= altpag and a1 <= largpag and a2 <= largpag:
    resposta = 'S'
elif a1 + a2 <= largpag and l1 <= altpag and l2 <= altpag:
    resposta = 'S'
elif a1 + l2 <= largpag and a2 <= altpag and l1 <= altpag:
    resposta = 'S'
elif a2 + l1 <= largpag and l2 < altpag and a1 <= altpag:
    resposta = 'S'
elif l1 + l2 <= largpag and a1 <= altpag and a2 <= altpag:
    resposta = 'S'
else:
    resposta = 'N'
    #a1 + l2 <= largpag or (a2 + l1 <= altpag or a2 + l1 <= largpag) or (l1 + l2 <= altpag or l1 + l2 <= largpag):
#     print('S')
# elif (a2 + l1 <= altpag or a2 + l1 <= largpag) and (a1 + l2 <= largpag or a1 + l2 <= altpag):
#     print('S')
# elif (l1 + l2 <= altpag or l1 + l2 <= largpag) and (l2 + l1 <= largpag or l2 + l1 <= altpag):
#     print('S')
# else:
#     print('N')
# else:
#     print('S')

print(resposta)