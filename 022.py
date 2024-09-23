"""
Flag = bandeira (marca um local)
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
    is é tipo ==, usado mto com "None"
id = identidade

v1 = 'a'
v2 = 'a'
print(id(v1)) 
print(id(v2)) #mesmo id pra ambos

"""

'''
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) #None True
print(passou_no_if, passou_no_if is not None) #None False
'''

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
    
'''
print(passou_no_if, passou_no_if is None) #True False
print(passou_no_if, passou_no_if is not None) #True True 
'''

if passou_no_if is None:
    print('Não passou no if.')

if passou_no_if is not None:
    print('Passou no if.')