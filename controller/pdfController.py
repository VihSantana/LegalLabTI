from logging import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Pdf:
    
    def baixar(logger:Logger,driver):
        err:bool = False
        ret:str = None
        type:int = None  
        try:
            imge = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,"//img[contains(@src,'bot-expandir.gif')]")))
            imge.click()
            logger.info(f'>> div "Inteiro Teor" expandida com sucesso ')
        except Exception as e:
            err = True
            ret = 'Erro ao expadir div "Inteiro Teor"'
            type = 1
            logger.error(f'>> Erro ao expadir div "Inteiro Teor"')
            return err,type,ret
                  
        try:
            download = driver.find_element_by_xpath("//input[@name='inteiroTeorPDF'][@type='button']")
            download.click()
            logger.info(f'>> "Inteiro Teor" baixado com sucesso ')
        except Exception as e:
            err = True
            ret = 'Erro ao fazer Download "Inteiro Teor"'
            logger.error(f'>> Erro ao fazer Download "Inteiro Teor"')
            type = 2
            return err,type,ret
        
        type = 0
        ret = "Download Efetuado com Sucesso..."
        return err,type,ret
       