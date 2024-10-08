# Projeto python (curso 1)
# Automação de preenchimento de dados em determinado site;
import pyautogui
import time
import pandas as pd

pyautogui.press('win')
pyautogui.write('Opera')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(5)

pyautogui.press('tab')
pyautogui.write('gmailexemplo')
pyautogui.press('tab')
pyautogui.write('senhaexemplo')
pyautogui.press('enter')
pyautogui.press('tab')


