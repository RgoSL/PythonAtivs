import pyautogui
from time import sleep

# Abrir o Zap
pyautogui.click(1025, 1055, duration=0.1)

# Abrir a conversa
pyautogui.click(378,184, duration=2)

# Ler e enviar as mensagens
with open(r'D:\CÓDIGOS\Automato\msgs.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        mensagem = linha.strip()  
        if mensagem:  
            pyautogui.click(892, 1006, duration=1)  
            pyautogui.write(mensagem)
            pyautogui.press('enter')  
            sleep(1)  