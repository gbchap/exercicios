#calculadora básica:
N1 = float(input('Digite o primeiro núabcmero: '))
N2 = float(input('Digite o segundo número: '))
OP = input('Qual será o operador? (+, -, x ou :) ')
SN = input('Mais operadores? (s/n) ')

if SN == 's':
    ME = input('Módulo(m), Exponencial(e) ou voltar(v)? ')
    if ME == 'm':
        print(N1 % N2)
    elif ME == 'e':
        print(N1 ** N2)
    else:
        SN = input('Mais operadores? (S/N) ')
        
else: 
    SOMA = N1 + N2
    SUB = N1 - N2
    MULTI = N1 * N2
    DIV = N1 / N2

    if OP == '+':
        print(SOMA)
    elif OP == '-':
        print(SUB)
    elif OP == 'x':
        print(MULTI)
    elif OP == ':':
        print(DIV)
    else:
        print('Digite um operador válido, por favor.')


    