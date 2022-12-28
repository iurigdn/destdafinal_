import uuid
import re
from geradorDeChave.encriptedKey import secretKey
from geradorDeChave.b64 import *
from hashlib import md5
import PySimpleGUI as sg


def wrongScreen(message):
    layout = [
        [
            sg.Text(message, background_color='red')
        ],
        [sg.Button('ok')]]
    window = sg.Window('teste').Layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'ok':
            break
    window.close()


[payerPasswordmd5, payerMacAdress] = b64decode(secretKey).split('||')

userMacAdress = (':'.join(re.findall('..', '%012x' % uuid.getnode())))

print(payerMacAdress)
print(userMacAdress)

if payerMacAdress != userMacAdress:
    wrongScreen('este não é o computador correto')
else:
    layout = [
        [
            sg.Text('senha:'),
            sg.InputText(background_color='#ffffff'),
        ],
        [sg.Button('verificar'), sg.Button('Cancelar')]]

    window = sg.Window('teste').Layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar' or event == (
        'verificar'):  # if user closes window or clicks cancel
            password = input = values[0].replace('"', '')
            break
    window.close()

    userPasswordmd5 = md5(password.encode()).hexdigest()

    print(userPasswordmd5)
    print(payerPasswordmd5)

    if userPasswordmd5 != payerPasswordmd5:
        wrongScreen('a senha ta errada')
    else:
        layout = [
            [
                sg.Text('deu bom', background_color='green')
            ],
            [sg.Button('ok')]]
        window = sg.Window('teste').Layout(layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'ok':
                break
        window.close()
