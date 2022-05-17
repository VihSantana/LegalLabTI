from logging import Logger
from selenium import webdriver
from random import randrange
from time import sleep
from selenium.webdriver.chrome.options import Options  
from controller.captchaController import Captcha
from controller.pdfController import Pdf
from functions.utils import copyFromDownloads
import config as conf
chrome_options = Options()

class Core :
    def processarUrls(logger:Logger,urls:list,base_name:str):
        retorno = []
        if conf.showBrowser == False:
                chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(conf.pathChromeDriver, options=chrome_options)        
        logger.info(f">> Configurando Chrome ...")        
        print(f">> A baixar {len(urls)} documentos...")
        logger.info(f">> A baixar {len(urls)} documentos...")  
        for idx in range(len(urls)):
            print(f">> {idx+1} de {len(urls)} documentos baixados ... ")
            logger.info(f">> {idx+1} de {len(urls)} documentos baixados ... ")  
                
            driver.get(urls[idx])
            print(f">> Fazendo Request na url:{urls[idx]}")
            logger.info(f">> Fazendo Request na url:{urls[idx]}") 
        
            try: # tenta resolver o captcha
                sleep(3)# aguardando página carregar
                Captcha.resolve(logger,driver)   
            except Exception as e: 
                print(e)
                pass 
            
            erro:bool = True
            msg:str  = None
            type:int = None
            qtd_erro:int = 0
            while erro:
                erro,type,msg = Pdf.baixar(logger,driver)
                print(msg)
                if erro and type==1:
                    Captcha.resolve(logger,driver)
                    qtd_erro+=1
                    if qtd_erro==conf.qtd_erro:
                        erro = False
                else:
                    sleep(3)
                    logger.info(f">> Download Efetuado com sucesso ...") 
                    print(f">> Download Efetuado com sucesso ...")
                    copyFromDownloads(logger,base_name,idx+1,'pdf')
                    sleep(randrange(conf.esperar_range)) # esperar para fazer a proxima request
                        
            
            retorno.append((erro,msg,urls[idx]))
        
        return retorno             