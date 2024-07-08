"""
condição = True

if condição:
    print('Este é o código do if')

código é executado.
"""
"""
condição = False

if condição:
    print('Este é o código do if')

código nao é executado.
"""

condição = False

if condição:
    print('Este é o código do if')
else:
    print('Este é o código do else')

condição1 = False
condição2 = True
condição3 = True
condição4 = False

if condição1:
    print('código da condição 1')
elif condição2:
    print('código da condição 2')
    print('código da condição 2.2')
elif condição3:
    print('código da condição 3')
elif condição4:
    pass
else:
    print('sem condições.')
# código da condição 3 não é executada, porque está embaixo.
# existe uma ordem!

if 10 == 10:
    print('outro if')
