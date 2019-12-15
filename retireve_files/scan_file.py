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
        print("\n"+path+' 目录文件夹，已经重新创建成功')

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
                print(newPathFile)
                fileIsExist = os.path.exists(newPathFile)   #指定文件夹下，文件名称是否已经存在
                if fileIsExist:     #如果存在
                    repetPathFile = newPath+str(num) + file     #给这个文件名称加上一个编号
                    shutil.copyfile(oldPathFile,repetPathFile)  #然后复制到指定文件夹下
                    num +=1
                    print(oldPathFile)
                else:
                    shutil.copyfile(oldPathFile,newPathFile)    #不存在，直接把文件复制到指定文件夹下


def main():
    oldPath = input("使用说明:\n"
                    "    1.需要检索文件路径，从根目录开始写，路径填写错误检索不到预期结果；\n"
                    "    2.想要保存的文件路径，最好是新建的文件夹，如果是已经存在的文件夹，\n"
                    "执行该程序后会首先删除该文件夹，然后再创建。（一定注意，防止删除掉自己的文件）；\n"
                    "    3.需要检索的文件名的后缀名，加入填写的是【.txt】，会检索出所有的【.txt】格式的文件，\n"
                    "保存到想要保存的文件路径中，如果检索出来的文件有相同的名称，保存时会在文件名的前面加上数字进行保存。\n\n"
                    "开始进行检索文件：\n"
                    "需要检索的文件路径如（D:\my_field\software\XMind）：")
    newPath = input("需要保存的文件路径如（D:\\my_field\\temp1\\）注意路径最后有个斜杠：")
    suffixname = input("需要检索的文件后缀名如（.html）：")

    if newPath.endswith("\\"):
        if oldPath+"\\" != newPath:
            get_file(oldPath,newPath,suffixname)
            input("\n检索完成，需要关闭的话点击回车，谢谢使用!")
        else:
            input("\n检索文件路径和想要保存的文件路径不能相同,请重启后，重新输入")
    else:
        input("\n失败！\n需要保存的文件路径输入的路径不正确,请检查格式和举例是否相同!    请重启后，重新输入")

if __name__ == '__main__':
    main()