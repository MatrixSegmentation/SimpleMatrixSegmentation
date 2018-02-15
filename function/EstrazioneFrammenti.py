import matplotlib.image as mpimg
import scipy.misc


def estrazione_frammenti(file_name_img_originale, numero_divisioni, output_path="Frammenti\\"):
    img = mpimg.imread(file_name_img_originale)
    grandezza_frammento = (round(img.shape[0] / numero_divisioni), round(img.shape[1] / numero_divisioni), img.shape[2])
    for i in range(numero_divisioni):
        for j in range(numero_divisioni):
            frammento = img[i * grandezza_frammento[0]:i * grandezza_frammento[0] + grandezza_frammento[0],
                        j * grandezza_frammento[1]:j * grandezza_frammento[1] + grandezza_frammento[1]]
            scipy.misc.toimage(frammento).save(output_path + "frammento" + str(i) + "," + str(j) + ".bmp")
    return grandezza_frammento
