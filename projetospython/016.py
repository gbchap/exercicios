# Interpolação básica de strings (mesma coisa que format)
'''
s - string
d e i - int
f - float
x e X - hexadecimal (0123456789ABCDEF)
'''

nome = 'Gabi'
preço = 1000.957879
variável = '%s, o preço total foi R$%.2f' % (nome, preço)
#'Gabi, o preço total foi R$1000.95'
print(variável)


print('o hexadecimal de %d é %X' % (15, 15)) #o hexadecimal de 15 é F
print('o hexadecimal de %d é %04X' % (15, 15)) #o hexadecimal de 15 é 000F