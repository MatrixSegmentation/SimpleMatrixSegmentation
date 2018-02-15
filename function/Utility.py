from os import path, makedirs, listdir, remove


def clean():
    for file in listdir("Compressi"):
        percorso = "Compressi\\" + file
        if path.exists(percorso):
            remove(percorso)
    for file in listdir("Frammenti"):
        percorso = "Frammenti\\" + file
        if path.exists(percorso):
            remove(percorso)
    for file in listdir("FrammentiJpeg"):
        percorso = "FrammentiJpeg\\" + file
        if path.exists(percorso):
            remove(percorso)
    results = ["Result\\result.bmp", "Result\\jpegDirect\\result.jpg", "Result\\jpegDirect\\result.bmp",
               "Result\\mergeCompress.tar.xz"]
    for r in results:
        if path.exists(r):
            remove(r)


def crate_directory(dirs=['Frammenti', 'FrammentiJpeg', 'Compressi', 'Result', 'Result\\jpegDirect']):
    for d in dirs:
        if not path.exists(d):
            makedirs(d)
