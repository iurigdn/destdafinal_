from b64 import *
from hashlib import md5
import re
import uuid
import PySimpleGUI as sg


codeMac = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
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

md5edKey = (f'{md5(password.encode()).hexdigest()}||{codeMac}')
encodedKey = b64encode(md5edKey)

print(encodedKey)
print(b64decode(encodedKey).split('||')[1]) #get mac adress again

with open("./geradorDeChave/encriptedKey.py", "w") as f:
  f.write(f'secretKey = "{encodedKey}"')