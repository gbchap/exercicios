# Fatiamento de strings:
'''
como visto antes, há índices negativos e pos:
 012345678
 olá mundo
-987654321
fatiamento [i:f:p] [::]
obs.: a função len retorna a qtd de caracteres da str

variavel = "olá mundo"
print(variavel[5]) #u
print(variavel[-4]) #u
'''

variavel = "olá mundo"
print(variavel[4:]) #mundo
print(variavel[4:8]) #mund  (índice final não incluso)
print(variavel[:5]) #olá m
# omissão = início ou fim dependendo

# função len conta caracteres
print(len(variavel)) #9 (conta com o 0)
print(len(variavel[3])) #1


print(variavel[0:9:1]) #OU print(variavel[0:len(variavel):1)
#olá mundo
#(0 é o inicio, 9 o fim, e a leitura será de 1 em 1)

print(variavel[0:9:2])
#oámno
#(0 é o inicio, 9 o fim, e a leitura será de 2 em 2)

print(variavel[::-1]) 
#odnum álo
#:: é a mesma coisa de [-1:-10:-1]. Inverte a string inteira.