#Introdução ao try/except
'''
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

int('a') #ValueError: invalid literal for int() with base 10: 'a'
float('a') #ValueError ValueError: could not convert string to float: 'a'
'''

'''
numero = input('Vou dobrar o número que você digitar:')
if numero.isdigit():
    print(f'O dobro de {numero} é {float(numero) * 2:.2f}')
else:
    print('Isso não é um número.')

# tem que transformar em float antes de fazer a conta, se não
# os resultados serão incorretos. Input sempre retorna uma string.

'''

# Utilizando try/except nesses códigos:

numero = input('Vou dobrar o número que você digitar:')
try:
    print(f'O dobro de {numero} é {float(numero) * 2:.2f}')
except:
    print('Isso não é um número.')
    
