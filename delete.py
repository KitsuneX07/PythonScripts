import os

def delete_files(txt_file_path, directory_path):
    count = 0
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        file_list = {line.strip() for line in f}

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file not in file_list:
                os.remove(os.path.join(root, file))
                count += 1
            else:
                file_list.remove(file)

    if len(file_list) == 0:
        print("文件夹中的文件与txt中的列表一一对应")
    else:
        print("以下文件在txt文件中有，但在目录中没有：", file_list)

    # print(count)

txt_file_path = r'E:\gal\解包\魔女的夜宴\audio_files.txt'
directory_path = r'E:\gal\解包\魔女的夜宴\voice\１－寧々'

delete_files(txt_file_path, directory_path)