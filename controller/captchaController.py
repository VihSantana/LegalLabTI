from logging import Logger
from time import sleep
from functions.utils import copyFromDownloads,deleteAudio
from functions import covertAudioToText
import config as conf

class Captcha:
    
    def resolve(logger:Logger,driver):
        try:
            driver.find_element_by_xpath('//a[@href="captchaAudio.svl"]').click()
            sleep(4)# aguardando baixar o audio
            erro,nomeArq=copyFromDownloads(logger,'',0,'wav')
            if erro != True:
                err,text=covertAudioToText.convert(logger,conf.appDir,nomeArq)
                if err != True:
                    deleteAudio(logger,nomeArq)
                    pass
                elementInputCaptcha = driver.find_element_by_id("captcha_text")
                sleep(0.2)
                elementInputCaptcha.clear()
                elementInputCaptcha.click()
                sleep(0.5)
                elementInputCaptcha.send_keys(text)
                print(f">> Captcha Resolvido com sucesso")
                logger.info(f">> Captcha Resolvido com sucesso") 
        except Exception as e:
            print(f'>> Nao Precisa Fazer o Captcha... ')
            logger.error(f'>> Nao Precisa Fazer o Captcha...') 
            pass    
 
            
            
            
                
            