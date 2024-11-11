#questão de teste muito interessante:
numero = int(input('Escreva um número: '))
 
if numero >= 1:
    if numero >= 2:
        if numero >= 3:
            print('Número maior/igual a 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')