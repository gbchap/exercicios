# Outros operadores - in e not in
# Strings são iteráveis (navegável item por item)
# 0 1 2 3 4
# P u d i m
#-5-4-3-2-1

'''
nome = 'Pudim'
print(nome[-1]) #m
print(nome[4]) #m
print(nome[0]) #P (maiúsculo)

print('u' in nome) #True
print('dim' in nome) #True
print(10 * '-')
print('z' in nome) #False
print('up' in nome) #False
print('dim' not in nome) #False
'''
nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')    