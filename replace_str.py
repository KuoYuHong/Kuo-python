import os
dirPath = os.getcwd()#r"你的路徑名稱"
txt_list = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
txt_list = [x for x in txt_list if x not in ['replace_FormatFactory.py']] #排除執行程式的檔案
print("所有要處理的檔名:",txt_list)
for i in txt_list:
    oldname = i
    # newname = oldname.split(' 00_')[0]+".mp3" #選擇改名規則
    newname = oldname.replace('_',' ') #選擇改名規則
    os.rename(oldname,newname)
    print(oldname+'>>>'+newname)
print("完成")