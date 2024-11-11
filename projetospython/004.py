import math
a = int(input('valor do cateto 1:'))
b = int(input('valor do cateto 2:'))
x = math.hypot(a, b)

print('utilizando o cateto 1 com o valor {} e o cateto 2 com o valor {},'.format(a, b))
print('o valor da hipotenusa será {}'.format(x))