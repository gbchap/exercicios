#criador de senhas aleatórias
import random

confirmacao = input('vamos gerar a senha? s/n:' )
if confirmacao == 's':
    True
else:
    False
        
lista_senhas = ['']

while confirmacao == True:
    numeros = random.randint(0,9)
    letras_min = 
    letras_mai =
    caracteres = random.choices['!', '@', '#','$', '%', '¨', '&', '*', '?']
    senha = f'{numeros}, {letras_min}, {letras_mai}, {caracteres}'
    random.shuffle(senha)
    
    if senha in lista_senhas:
        #nao adicionar á lista de senhas
    else:
        #adicionar á lista de senhas
    print(senha)
    print(lista_senhas)
    
'''
o unico problema do codigo é que terao apenas numeros pre definidos de cada caractere.
O objetivo é deixar a senha mais aleatorizada possiel, o que talvez nao funcione 
com o uso de f-strings para definir os conteudos da senha, mesmo com 
a presença do comando shuffle depois.

uma solução seria utilizar o comando choices mas isso faria necessario a criação
de variaveis listando os numeros de 0 a 9.
'''