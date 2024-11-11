# Formatação básica com f-strings
'''
s - string
d - int
f - float
x ou X - hexadecimal
.<numero de digitos>
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
ex.: 0>-100, .1f
conversion flags - !r !s !a (não esquentar por enquanto)
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')

#ABC
#       ABC 
#ABC       .
#   ABC  

print(f'{1000.9182747:.1f}') #1000.9   
print(f'{1000.9182747:,.1f}') #1,000.9   
print(f'O hexadecimal de 1500 é {1500:08X}') #O hexadecimal de 1500 é 000005DC




