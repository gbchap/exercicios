# Operadores Lógicos pt.3 - NOT (inverter expressões)
# not False == True
# not True == False

senha = input('Digite sua senha: ')

if (senha != '1234') and (senha != ''):
    print('Senha incorreta.')
if senha == '1234':
    print('Senha correta.')
if not senha:
    print('Você não digitou nada.')