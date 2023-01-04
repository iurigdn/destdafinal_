from b64 import *
from hashlib import md5
import re
import uuid
import PySimpleGUI as sg
import pyperclip as pc
import sys

codeMac = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
firsthLayout = [
        [
            sg.Text('senha:'),
            sg.InputText(background_color='#ffffff'),
        ],
        [sg.Text('a sua senha será criptografada e ninguém terá acesso a ela',text_color='#fff111',)],
        [sg.Button('gerar'), sg.Button('Cancelar',)]]

finalLayout = lambda token : [
        [
            sg.Text(token)
        ],
        [sg.Button('ok'), sg.Button('copiar')]]


window = sg.Window('criação do token').Layout(firsthLayout)

while True:
    event, values = window.read()
    if event == 'gerar':  # if user closes window or clicks cancel
        password = input = values[0].replace('"', '')
    if event == sg.WIN_CLOSED or event == 'Cancelar' :
        window.close()
        sys.exit()

    break




md5edKey = (f'{md5(password.encode()).hexdigest()}||{codeMac}')
encodedKey = b64encode(md5edKey)


window = sg.Window('seu token').Layout(finalLayout(encodedKey))
while True:
    event, values = window.read()
    if event == 'copiar':
      pc.copy(encodedKey)
    if event == sg.WIN_CLOSED or event == 'ok':
        break
window.close()

print(encodedKey)
print(b64decode(encodedKey).split('||')[1]) #get mac adress again

#with open("./geradorDeChave/encriptedKey.py", "w") as f:
#  f.write(f'secretKey = "{encodedKey}"')