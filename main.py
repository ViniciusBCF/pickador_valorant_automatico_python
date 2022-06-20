from pyautogui import *
import pyautogui

def click(position):
    pyautogui.moveTo(position)
    pyautogui.click()

def seleciona_boneco():
    global boneco1
    global boneco2
    boneco1 = input("Selecione um número para escolher o boneco a ser pickado: "
                    "\n1-Astra 2-Breach 3-Brimstone 4-Chamber 5-Cypher"
                    "\n6-Fade 7-Jett 8-KAY/O 9-Killjoy 10-Neon"
                    "\n11-Omen 12-Phoenix 13-Raze 14-Reyna 15-Sage "
                    "\n16-Skye 17-Sova 18-Viper 19-Yoru"
                    "\nSua primeira opção é: ").strip()
    boneco2 = input("\n1-Astra 2-Breach 3-Brimstone 4-Chamber 5-Cypher"
                    "\n6-Fade 7-Jett 8-KAY/O 9-Killjoy 10-Neon"
                    "\n11-Omen 12-Phoenix 13-Raze 14-Reyna 15-Sage"
                    "\n16-Skye 17-Sova 18-Viper 19-Yoru"
                    "\nSua segunda opção é: ").strip()

def check_boneco():
    button_pos = pyautogui.locateCenterOnScreen(boneco1 + '.png', confidence=0.8)
    button_pos2 = pyautogui.locateCenterOnScreen(boneco2 + '.png', confidence=0.8)

    if button_pos != None:
        click(button_pos)
        return True

    elif button_pos2 !=None:
        click(button_pos2)
        return True

    return False

def check_confirma():
    button_pos1 = pyautogui.locateCenterOnScreen('confirmar.png', confidence=0.8)

    if button_pos1 != None:
        click(button_pos1)
        return True

    return False


def main():
    seleciona_boneco()
    while True:
        if check_boneco():
            print('Boneco selecionado.')

            break


    while True:
        if check_confirma():
            print('Boneco confirmado.')

            break

main()