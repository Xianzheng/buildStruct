
# srcfile 需要复制、移动的文件   
# dstpath 目的地址
 
import os
import shutil
from glob import glob
 
def mycopyfile(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        # print ("copy %s -> %s"%(srcfile, dstpath + fname))
 
 
src_dir = './out/'
dst_dir = './application/testapp/'                                    # 目的路径记得加斜杠
src_file_list = glob(src_dir + '*')                    # glob获得路径下所有文件，可根据需要修改
for srcfile in src_file_list:
    mycopyfile(srcfile, dst_dir)
# mycopyfile('./out/*', './application/testapp/')