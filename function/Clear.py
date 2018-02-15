import os

def clean():
    for file in os.listdir("Compressi"):
        path="Compressi\\" + file
        if (os.path.exists(path)):
            os.remove(path)
    for file in os.listdir("Frammenti"):
        path = "Frammenti\\" + file
        if (os.path.exists(path)):
            os.remove(path)
    results=["Result\\result.bmp","Result\\jpegDirect\\result.jpeg","Result\\jpegDirect\\result.bmp"]
    for r in results:
        if(os.path.exists(r)):
            os.remove(r)