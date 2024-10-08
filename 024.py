'''
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
o break quebra o looping do while.
'''

''' 
condicao = True 
while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break 

print('Acabou.') #Seu nome é sair Acabou.
#Só aparece acabou porque o código 'quebra'.
''' 

'''
contador = 0

while contador < 10:
    contador = contador + 1 
    print(contador)

print('Acabou')
'''

#1
#2     
#3     
#4     
#5     
#6     
#7     
#8     
#9     
#10    
#Acabou

#Mas se fizermos assim:
'''
contador = 0

while contador < 10:
     print(contador)
     contador = contador + 1 
    
print('Acabou')
'''
#0
#1     
#2     
#3     
#4     
#5     
#6     
#7     
#8     
#9     
#Acabou

'''
operadores de atribuição:
= += -= *= /= (divisão sempre retorna float) //= (divisao inteira) **= (potenciação) %= (módulo)

ou seja, contador = contador + 1
e contador += 1 são a mesma coisa.

vamos substituir "contador" para "str" para ficar
menos confuso.

assim como:

str -= 1 
str = str - 1

str *=
str = str * 1

etc


str = 10

str = str - 1
print(str) #9

'''

# while + continue

contador = 0

while contador <= 100: 
     contador += 1 
     
     if contador == 6:
         print(f'não vou mostrar o {contador}')
         continue
     
     if contador >= 10 and contador <= 27:
         print(f'não vou mostrar o {contador}')
         continue

     print(contador)
     
     if contador == 40:
         break
     
    
print('Acabou')



