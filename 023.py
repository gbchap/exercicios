# Exercícios

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
''' 
numero = (input('Digite um número inteiro: '))

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
      print('par')
    else:
     print('ímpar')
else:
   print('O número não é inteiro.')
''' 
#para verificar se o número é ou não inteiro, usar .isdigit() que considera
#tudo que não for digito como false
#ou, então, se não usarmos .isdigit(), usar try e except. Mas aí é pra
#testar pontos flutuantes tb (entao a condição do inteiro não é relevante)


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''
entrada = (input('Digite o horário: '))

try:
    horario = int(entrada)

    bom_dia = 0 <= (horario) < 12
    boa_tarde = 11 < (horario) < 18
    boa_noite = 17 < (horario) <= 23
    
    if bom_dia:
        print('Bom dia!')
    elif boa_tarde:
        print('Boa tarde!')
    elif boa_noite:
        print('Boa noite!')
    else:
        print('Coloque um horário válido!')
except: 
    print('Por favor, digite um número inteiro.') #ou seja, daria erro (não inteiro)
    
'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
'''
nome = input('Digite seu primeiro nome: ')
tam_nome = len(nome)

if 1 < tam_nome:
    if tam_nome <= 4:
        print('Seu nome é curto.')
    elif 4 < tam_nome <= 6:
        print('Seu nome é médio.')
    else:
        print('Seu nome é grande.')
else:
    print('Escreva mais de uma letra.')
'''