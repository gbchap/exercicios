# Projeto python (curso 1)
# Automação de preenchimento de dados em determinado site;

import pyautogui
import time
import pandas as pd

pyautogui.press('win')
pyautogui.write('Opera')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(5.5)

pyautogui.press('tab')
pyautogui.write('gmailexemplo')
pyautogui.press('tab')
pyautogui.write('senhaexemplo')
pyautogui.press('enter')
time.sleep(1)

tabela = pd.read_csv('projeto.python/produtos.csv')
#pd sendo 
print(tabela)

for linha in tabela.index:
#sendo .index a indicação de que estamos nomeando rows. Existe também o
#.columns, usado para nomear as colunas se elas forem "inomeáveis" (por causa de quantidade).
    
    time.sleep(2)
    pyautogui.click(x=590, y=280)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    
    '''
    ou apenas 
    pyautogui.write(str(tabela.loc[linha, 'codigo']))

    '''
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    #se não existir campo de obs, não escrever nada. Não está especificado aqui.
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('home')
    