largpag, altpag = map(int,input().split())
l1, a1     = map(int,input().split())
l2, a2     = map(int,input().split())

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

print(resposta)