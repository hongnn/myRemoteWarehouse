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
        shutil.rmtree(path)
        os.makedirs(path)
        print(path+' 目录已经重新创建')

def get_dir(path):              #获取目录路径
    for root,dirs,files in os.walk(path):     #遍历path,进入每个目录都调用visit函数，，有3个参数，root表示目录路径，dirs表示当前目录的目录名，files代表当前目录的文件名
        for dir in dirs:
            #print(dir)             #文件夹名
            print(os.path.join(root,dir))      #把目录和文件名合成一个路径

def get_file(oldPath,newPath,suffixname):
    CreateDir(newPath)      #创建文件夹
    num = 1#获取文件路径
    for root, dirs, files in os.walk(oldPath):

        for file in files:
            if file.endswith(suffixname):
                oldPathFile = os.path.join(root,file)       #被检索的文件
                newPathFile = os.path.join(newPath,file)    #需要保存到指定文件下的文件
                fileIsExist = os.path.exists(newPathFile)   #指定文件夹下，文件名称是否已经存在
                if fileIsExist:     #如果存在
                    repetPathFile = newPath+str(num) + file     #给这个文件名称加上一个编号
                    shutil.copyfile(oldPathFile,repetPathFile)  #然后复制到指定文件夹下
                    num +=1
                    print(oldPathFile)
                else:
                    shutil.copyfile(oldPathFile,newPathFile)    #不存在，直接把文件复制到指定文件夹下



# oldPath ="D:\my_field\software\XMind"  # 文件夹路径
# newPath = "D:\\my_field\\temp1\\"

def main():
    oldPath = input("需要检索的文件路径如（D:\my_field\software\XMind）：")
    newPath = input("需要保存的文件路径如（D:\\my_field\\temp1\\）：")
    suffixname = input("需要检索的文件后缀名如（.html）：")
    get_file(oldPath,newPath,suffixname)


if __name__ == '__main__':
    main()