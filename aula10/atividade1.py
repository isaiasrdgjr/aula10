import random
import os


def somar(n1, n2):
    s = n1 + n2
    return s


def subtrair(n1, n2):
    sub = n1 - n2
    return sub


def multiplicar(n1, n2):
    m = n1 * n2
    return m


def dividir(n1, n2):
    d = n1/n2
    return d


os.system('cls')
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
sinal = input('Informe o sinal de cálculo: ')

match sinal:
    case '+':
        soma = somar(num1, num2)
        print(f'Soma = {soma:.2f}')

    case '-':
        subtracao = subtrair(num1, num2)
        print(f'subtração = {subtracao:.2f}')

    case '*':
        multiplicacao = multiplicar(num1, num2)
        print(f'multiplicação = {multiplicacao:.2f}')

    case '/':
        divisao = dividir(num1, num2)
        print(f'divisão = {divisao:.2f}')

    case _:
        print('Informe um sinal válido! ')
