import os

def scan_files(directory,postfix=None):
    files_list=[]

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))

    return files_list

sf = scan_files("D:\my_field\software\XMind",".html")

print(sf)

