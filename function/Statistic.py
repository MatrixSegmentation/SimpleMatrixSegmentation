import os
import skimage.measure as sky
import matplotlib.image as mpimg


def statistic(input_filename_img):
    img_input = os.path.getsize(input_filename_img)
    peso_cartella = 0
    for file in os.listdir("Compressi"):
        peso_cartella += os.path.getsize("Compressi\\" + file)
    immagine_input = mpimg.imread(input_filename_img)
    custom = mpimg.imread('Result\\result.bmp')
    direct = mpimg.imread('Result\\jpegDirect\\result.bmp')
    peso_jpeg = os.path.getsize("Result\\jpegDirect\\result.jpg")
    peso_compressione = os.path.getsize("Result\\mergeCompress.tar.xz")
    custom_psnr = sky.compare_psnr(immagine_input, custom)
    print("CUSTOM\tC.R. : " + str(img_input / peso_cartella) + ":1\tPSNR : " + str(custom_psnr))
    print("Compressed\t C.R. : " + str(img_input / peso_compressione))
    jpeg_psnr = sky.compare_psnr(immagine_input, direct)
    print("JPEG\tC.R. :" + str(img_input / peso_jpeg) + ":1\tPSNR : " + str(jpeg_psnr))


def statistic_frammenti(frammenti_importanti):
    for i in frammenti_importanti:
        frammento_jpeg = mpimg.imread("FrammentiJpeg\\" + i)
        frammento_custom = mpimg.imread("Compressi\\" + i.replace("bmp", "jpg"))
        frammento_originale = mpimg.imread("Frammenti\\" + i)
        psnrJpeg = sky.compare_psnr(frammento_originale, frammento_jpeg)
        psnrCustom = sky.compare_psnr(frammento_originale, frammento_custom)
        print(i + "\tJPEG PSNR : " + str(psnrJpeg) + "\tCUSTOM PSNR : " + str(psnrCustom))
