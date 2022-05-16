
from logging import Logger
import os

def create(logger :Logger,dir,filename):
    err = False
    ret = None
    try:
        filename = str(filename)
        os.system("pdfx "+str(dir)+"\\documents\\"+filename+".pdf -v -j -o json\\"+filename+"-url.json")
        ret = str(filename+"-url.json")
        logger.info(f">> Create file {filename}-url.json")
    except Exception as e:
        logger.info(f">> Erro on create file {filename}-url.json")
        err = True
        ret = e.args     
    return err,ret