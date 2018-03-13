from function.TarXzCompression import tar_xz_compress
from function.Utility import *
from function.CompressioneFrammenti import comprimi_frammenti
from function.EstrazioneFrammenti import *
from function.UnioneFrammenti import merge
from function.Compressore import jpeg_compress
from function.Statistic import *

crate_directory()
clean()

filenameIntoImgInput='ImgInput\\limone.bmp'
arr = ["1,0","2,0","2,1","3,0"]
frammentiImpo = ["frammento"+arr.pop(0)+".bmp"]

for i in arr:
    frammentiImpo.append("frammento"+i+".bmp")

foreground = 80
background = 50
qualityJpegDirect = 70
numeroDivisioni = 4
pathResutJpeg = "Result\\jpegDirect\\result.jpg"

print("Ottengo i frammenti : ")
grandezza_frammento = estrazione_frammenti(filenameIntoImgInput, numeroDivisioni)
print("End\nComprimo i frammenti : ")
comprimi_frammenti(frammentiImpo, foreground, background)
print("End\nUnisco i frammenti : ")
merge(filenameIntoImgInput, grandezza_frammento)
print("End\nCompressione diretta e salvataggio in bitmap : ")
jpeg_compress(filenameIntoImgInput, pathResutJpeg, qualityJpegDirect)
direct = mpimg.imread(pathResutJpeg)
scipy.misc.toimage(direct).save(pathResutJpeg.replace("jpg", "bmp"))
print("End\nEstraggo i frammenti dall'immagine Jpeg diretta : ")
estrazione_frammenti(pathResutJpeg, numeroDivisioni, "FrammentiJpeg\\")
print("End\n\nConfronto i risultati sui frammenti di interesse : ")
statistic_frammenti(frammentiImpo)
print("End\n\nConfronto del'immagine intera : ")
tar_xz_compress()
statistic(filenameIntoImgInput)
print("End")
