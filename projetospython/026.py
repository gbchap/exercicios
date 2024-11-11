# exercício guiado com while: iterando strings com while
#fazer uma nova string com while, iteração de asteriscos entre os índices.

''' 
nome = 'Nome Próprio' #strings são iteráveis
print(nome)
tamanho_nome = print(len(nome))
print(nome[3])
''' 
nome = 'Nome Próprio'
novo_nome = ''
nmr_letras = len(nome)

nmr = 0

while nmr < len(nome):
        
    letra = nome[nmr]
    novo_nome += letra
    nmr += 1
    novo_nome += '*'  
    
print(novo_nome)
    

