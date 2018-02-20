import matplotlib.image as mpimg
import scipy.misc


def estrazione_frammenti(file_name_img_originale, numero_divisioni, output_path="Frammenti\\"):
    img = mpimg.imread(file_name_img_originale)
    grandezza_frammento = (round(img.shape[0] / numero_divisioni), round(img.shape[1] / numero_divisioni))
    for i in range(numero_divisioni):
        for j in range(numero_divisioni):
            inizio_frammento_righe = i * grandezza_frammento[0]
            fine_frammento_righe = i * grandezza_frammento[0] + grandezza_frammento[0]
            inizio_frammento_colonne = j * grandezza_frammento[1]
            fine_frammento_colonne = j * grandezza_frammento[1] + grandezza_frammento[1]
            frammento = img[inizio_frammento_righe:fine_frammento_righe,inizio_frammento_colonne:fine_frammento_colonne]
            scipy.misc.toimage(frammento).save(output_path + "frammento" + str(i) + "," + str(j) + ".bmp")
    return grandezza_frammento

