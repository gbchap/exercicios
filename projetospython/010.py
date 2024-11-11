# Exercício if/else/elseif
primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')


maior = primeiro_valor >= segundo_valor
if maior == True:
    print(f'{primeiro_valor} é maior ou igual a {segundo_valor}')
else:
    print(f'{segundo_valor} é maior do que {primeiro_valor}')
    
    
"""
solução:

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual a {segundo_valor=})
else:
    print(f'{segundo_valor=} é maior que {primeiro_valor=})
"""