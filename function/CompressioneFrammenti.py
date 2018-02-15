import os
from function.Compressore import jpeg_compress


def comprimi_frammenti(frammenti_importanti,forground,background):

    lista_file = []
    for file in os.listdir("Frammenti"):
        lista_file.append(file)

    for s in lista_file:
        if s in frammenti_importanti:
            jpeg_compress("Frammenti\\" + s, "Compressi\\" + s.replace(".bmp",".jpg"), forground)
        else:
            jpeg_compress("Frammenti\\" + s, "Compressi\\" + s.replace(".bmp",".jpg"), background)