
from urllib.parse import urlparse
from urllib.parse import parse_qs
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  
from controller.captchaController import Captcha
from functions import generateJsonHiperLink as gjhl
from functions import utils as utl
import config as conf
chrome_options = Options()


#erro,retorno=gjhl.create(conf.appDir,"BJE-202") #gera json contendo informações pdf
erro,urls=utl.filterHiperLinks(conf.appDir,"BJE-202-url.json",conf.filtroUrls)

# faz com que o browser não abra durante o processo
if conf.showBrowser == False:
    chrome_options.add_argument("--headless")
 
## caminho para o seu webdriver
pathChromeDriver = str(conf.appDir)+"\\web-driver\\chromedriver.exe"
driver = webdriver.Chrome(pathChromeDriver, options=chrome_options)
#driver.get(urls[0])
parsed_url = urlparse(urls[len(urls)-1])
print(urls[len(urls)-1])
numeroRegistro = parse_qs(parsed_url.query)['numeroRegistro'][0]
totalLinhas = parse_qs(parsed_url.query)['totalLinhas'][0]
print(numeroRegistro)
print(totalLinhas)

try: # tenta resolver o captcha
    #sleep(3)# aguardando página carregar
    #Captcha.resolve(driver)   
    pass 
except Exception as e: 
    print(e)
    pass    

#baixa pdf
#sleep(5)


