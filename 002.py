'''
Estudo com format / imc
'''

nome = str(input('Nome:'))
altura = float(input('Altura em m:'))
peso = int(input('Peso em kg:'))

imc = peso / altura ** 2

linha_1 = f'Olá {nome}! Você tem {altura:.2f} metros de altura e seu peso é de'
linha_2 = f'{peso} kg. Seu IMC é, portanto, {imc}'

print(linha_1)
print(linha_2)