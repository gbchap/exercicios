# calculadora utilizando o comando while

while True:
    N1 = input('Digite o primeiro número: ')
    N2 = input('Digite o segundo número: ')
    
    nmrs_validos = None
    try:
        N1_float = float(N1)
        N2_float = float(N2)
        nmrs_validos = True
        
    except:
        nmrs_validos = None
        
    if nmrs_validos is None:
        print('Por favor, digite apenas números.')
        continue
        
        
    SOMA = N1_float + N2_float
    SUB = N1_float - N2_float
    MULTI = N1_float * N2_float
    DIV = N1_float / N2_float
    
    OP = input('Qual será o operador? (+, -, x ou :) ')
        
    if OP == '+':
        print(SOMA)
    elif OP == '-':
        print(SUB)
    elif OP == 'x':
        print(MULTI)
    elif OP == ':':
        print(DIV)
    else:
        print('Digite um operador válido, por favor.')
            
            
        sair = input('Quer sair? (s/n): ').lower().startswith('s')
        while True:
            if sair is True:
                print('Você saiu.')
                break
        

    
    
    
    