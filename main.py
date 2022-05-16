import os
import logging
import config as conf
from controller.coreController import Core
from functions import generateJsonHiperLink as gjhl
from functions import utils as utl

logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


pasta = str(conf.appDir+"\\documents")
for diretorio, subpastas, arquivos in os.walk(pasta):
    if len(arquivos)>1:
       print(f">> {len(arquivos)} arquivos a serem processados ...")
       logger.info(f">> {len(arquivos)} arquivos a serem processados ...")
    else:    
       print(f">> {len(arquivos)} arquivo a ser processado ...")
       logger.info(f">> {len(arquivos)} arquivo a ser processado ...")
    for arquivo in arquivos:
        print(f">> {arquivo} sendo processado ...")
        logger.info(f">> {arquivo} sendo processado ...")
        nomeArq = arquivo.split('.')
        nomeArq = str(nomeArq[0])
        erro:bool= None
        retorno = None
        erro,retorno=gjhl.create(logger,conf.appDir,nomeArq) #gera json contendo informações pdf
        if erro == False:
            erro,urls=utl.filterHiperLinks(logger,conf.appDir,retorno,conf.filtroUrls)
            logger.info(f">> URlS:{urls}")
            if erro == False:
                Core.processarUrls(logger,urls,nomeArq)
                




