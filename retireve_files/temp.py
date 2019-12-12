import os



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


sf,root = scan_files("D:\my_field\software\XMind",".html")

print(sf)

