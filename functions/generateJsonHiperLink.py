
import os

def create(dir,filename):
    err = False
    ret = None
    try:
        filename = str(filename)
        os.system("pdfx "+str(dir)+"\\documents\\"+filename+".pdf -v -j -o json\\"+filename+"-url.json")
        ret = str(filename+"-url.json")
    except Exception as e:
        err = True
        ret = e.args     
    return err,ret