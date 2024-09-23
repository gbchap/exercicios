
#Variáveis, constantes e complexidade de código
'''
- CONSTANTE -> "variáveis" que vão mudar

- evitar muitas condições no mesmo if

-           <- mais espaços = código complexo. Em programação, isso
é ruim.

'''
velocidade = 61 #constante durante toda a trajetória
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_passa_r1 = velocidade > RADAR_1
carro_passa_r1 = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)
velocidade_npassa_r1 = velocidade >= RADAR_1
carro_passou_r1 = (LOCAL_1 + RADAR_RANGE) < local_carro

if velocidade_passa_r1:
    print(f'A velocidade de {velocidade}km/h\
 do carro é maior do que a permitida.')
else:
    print(f'A velocidade de {velocidade}km/h\
 do carro é permitida.')
    
if carro_passa_r1:
    print('O carro passa pelo radar.')
elif carro_passou_r1:
    print('O carro passou pelo radar.')
else:
    print('O carro ainda não passou pelo radar.')

if (carro_passa_r1 or carro_passou_r1) and velocidade_passa_r1:
    print('O carro foi multado em radar 1.')

if (carro_passa_r1 or carro_passou_r1) and not velocidade_passa_r1:
    print('O carro não foi multado em radar 1.')