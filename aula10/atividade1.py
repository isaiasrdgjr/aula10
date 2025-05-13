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
num1 = float(input('Informe o número: '))
sinal = input('Informe o sinal de cálculo: ')
num2 = float(input('Informe o número: '))


if sinal == '+':
    soma = somar(num1, num2)
    print(f'Soma = {soma:.2f}')

elif sinal == '-':
    subtracao = subtrair(num1, num2)
    print(f'subtração = {subtracao:.2f}')

elif sinal == '*':
    multiplicacao = multiplicar(num1, num2)
    print(f'multiplicação = {multiplicacao:.2f}')

elif sinal == '/':
    divisao = dividir(num1, num2)
    print(f'divisão = {divisao:.2f}')

else:
    print('Digite um sinal válido!')
