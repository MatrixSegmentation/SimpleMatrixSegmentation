from PIL import Image


def jpeg_compress(path_img_input, output, quality):
    image = Image.open(path_img_input)
    file = open(output, "w")
    image.save(file.buffer, "JPEG", quality=quality)



