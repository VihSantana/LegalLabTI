import json,os,glob
from logging import Logger
import shutil
import config as conf

def filterHiperLinks(logger:Logger,dir,filename,arg):
    err = False
    ret = None
    try:
        urls = []
        f = open(str(dir)+"\\json\\"+filename)
        jsonHiperLinks = json.load(f)
        for idx in range(len(jsonHiperLinks['references']['url'])):
            url = jsonHiperLinks['references']['url'][idx]
            achou=str(url).find(str(arg))
            if achou != -1:
                urls.append(url)
        ret = urls 
        logger.info(">> Hiper links Filtrado com sucesso")   
    except Exception as e :
        logger.error(f">> Erro ao filtra Hiper links no json {e.args}")
        err = True
        ret = e.args

    return err,ret

def copyFromDownloads(logger:Logger,base_name:str,index:int,type:str):
    err = False
    ret = None
    try:
        file_type = '\*'+type # se nao quiser filtrar por extenção deixe apenas *
        files = glob.glob(conf.dirDownloads + file_type)
        max_file = max(files, key=os.path.getctime)
        basename = os.path.basename(max_file)
        file_name = os.path.splitext(basename)[0]
        if type=='pdf':
            shutil.copy(max_file,conf.appDir+"\\pdf_baixados\\"+base_name+"-"+str(index)+".pdf")
            os.remove(max_file)
        else:    
            shutil.move(max_file,conf.appDir+"\\audios\\"+file_name+".wav")
        ret = file_name
        logger.info(f">> Arquivo {file_name}.{type} copiado da pasta downloads") 
    except Exception as e:
        logger.error(f">> Erro ao copiar arquivo da pasta downloads  ERRO: {e.args}")
        err = True
        ret = e.args
    
    return err,ret


def deleteAudio(logger:Logger,filename):
    if os.path.exists(conf.appDir+"\\audios\\"+filename+".wav"):
        os.remove(conf.appDir+"\\audios\\"+filename+".wav")
    logger.info(f">> Deletando audio {filename}.wav") 


     
   
    
    

    