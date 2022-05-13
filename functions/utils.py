import json,os,glob
import shutil
import config as conf

def filterHiperLinks(dir,filename,arg):
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
    except Exception as e :
        err = True
        ret = e.args

    return err,ret

def copyAudioFromDownloads():
    err = False
    ret = None
    try:
        file_type = '\*wav' # se nao quiser filtrar por extenção deixe apenas *
        files = glob.glob(conf.dirDownloads + file_type)
        max_file = max(files, key=os.path.getctime)
        basename = os.path.basename(max_file)
        file_name = os.path.splitext(basename)[0]
        shutil.move(max_file,conf.appDir+"\\audios\\"+file_name+".wav")
        ret = file_name
    except Exception as e:
        err = True
        ret = e.args
    
    return err,ret  

def deleteAudio(filename):
    if os.path.exists(conf.appDir+"\\audios\\"+filename+".wav"):
        os.remove(conf.appDir+"\\audios\\"+filename+".wav")
   
    
    

    