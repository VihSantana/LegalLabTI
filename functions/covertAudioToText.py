from logging import Logger
import speech_recognition as sr
from time import sleep

def convert(logger:Logger,dir,filename):
    err = False
    ret = None
    try:
        sleep(0.3)
        r = sr.Recognizer()
        sleep(0.3)
        with sr.AudioFile(str(dir)+"\\audios\\"+filename+".wav") as source:
            sleep(0.3)
            audio_data = r.record(source)
            sleep(0.3)
            ret = r.recognize_google(audio_data,language='pt-br')
        logger.info(f">> Audio convertido com sucesso")     
    except Exception as e:
        logger.error(f">> Error ao converter audio ERRO:{e.args}")  
        err = True

    return err,ret


   