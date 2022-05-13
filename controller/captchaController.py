from time import sleep
from functions.utils import copyAudioFromDownloads,deleteAudio
from functions import covertAudioToText
import config as conf

class Captcha:
    
    def resolve(driver):
        driver.find_element_by_xpath('//a[@href="captchaAudio.svl"]').click()
        sleep(4)# aguardando baixar o audio
        erro,nomeArq=copyAudioFromDownloads()
        if erro != True:
            err,text=covertAudioToText.convert(conf.appDir,nomeArq)
            if err != True:
                deleteAudio(nomeArq)
                pass
            elementInputCaptcha = driver.find_element_by_id("captcha_text")
            sleep(0.2)
            elementInputCaptcha.click()
            sleep(0.5)
            elementInputCaptcha.send_keys(text)
            
            
            
                
            