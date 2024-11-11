'''
Estudo com f-string / imc
'''

nome = input('Nome:')
altura = input('Altura em m:')
peso = input('Peso em kg:')

str_nome = str(nome)
fl_altura = float(altura)
int_peso = int(peso)

imc = peso / altura ** 2

linha_1 = f'Olá {nome}! Você tem {altura:.2f} metros de altura e seu peso é de'
linha_2 = f'{peso} kg. Seu IMC é, portanto, {imc}'

print(linha_1)
print(linha_2)