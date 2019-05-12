import glob
import codecs
read_files=glob.glob(r'*.txt')# 通過glob返回滿足條件的文件列表,也可以用os.listdir獲取當前路徑下的文件

with codecs.open('output.txt', 'ab+') as outfile:
    for f in read_files:
        with open(f,'rb') as infile:
            outfile.write(infile.read())
