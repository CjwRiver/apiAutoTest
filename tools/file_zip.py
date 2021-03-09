# /usr/bin/python
# coding=utf-8
import os
import zipfile
import sys
import zlib
def un_zip():
    try:
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    path = 'D:\\TestSoftware\\PyCharm\\PyCharmProject\\apiAutoTest'  # 要进行压缩的文档目录
    start = path.rfind(os.sep) + 1
    filename = 'D:\\apiAutoTest.zip'  # 压缩后的文件名
    z = zipfile.ZipFile(filename, mode="w", compression=compression)
    try:
        for dirpath, dirs, files in os.walk(path):
            for file in files:
                if file == filename or file == "zip.py":
                    continue
                print(file)
                z_path = os.path.join(dirpath, file)
                z.write(z_path, z_path[start:])
        z.close()
    except:
        if z:
            z.close()
if __name__ == '__main__':
    un_zip()

