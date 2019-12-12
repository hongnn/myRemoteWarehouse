import os
import shutil

def CreateDir(path):
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        print(path+' 目录创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
def scan_files(directory,postfix=None):
    files_list=[]
    root_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(special_file)
                    root_list.append(root)
    return files_list,root_list
def CopyFile(filepath, newPath):
    # 获取当前路径下的文件名，返回List

    fileNames,root =scan_files(filepath,".html")

    for file in fileNames:

        if file.endswith(".html"):
            for i in root:



                # 将文件命加入到当前文件路径后面
                newDir = i + '/' + file
                # 如果是文件
                if os.path.isfile(newDir):
                    print(newDir)
                    newFile = newPath + file
                    shutil.copyfile(newDir, newFile)
                #如果不是文件，递归这个文件夹的路径
                else:
                    CopyFile(newDir,newPath)





CreateDir("D:\\my_field\\temp1")
CopyFile("D:\my_field\software\XMind","D:\\my_field\\temp1\\")