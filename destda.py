# Destda Com Movimento Versao 1 29/11/2022

import time
import pyautogui
import pandas as pd
import logging
from openpyxl import Workbook, load_workbook

def addFeitaColumn(path):
    planilha = load_workbook(path)
    aba = planilha.active
    aba['G1'] = 'feita'
    planilha.save(path)

def putOk(table,empresa,path):
    try:
        table.loc[table['empresa']==empresa, 'feita'] = 'ok'
    except:
        try:
            table.loc[table['empresa']==empresa, 'G'] = 'ok'
        except Exception as e:
            print(f'não coloquei o ok em {empresa} pois:',e)
            return None
    table.to_excel(path,index=False)
    print(f'coloquei o ok em {empresa}')
    

def run(path):
    logging.basicConfig(
        handlers=[logging.FileHandler(filename="./logs/log_records.txt",encoding='utf-8', mode='a+')],
        format="%(asctime)s - %(levelname)s - %(message)s", 
        datefmt="%F %A %T", 
        level=logging.INFO)
    logging.info("Programa Iniciado")
    print("Programa Iniciado")
    addFeitaColumn(path)
    df = pd.read_excel(path)
    logging.info('leu a planilha')

    #Informando as colunas e colocando no zip
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
    
    logging.info('Usuário clicou em Iniciar')
    for empresa, dia, comenc, semenc, difativo, difauc in zip(empresas, dias, comencs, semencs, difativos, difaucs):
        if df[df['empresa'] == empresa]['feita'].values[0] == 'ok':
            print(f'a empresa {empresa} ja estava feita')
        else:
            try:
                from botcity.core import DesktopBot

                class Bot(DesktopBot):
                    def action(self, execution=None):
                        try:
                            if not self.find( "novodocumento", matching=0.97, waiting_time=10000):
                                self.not_found("novodocumento")
                            self.click()

                            if not self.find( "nomeempresarial", matching=0.97, waiting_time=10000):
                                self.not_found("nomeempresarial")
                            self.click_relative(126, 24)

                            pyautogui.write(str(empresa))

                            time.sleep(2)
                            self.tab()
                            pyautogui.write(str(dia))
                            time.sleep(2)

                            if not self.find( "carregarperiodo", matching=0.97, waiting_time=10000):
                                self.not_found("carregarperiodo")
                            self.click()

                            time.sleep(2)
                            self.page_down()
                            self.tab()
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

                            if not self.find( "ABRIR", matching=0.97, waiting_time=10000):
                                self.not_found("ABRIR")
                            self.click()


                            time.sleep(2)

                            if not self.find( "destda", matching=0.97, waiting_time=10000):
                                self.not_found("destda")
                            self.click()

                            if not self.find( "icmsentrada", matching=0.97, waiting_time=10000):
                                self.not_found("icmsentrada")
                            self.click()

                            if not self.find( "alterarmov", matching=0.97, waiting_time=10000):
                                self.not_found("alterarmov")
                            self.click()

                            self.tab()
                            self.tab()
                            pyautogui.write(str(comenc))

                            self.tab()
                            pyautogui.write(str(semenc))

                            self.tab()
                            pyautogui.write(str(difativo))

                            self.tab()
                            pyautogui.write(str(difauc))

                            time.sleep(2)

                            if not self.find( "confirmarmov", matching=0.97, waiting_time=10000):
                                self.not_found("confirmarmov")
                            self.click()

                            #Verificar se aparece a tela quando o valor ultrapassa 10, se não der o alerta
                            # o código continua normalmente, se der, clica em ok e continua

                            if not self.find( "alerta", matching=0.97, waiting_time=3000):
                                self.not_found("alerta")
                            else: self.click_relative(306, 89)

                            time.sleep(4)

                            if not self.find( "fechartelamov", matching=0.97, waiting_time=10000):
                                self.not_found("fechartelamov")
                            self.click()

                            time.sleep(2)
                            if not self.find( "encerrar", matching=0.97, waiting_time=10000):
                                self.not_found("encerrar")
                            self.click()
                            time.sleep(2)
                            if not self.find( "gerardoc", matching=0.97, waiting_time=10000):
                                self.not_found("gerardoc")
                            self.click()
                            time.sleep(2)
                            if not self.find( "inicproc", matching=0.97, waiting_time=10000):
                                self.not_found("inicproc")
                            self.click()
                            time.sleep(2)
                            if not self.find( "certificadomb", matching=0.97, waiting_time=10000):
                                self.not_found("certificadomb")
                            self.click()
                            time.sleep(2)
                            if not self.find( "autenticar", matching=0.97, waiting_time=10000):
                                self.not_found("autenticar")
                            self.click()


                            time.sleep(5)

                            if not self.find( "okprocess", matching=0.97, waiting_time=10000):
                                self.not_found("okprocess")
                            self.click()

                            if not self.find( "transmitir", matching=0.97, waiting_time=10000):
                                self.not_found("transmitir")
                            self.click()

                            time.sleep(4)

                            if not self.find( "iniciarproc2", matching=0.97, waiting_time=10000):
                                self.not_found("iniciarproc2")
                            self.click()

                            time.sleep(4)

                            if not self.find( "procfinalizado", matching=0.97, waiting_time=10000):
                                self.not_found("procfinalizado")
                            self.click_relative(262, 53)

                            if not self.find( "exportar", matching=0.97, waiting_time=10000):
                                self.not_found("exportar")
                            self.click()


                            pyautogui.write(str(empresa))

                            time.sleep(2)

                            self.enter()

                            if not self.find( "visualizargerado", matching=0.97, waiting_time=10000):
                                self.not_found("visualizargerado")
                            self.click_relative(264, 55)

                            self.enter()

                            if not self.find( "fechartela2", matching=0.97, waiting_time=10000):
                                self.not_found("fechartela2")
                            self.click()

                            if not self.find( "iniciar", matching=0.97, waiting_time=10000):
                                self.not_found("iniciar")
                            self.click()

                            if not self.find( "fechardocumento", matching=0.97, waiting_time=10000):
                                self.not_found("fechardocumento")
                            self.click()

                            if not self.find( "fechartelaultima", matching=0.97, waiting_time=10000):
                                self.not_found("fechartelaultima")
                            self.click()

                            #Lendo a planilha do excel para escrever o ok
                            putOk(df,empresa,path)
                        except Exception as e:
                            print(e)

                    def not_found(self, label):
                        print(f"Element not found: {label}")
                
                Bot.main()
            except Exception as e:
                print(e)


        
