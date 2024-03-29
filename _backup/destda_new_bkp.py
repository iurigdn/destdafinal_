# Destda Com e Sem Movimento Versao 20/10/2023


import time
import pyautogui
import pandas as pd
import logging
from openpyxl import Workbook, load_workbook

# import os
# os.startfile('C:\SimplesNacional\SEDIF\SEDIF.exe')

logging.basicConfig(
    handlers=[logging.FileHandler(filename="./logs/log_records.txt", encoding='utf-8', mode='a+')],
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%F %A %T",
    level=logging.INFO)


def notify(text):
    print(text)
    logging.info(text)


def addFeitaColumn(path):
    planilha = load_workbook(path)
    aba = planilha.active
    aba['G1'] = 'feita'
    planilha.save(path)


def putOk(table, empresa, path):
    try:
        table.loc[table['empresa'] == empresa, 'feita'] = 'ok'
    except:
        try:
            table.loc[table['empresa'] == empresa, 'G'] = 'ok'
        except Exception as e:
            notify(f'não coloquei o ok em {empresa} pois:', e)
            return None
    table.to_excel(path, index=False)
    notify(f'coloquei o ok em {empresa}')


def run(path):
    notify("Programa Iniciado")
    notify("Programa Iniciado")
    addFeitaColumn(path)
    df = pd.read_excel(path)
    notify('leu a planilha')

    # Informando as colunas e colocando no zip
    dias = df['dia']
    empresas = df['empresa']
    comencs = df['comenc']
    semencs = df['semenc']
    difativos = df['difativo']
    difaucs = df['difauc']

    # linha = 2 # a partir da linha 2

    pyautogui.alert(text='Ao clicar em INICIAR, a DESTDA COM MOVIMENTO será iniciada.'
                         'Verifique se a Destda está aberta na página incial'
                         'Abra a Destda e não utilize mais o teclado e mouse ', title='Atenção', button='INICIAR')

    notify('Usuário clicou em Iniciar')
    for empresa, dia, comenc, semenc, difativo, difauc in zip(empresas, dias, comencs, semencs, difativos, difaucs):
        notify('Usuário clicou em Iniciar')

        stringuedTable = list(map(lambda x: str(x), df[df['empresa'] == empresa].values[0]))
        filteredNanTable = list(filter(lambda y: y == 'nan', stringuedTable))
        print(filteredNanTable, len(filteredNanTable))

        if df[df['empresa'] == empresa]['feita'].values[0] == 'ok':
            notify(f'a empresa {empresa} ja estava feita')
        else:
            try:
                from botcity.core import DesktopBot

                class Bot(DesktopBot):
                    def action(self, execution=None):
                        try:
                            if not self.find("novodocumento", matching=0.97, waiting_time=10000):
                                self.not_found("novodocumento")
                            self.click()

                            if not self.find("nomeempresarial", matching=0.97, waiting_time=10000):
                                self.not_found("nomeempresarial")
                            self.click_relative(126, 24)

                            pyautogui.write(str(empresa))

                            time.sleep(2)
                            self.tab()
                            pyautogui.write(str(dia))
                            time.sleep(2)

                            if not self.find("carregarperiodo", matching=0.97, waiting_time=10000):
                                self.not_found("carregarperiodo")
                            self.click()

                            time.sleep(2)
                            self.page_down()
                            self.tab()
                            if len(filteredNanTable) < 5:
                                # parte azul
                                notify('parte azul')
                                self.paste("0")
                                self.tab()
                                self.tab()
                                time.sleep(2)
                                pyautogui.write("com")
                                self.tab()
                                time.sleep(2)

                                pyautogui.hotkey('alt', 'c')
                                time.sleep(2)
                                pyautogui.click(x=100, y=200)

                                time.sleep(7)
                                if not self.find("ABRIR", matching=0.97, waiting_time=10000):
                                    self.not_found("ABRIR")
                                self.click()

                                time.sleep(2)

                                if not self.find("destda", matching=0.97, waiting_time=10000):
                                    self.not_found("destda")
                                self.click()

                                if not self.find("icmsentrada", matching=0.97, waiting_time=10000):
                                    self.not_found("icmsentrada")
                                self.click()

                                if not self.find("alterarmov", matching=0.97, waiting_time=10000):
                                    self.not_found("alterarmov")
                                self.click()

                                self.tab()
                                self.tab()
                                pyautogui.write(str(comenc).replace(".", ","))

                                self.tab()
                                pyautogui.write(str(semenc).replace(".", ","))

                                self.tab()
                                pyautogui.write(str(difativo).replace(".", ","))

                                self.tab()
                                pyautogui.write(str(difauc).replace(".", ","))

                                time.sleep(2)

                                if not self.find("confirmarmov", matching=0.97, waiting_time=10000):
                                    self.not_found("confirmarmov")
                                self.click()

                                # Verificar se aparece a tela quando o valor ultrapassa 10, se não der o alerta
                                # o código continua normalmente, se der, clica em ok e continua

                                if not self.find("alerta", matching=0.97, waiting_time=3000):
                                    self.not_found("alerta")
                                else:
                                    self.click_relative(306, 89)

                                time.sleep(4)
                                if not self.find("fechartela2", matching=0.97, waiting_time=10000):
                                    self.not_found("fechartela2")
                                self.click()

                            else:
                                # parte vermelha
                                notify('parte vermelha')
                                self.paste("0")
                                self.tab()
                                self.tab()
                                time.sleep(1)
                                self.page_down()
                                time.sleep(2)
                                pyautogui.hotkey('alt', 'c')
                                time.sleep(7)
                                pyautogui.click(x=100, y=200)

                                if not self.find("ABRIR", matching=0.97, waiting_time=10000):
                                    self.not_found("ABRIR")
                                self.click()


                            time.sleep(2)
                            # if not self.find("confirmarmov", matching=0.97, waiting_time=10000):
                            #     self.not_found("confirmarmov")
                            # self.click()
                            #time.sleep(7)

                            # if not self.find("ABRIR", matching=0.97, waiting_time=10000):
                            #     self.not_found("ABRIR")
                            # self.click()

                            time.sleep(5)


                            if not self.find("encerrar", matching=0.97, waiting_time=10000):
                                self.not_found("encerrar")
                            self.click()
                            time.sleep(2)
                            if not self.find("gerardoc", matching=0.97, waiting_time=10000):
                                self.not_found("gerardoc")
                            self.click()
                            time.sleep(2)
                            if not self.find("inicproc", matching=0.97, waiting_time=10000):
                                self.not_found("inicproc")
                            self.click()
                            time.sleep(2)
                            if not self.find("certificadomb", matching=0.97, waiting_time=10000):
                                self.not_found("certificadomb")
                            self.click()
                            time.sleep(2)
                            if not self.find("autenticar", matching=0.97, waiting_time=10000):
                                self.not_found("autenticar")
                            self.click()

                            time.sleep(5)

                            if not self.find("okprocess", matching=0.97, waiting_time=10000):
                                self.not_found("okprocess")
                            self.click()

                            if not self.find("transmitir", matching=0.97, waiting_time=10000):
                                self.not_found("transmitir")
                            self.click()

                            time.sleep(4)

                            if not self.find("iniciarproc2", matching=0.97, waiting_time=10000):
                                self.not_found("iniciarproc2")
                            self.click()

                            time.sleep(4)

                            if not self.find("procfinalizado", matching=0.97, waiting_time=10000):
                                self.not_found("procfinalizado")
                            self.click_relative(262, 53)

                            if not self.find("exportar", matching=0.97, waiting_time=10000):
                                self.not_found("exportar")
                            self.click()

                            pyautogui.write(str(empresa))

                            time.sleep(2)

                            self.enter()

                            if not self.find("visualizargerado", matching=0.97, waiting_time=10000):
                                self.not_found("visualizargerado")
                            self.click_relative(264, 55)
                            time.sleep(2)
                            self.enter()

                            if not self.find("fechartela2", matching=0.97, waiting_time=10000):
                                self.not_found("fechartela2")
                            self.click()

                            time.sleep(2)
                            if not self.find("iniciar", matching=0.97, waiting_time=10000):
                                self.not_found("iniciar")
                            self.click()

                            if not self.find("fechardocumento", matching=0.97, waiting_time=10000):
                                self.not_found("fechardocumento")
                            self.click()
                            time.sleep(2)
                            if not self.find("fechartelaultima", matching=0.97, waiting_time=10000):
                                self.not_found("fechartelaultima")
                            self.click()
                            time.sleep(2)


                            # Lendo a planilha do excel para escrever o ok
                            putOk(df, empresa, path)
                        except Exception as e:
                            notify(e)

                    def not_found(self, label):
                        notify(f"Element not found: {label}")

                Bot.main()
            except Exception as e:
                notify(e)

