import tarfile
import lzma


def tar_xz_compress(output_file="Result\\mergeCompress.tar.xz", input_directory="Compressi\\"):
    xz_file = lzma.LZMAFile(output_file, mode='w')
    with tarfile.open(mode='w', fileobj=xz_file) as tar_xz_file:
        tar_xz_file.add(input_directory)
    xz_file.close()
