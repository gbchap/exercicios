# Operadores Lógicos pt.3 - NOT (inverter expressões)
# not False == True
# not True == False


# Checador de senha:

senha = input('Digite sua senha: ')

if (senha != 'bomestaremcasa') and (senha != ''):
    print('Senha incorreta.')
if senha == 'bomestaremcasa':
    print('Senha correta.')
if not senha:
    print('Você não digitou nada.')

