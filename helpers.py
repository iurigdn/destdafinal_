import PySimpleGUI as sg
from hashlib import md5

class Layouts:
    def __init__(self):  
        self.password = [
            [
                sg.Text('senha:'),
                sg.InputText(background_color='#ffffff'),
            ],
            [sg.Button('verificar'), sg.Button('Cancelar')]]

        self.simple = lambda color,text: [sg.Text(text, background_color=color)]

        self.wrong = lambda text:[(self.simple(color = 'red', text = text)),([sg.Button('tentar novamente')])]
        self.ok = lambda text:[(self.simple(color = 'green', text = text)),([sg.Button('ok')])]

class Waiters:
    def __init__(self):
        self.passwordStr = ''
    
    def password(self,title,correctHash):
        window = sg.Window(title).Layout(layouts.password)
        while True:
            event, values = window.read()
            self.passwordStr = input = values[0].replace('"', '')
            userPasswordmd5 = md5(self.passwordStr.encode()).hexdigest()
            
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                exit()
            if event == 'verificar' and userPasswordmd5 == correctHash:  # if user closes window or clicks cancel
                window.close()
                break
        

    def ok(self,title):
        window = sg.Window(title).Layout(layouts.ok(text ='a senha está correta'))
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'ok':
                break
        window.close()

    # def wrong(self,title):
    #     window = sg.Window(title).Layout(layouts.wrong(text ='a sua senha está errada'))
    #     while True:
    #         event, values = window.read()
    #         if event == sg.WIN_CLOSED:
    #             window.close()
    #             exit()
    #         if event == 'tentar novamente':
    #             break
    #     window.close()

layouts = Layouts()
waiters = Waiters()