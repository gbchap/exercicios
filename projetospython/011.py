# Operadores Lógicos pt.1 - AND (todas devem ser true, se não é false)

entrada = input('[E]ntrar  [S]air: ')
if entrada == 'E':
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'
    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrou')
    else:
        print('Não Entrou')
else: 
    print('Não Entrou')
