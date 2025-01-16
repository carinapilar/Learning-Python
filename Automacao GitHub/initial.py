import pyautogui
import time

# Pegando posição do Select All
# time.sleep(5)
# print(pyautogui.position())

# Seleciona todos os itens várias vezes e dá unsubscribe
for x in range(0, 189):
    pyautogui.click(x=376, y=280)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("space")

    time.sleep(5)
