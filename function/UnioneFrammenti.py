import scipy.misc
from os import listdir
from function.UnioneFrammenti import *
import matplotlib.image as mpimg
import numpy as np


def merge(filename_into_img_input, grandezza_frammento, path_result='Result\\result.bmp', dir_merge="Compressi"):
    lista = []
    for file in listdir(dir_merge):
        lista.append(file)

    sorted(lista)

    fr0 = mpimg.imread(filename_into_img_input)
    unione = np.zeros(fr0.shape, dtype=fr0.dtype)

    for f in lista:
        frammento = mpimg.imread(dir_merge + "\\" + f)
        f = f.replace("frammento", "")
        f = f.replace(".jpg", "")
        posizione = f.split(",")
        posizione[0] = int(posizione[0])
        posizione[1] = int(posizione[1])
        inizio_colonna = posizione[0] * grandezza_frammento[0]
        inizio_riga = posizione[1] * grandezza_frammento[1]
        unione[inizio_colonna:inizio_colonna + grandezza_frammento[0],
        inizio_riga:inizio_riga + grandezza_frammento[1]] = \
            frammento[0:grandezza_frammento[0], 0:grandezza_frammento[1]]
    scipy.misc.toimage(unione).save(path_result)
