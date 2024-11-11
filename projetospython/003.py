cat_op = float(input('valor do cateto 1:'))
cat_adj = float(input('valor do cateto 2:'))

hip = (cat_op ** 2 + cat_adj ** 2) ** (1/2)

print(f'o valor da hipotenusa será {hip:.2f}')
#ou {hip:.2f}
#ou {(round(hip, 2))}