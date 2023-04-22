#pelo menos um monitor por viagem
#import do módulo math
import math

#Capacidade do Teleférico
capacidade = int(input())
#Quantidade de Alunos
alunos = int(input())
#total de viagens
viagens = math.ceil(alunos/(capacidade - 1))

print(viagens)