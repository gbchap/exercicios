# Operadores Lógicos pt.2 - OR (qualquer true define true)
#None = não valor
'''

entrada = input('[E]ntrar  [S]air: ')
if entrada == 'E' or 'e':
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'
    if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
        print('Entrou')
    else:
        print('Não Entrou')
else: 
    print('Não Entrou')
'''

# Avaliação de Curto circuito:
senha = input('Senha: ') or 'Sem Senha'
print(senha)
