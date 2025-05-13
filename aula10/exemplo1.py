import random
import os

# n = random.randint(1, 5)
# m = random.randint(1, 5)

# os.system('cls')
# print(n, m)

# lst_numeros = [random.randint(1, 10) for i in range(5)]

# print(lst_numeros)

# EXEMPLO 2


def gerar_numero(i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num


ini = int(input('Informe o n° inicial: '))
ult = int(input('Informe o n° final: '))
qtd = int(input('Quanidade de números: '))

numeros = gerar_numero(ini, ult, qtd)
os.system('cls')
print(numeros)
