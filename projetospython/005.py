
# if /    elif   / else
# se / se não se / se não

entrada = input('Você quer entrar ou sair?')

if entrada == 'entrar':
    print('você entrou no sistema')
elif entrada == 'sair':
    print('você saiu do sistema')
else:
    print('digite "entrar" ou "sair".')


# if/else são padrão. Se não tiver elif,
# então td que não for if vai ser else.
# Sempre há 1 if e 1 else, mas
# podem ter vários elif.

